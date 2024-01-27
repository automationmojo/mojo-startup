
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
    
    def test_config_loads_from_environment_with_converter(self):

        tmp_config_file = tempfile.mktemp()
        with open(tmp_config_file, 'w+') as tcf:
            tcf.write(TEST_CONFIGURATION)

        os.environ["MJR_STARTUP_SETTINGS"] = tmp_config_file

        os.environ["both_variable"] = "blah,blahblah,blahblahblah"

        from mojo.startup.startupconfigloader import StartupConfigLoader

        scloader = StartupConfigLoader("BLAH")
        csv_converter = lambda sval: set(sval.split(','))

        sval = scloader.get_variable_value("both_variable", default="fromdefault", converter=csv_converter)

        assert(type(sval) == set)
        assert(len(sval) == 3)
        assert(sval[0] == 'blah')
        assert(sval[2] == 'blahblahblah')

        return

if __name__ == '__main__':
    unittest.main()
