
import unittest

import os
import tempfile

TEST_CONFIGURATION = """
[BLAH]
test_setting=blah
"""

class ConfigurationTests(unittest.TestCase):

    def test_config_parse(self):

        tmp_config_file = tempfile.mktemp()
        with open(tmp_config_file, 'w+') as tcf:
            tcf.write(TEST_CONFIGURATION)

        os.environ["MJR_STARTUP_SETTINGS"] = tmp_config_file

        from mojo.startup.wellknown import StartupConfigSingleton

        suconf = StartupConfigSingleton()

        blah_sec = suconf["BLAH"]
        sval = blah_sec["test_setting"]

        assert(sval == "blah")

        return

if __name__ == '__main__':
    unittest.main()
