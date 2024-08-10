"""
.. module:: startupdefaults
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the most basic variables required to begin the startup
               of a customized mojo environment.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []

import os

class MOJO_STARTUP_DEFAULTS:

    MJR_STARTUP_SETTINGS = os.path.expanduser(os.path.join("~", ".mojo.config"))

