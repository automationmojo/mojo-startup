"""
.. module:: startupvariables
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the most basic variables required to begin the startup
               of a customized mojo environment.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []

import os

from mojo.startup.startupdefaults import MOJO_STARTUP_DEFAULTS

class MOJO_STARTUP_VARIABLES:

    MJR_STARTUP_SETTINGS = None
 

def resolve_startup_variables():

    if "MJR_STARTUP_SETTINGS" in os.environ:
        MOJO_STARTUP_VARIABLES.MJR_STARTUP_SETTINGS = os.environ["MJR_STARTUP_SETTINGS"]
        MOJO_STARTUP_VARIABLES.MJR_STARTUP_SETTINGS = os.path.abspath(os.path.expandvars(os.path.expanduser(MOJO_STARTUP_VARIABLES.MJR_STARTUP_SETTINGS)))
    else:
        MOJO_STARTUP_VARIABLES.MJR_STARTUP_SETTINGS = MOJO_STARTUP_DEFAULTS.MJR_STARTUP_SETTINGS

    return