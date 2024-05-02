"""
.. module:: wellknown
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that provides a wellknow startup configuration singleton.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []

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

