
import unittest

import os
import tempfile

TEST_CONFIGURATION = """
[BLAH]
test_setting=fromfile
"""

class ConfigurationTests(unittest.TestCase):

    def test_config_loads_from_file(self):

        tmp_config_file = tempfile.mktemp()
        with open(tmp_config_file, 'w+') as tcf:
            tcf.write(TEST_CONFIGURATION)

        os.environ["MJR_STARTUP_SETTINGS"] = tmp_config_file

        from mojo.startup.startupconfigloader import StartupConfigLoader

        scloader = StartupConfigLoader("BLAH")

        sval = scloader.get_variable_value("test_setting")

        assert(sval == "fromfile")

        return
    
    def test_config_loads_from_environment(self):

        tmp_config_file = tempfile.mktemp()
        with open(tmp_config_file, 'w+') as tcf:
            tcf.write(TEST_CONFIGURATION)

        os.environ["MJR_STARTUP_SETTINGS"] = tmp_config_file
        os.environ["test_setting"] = "fromenviron"

        from mojo.startup.startupconfigloader import StartupConfigLoader

        scloader = StartupConfigLoader("BLAH")

        sval = scloader.get_variable_value("test_setting")

        assert(sval == "fromenviron")

        return

if __name__ == '__main__':
    unittest.main()
