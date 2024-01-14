#!/usr/bin/env python3
""" Filtered Logger
"""
import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:  # nopep8
    """ Filter the input user data
    """
    for data in fields:
        message = re.sub(fr'{data}=.+?{separator}', f'{data}={redaction}{separator}', message)  # nopep8
    return message
