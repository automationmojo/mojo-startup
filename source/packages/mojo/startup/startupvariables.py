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

class MOJO_STARTUP_VARIABLES:

    MJR_STARTUP_SETTINGS = os.path.expanduser(os.path.join("~", ".mojo.config"))
    if "MJR_STARTUP_SETTINGS" in os.environ:
        MJR_STARTUP_SETTINGS = os.environ["MJR_STARTUP_SETTINGS"]
        MJR_STARTUP_SETTINGS = os.path.abspath(os.path.expandvars(os.path.expanduser(MJR_STARTUP_SETTINGS)))
