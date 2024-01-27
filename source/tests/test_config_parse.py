
import unittest

import os
import tempfile

TEST_CONFIGURATION = """
[BLAH]
file_variable=fromfile
both_variable=fromfile
"""

class ConfigurationTests(unittest.TestCase):

    def setUp(self):

        tmp_config_file = tempfile.mktemp()
        with open(tmp_config_file, 'w+') as tcf:
            tcf.write(TEST_CONFIGURATION)

        os.environ["MJR_STARTUP_SETTINGS"] = tmp_config_file

        return

    def test_config_loads_from_file(self):

        from mojo.startup.startupconfigloader import StartupConfigLoader

        scloader = StartupConfigLoader("BLAH")

        sval = scloader.get_variable_value("file_variable", default="fromdefault")

        assert(sval == "fromfile")

        return
    
    def test_config_loads_from_environment(self):

        tmp_config_file = tempfile.mktemp()
        with open(tmp_config_file, 'w+') as tcf:
            tcf.write(TEST_CONFIGURATION)

        os.environ["MJR_STARTUP_SETTINGS"] = tmp_config_file

        os.environ["both_variable"] = "fromenviron"

        from mojo.startup.startupconfigloader import StartupConfigLoader

        scloader = StartupConfigLoader("BLAH")

        sval = scloader.get_variable_value("both_variable", default="fromdefault")

        assert(sval == "fromenviron")

        return
    
    def test_config_loads_from_default(self):

        tmp_config_file = tempfile.mktemp()
        with open(tmp_config_file, 'w+') as tcf:
            tcf.write("")

        from mojo.startup.startupconfigloader import StartupConfigLoader

        scloader = StartupConfigLoader("BLAH")

        sval = scloader.get_variable_value("default_variable", default="fromdefault")

        assert(sval == "fromdefault")

        return

if __name__ == '__main__':
    unittest.main()
