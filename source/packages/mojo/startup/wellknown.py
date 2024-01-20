
import os

from configparser import ConfigParser

# NOTE: This code is loaded super early where there is likely to only be a single thread
#       so there is likely no need for any locking.

STARTUP_CONFIG = None

from mojo.startup.startupvariables import MOJO_STARTUP_VARIABLES

def StartupConfigSingleton():

    global STARTUP_CONFIG

    if STARTUP_CONFIG is None:
        STARTUP_CONFIG = ConfigParser()
        if os.path.exists(MOJO_STARTUP_VARIABLES.MJR_STARTUP_SETTINGS):
            STARTUP_CONFIG.read(MOJO_STARTUP_VARIABLES.MJR_STARTUP_SETTINGS)

    return STARTUP_CONFIG

