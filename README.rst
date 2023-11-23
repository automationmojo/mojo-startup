=======================
mojo-startup
=======================
This package setups up a pattern for extremely early pre-configuration settings and behaviors.

===========
Description
===========
This module does one thing very important.  It establishes the path for all other 'mojo' packages
on where to load default config from.  This is very important because it provides extensibility
as early as possible in the running of any code.

The pattern established for defaults is that a variable is:
* Variable is set to a hard coded default
* startup configuration is checked for an override
* the environment variables are checked for an override

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
