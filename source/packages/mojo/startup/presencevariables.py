"""
.. module:: presencevariables
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the most basic variables required to begin the startup
               of a customized mojo environment.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []

import os

from mojo.collections.contextpaths import ContextPaths
from mojo.collections.wellknown import ContextSingleton

from mojo.startup.startupconfigloader import StartupConfigLoader
from mojo.startup.presencesettings import MOJO_PRESENCE_DEFAULTS

class MOJO_PRESENCE_VARIABLES:

    MJR_NAME = None
    MJR_HOME_DIRECTORY = None
    MJR_EXTENSION_MODULES = None

def resolve_presence_variables():

    scloader = StartupConfigLoader("MOJO-STARTUP")

    ctx = ContextSingleton()

    MOJO_PRESENCE_VARIABLES.MJR_NAME = scloader.get_variable_value("MJR_NAME", default=MOJO_PRESENCE_DEFAULTS.MJR_NAME)
    ctx.insert(ContextPaths.PRESENCE_NAME, MOJO_PRESENCE_VARIABLES.MJR_NAME)

    MOJO_PRESENCE_VARIABLES.MJR_HOME_DIRECTORY = scloader.get_variable_value("MJR_HOME_DIRECTORY", default=MOJO_PRESENCE_DEFAULTS.MJR_HOME_DIRECTORY)
    MOJO_PRESENCE_VARIABLES.MJR_HOME_DIRECTORY = os.path.abspath(os.path.expandvars(os.path.expanduser(MOJO_PRESENCE_VARIABLES.MJR_HOME_DIRECTORY)))
    ctx.insert(ContextPaths.PRESENCE_HOME_DIRECTORY, MOJO_PRESENCE_VARIABLES.MJR_HOME_DIRECTORY)

    MOJO_PRESENCE_VARIABLES.MJR_EXTENSION_MODULES = scloader.get_variable_value("MJR_EXTENSION_MODULES", default=MOJO_PRESENCE_DEFAULTS.MJR_EXTENSION_MODULES)
    ctx.insert(ContextPaths.PRESENCE_EXTENSION_MODULES, MOJO_PRESENCE_VARIABLES.MJR_EXTENSION_MODULES)

    return
