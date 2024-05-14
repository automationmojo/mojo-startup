"""
.. module:: converters
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains various converters that are used to convert settings into python types.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []

from typing import List, Union


def convert_value_to_bool(sval: Union[bytes, str, int]) -> bool:
    
    rtnval = None

    sval_type = type(sval)
    if sval_type == bool:
        rtnval = sval
    elif sval_type == bytes:
        sval_lower = sval.lower()
        if sval_lower in [b'1', b'true', b'yes']:
            rtnval = True
        elif sval_lower in [b'0', b'false', b'no']:
            rtnval = False
    elif sval_type == str:
        sval_lower = sval.lower()
        if sval_lower in ['1', 'true', 'yes']:
            rtnval = True
        elif sval_lower in ['0', 'false', 'no']:
            rtnval = False
    elif sval_type == int:
        if sval == 1:
            rtnval = True
        elif sval == 0:
            rtnval = False
    
    if rtnval is None:
        errmsg =f"Unable to convert setting type={sval_type} value={sval} to a bool."
        raise ValueError(errmsg)

    return rtnval


def convert_sep_value_to_list(sval: str, sep: str) -> List[str]:

    val_list = []
    for v in sval.split(sep):

        # Skip empty space items created for whitespace seperators
        if (sep == ' ' or sep == '\t') and v == '':
            continue
        
        val_list.append(v.strip())

    return val_list


def convert_sep_value_to_unique_list(sval: str, sep: str) -> List[str]:
    
    val_set = set()
    for v in sval.split(sep):

        # Skip empty space items created for whitespace seperators
        if (sep == ' ' or sep == '\t') and v == '':
            continue

        val_set.add(v.strip())

    val_list = list(val_set)

    return val_list


CSV_TO_LIST_CONVERTER = lambda sval: convert_sep_value_to_list(sval, ',')
CSV_TO_UNIQUE_LIST_CONVERTER = lambda sval: convert_sep_value_to_unique_list(sval, ',')

COLSV_TO_LIST_CONVERTER = lambda sval: convert_sep_value_to_list(sval, ':')
COLSV_TO_UNIQUE_LIST_CONVERTER = lambda sval: convert_sep_value_to_unique_list(sval, ':')

SCSV_TO_LIST_CONVERTER = lambda sval: convert_sep_value_to_list(sval, ';')
SCSV_TO_UNIQUE_LIST_CONVERTER = lambda sval: convert_sep_value_to_unique_list(sval, ';')

SPSV_TO_LIST_CONVERTER = lambda sval: convert_sep_value_to_list(sval, ' ')
SPSV_TO_UNIQUE_LIST_CONVERTER = lambda sval: convert_sep_value_to_unique_list(sval, ' ')
