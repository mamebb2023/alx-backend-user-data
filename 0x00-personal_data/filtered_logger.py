#!/usr/bin/env python3
""" Filtered Logger
"""
import logging
import re
from typing import List
import mysql.connector
from os import getenv

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:  # nopep8
    """ Filter the input user data
    """
    for data in fields:
        message = re.sub(fr'{data}=.+?{separator}', f'{data}={redaction}{separator}', message)  # nopep8
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the log input
        """
        return filter_datum(
                self.fields,
                self.REDACTION,
                super(RedactingFormatter, self).format(record),
                self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ Returns a logger object
    """
    logger = logging.getLogger("user_data")
    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream)
    logger.propagate = False
    logger.setLevel(logging.INFO)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Get a sequre database access
    """
    return mysql.connector.connection(
                user=getenv('PERSONAL_DATA_DB_USERNAME'),
                password=getenv('PERSONAL_DATA_DB_PASSWORD'),
                host=getenv('PERSONAL_DATA_DB_HOST'),
                database=getenv('PERSONAL_DATA_DB_NAME')
            )
