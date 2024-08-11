
"""
.. module:: presencesettings
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the settings necessary to establish a presence on the users machine.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []

from typing import Optional

import os

from mojo.startup.startupdefaults import MOJO_STARTUP_DEFAULTS

class MOJO_PRESENCE_DEFAULTS:

    MJR_NAME = "MJR"
    MJR_HOME_DIRECTORY = os.path.expanduser(os.path.join("~", MJR_NAME.lower()))
    MJR_EXTENSION_MODULES = ""
    

PRESENCE_SETTINGS_ESTABLISHED = False


def establish_presence_settings(*, name: Optional[str]=None, home_dir: Optional[str]=None, settings_file: Optional[str]=None, extension_modules: Optional[str]=None, **other):
    """
        The `establish_extension_settings` method is called to modify the name and home folder of the
        environment.  This is accomplished by overloading a the 'Startup' defaults.  The name and home
        directory might still be changed later during the 'Parameterize' phase.

        :param name: A one word name for the environment.
        :param home_directory: The home directory where configuration files and results will be stored.
    """

    global PRESENCE_SETTINGS_ESTABLISHED

    if not PRESENCE_SETTINGS_ESTABLISHED:
        PRESENCE_SETTINGS_ESTABLISHED = True

        if name is not None:
            MOJO_PRESENCE_DEFAULTS.MJR_NAME = name
        if home_dir is not None:
            MOJO_PRESENCE_DEFAULTS.MJR_HOME_DIRECTORY = home_dir
        if settings_file is not None:
            MOJO_STARTUP_DEFAULTS.MJR_STARTUP_SETTINGS = settings_file
        if extension_modules is not None:
            MOJO_PRESENCE_DEFAULTS.MJR_EXTENSION_MODULES = extension_modules

    return

