=======================
mojo-startup
=======================
This package sets up a pattern for extremely early pre-configuration of variable extensibility
hook for the startup configuration.  This module looks for a single environment variable to be set:

.. code-block::

    MJR_STARTUP_SETTINGS

The value of this variable is accessed like so:

.. code-block::

    from mojo.startup.startupvariables import MOJO_STARTUP_VARIABLES
    
    print(MOJO_STARTUP_VARIABLES.MJR_STARTUP_SETTINGS)


The `MJR_STARTUP_SETTINGS` variable is set to the path for a config file that should point to the
configuration file that is used to startup the runtime.

The default value for the `MJR_STARTUP_SETTINGS` variable is `~/.mojo.config`.

The `mojo-startup` module makes a singleton `ConfigParser` available for other modules to use.  This
configuration parser can be accessed by:

.. code-block::
    
    from mojo.startup.wellknown import StartupConfigSingleton
    
    cparser = StartupConfigSingleton()
    
    defaults_section = cparser["DEFAULTS"]
    someval = defaults_section["SOME_VARIABLE"]

===========
Description
===========
This module does one very important thing.  It establishes the path for all other 'mojo' packages
on where to load default config from.  This is very important because it provides extensibility
as early as possible in the running of any code.

The pattern established for defaults for variables is:
* Variable is set to a hard coded default
* Startup configuration is checked for an override
* The environment variables are checked for an override

=================
Code Organization
=================
* .vscode - Common tasks
* development - This is where the runtime environment scripts are located
* repository-setup - Scripts for homing your repository and to your checkout and machine setup
* userguide - Where you put your user guide
* source/packages - Put your root folder here 'source/packages/(root-module-folder)'
* source/sphinx - This is the Sphinx documentation folder
* workspaces - This is where you add VSCode workspaces templates and where workspaces show up when homed.

==========
References
==========

- `User Guide <userguide/userguide.rst>`
- `Coding Standards <userguide/10-00-coding-standards.rst>`
