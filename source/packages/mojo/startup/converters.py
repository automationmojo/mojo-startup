"""
.. module:: converters
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains various converters that are used to convert settings into python types.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []

from typing import List

def sep_value_to_list_converter(sval: str, sep: str) -> List[str]:
    
    val_list = []
    for v in sval.split(sep):
        val_list.append(v.strip())

    return val_list

def sep_value_to_unique_list_converter(sval: str, sep: str) -> List[str]:
    
    val_set = set()
    for v in sval.split(sep):
        val_set.add(v.strip())

    val_list = list(val_set)

    return val_list


CSV_TO_LIST_CONVERTER = lambda sval: sep_value_to_list_converter(sval, ',')
CSV_TO_UNIQUE_LIST_CONVERTER = lambda sval: sep_value_to_unique_list_converter(sval, ',')

COLSV_TO_LIST_CONVERTER = lambda sval: sep_value_to_list_converter(sval, ':')
COLSV_TO_UNIQUE_LIST_CONVERTER = lambda sval: sep_value_to_unique_list_converter(sval, ':')

SCSV_TO_LIST_CONVERTER = lambda sval: sep_value_to_list_converter(sval, ';')
SCSV_TO_UNIQUE_LIST_CONVERTER = lambda sval: sep_value_to_unique_list_converter(sval, ';')

SPSV_TO_LIST_CONVERTER = lambda sval: sep_value_to_list_converter(sval, ' ')
SPSV_TO_UNIQUE_LIST_CONVERTER = lambda sval: sep_value_to_unique_list_converter(sval, ' ')