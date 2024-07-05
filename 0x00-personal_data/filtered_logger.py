#!/usr/bin/env python3
"""Filter datum function"""
import logging
import mysql.connector
import os
import re
from typing import List, Sequence


PII_FIELDS = ("phone", "ssn", "password", "email", "name")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate important personal data"""
    for field in fields:
        message = re.sub(rf"{field}=[^{separator}]+{separator}",
                         rf"{field}={redaction}{separator}", message)
    return (message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialise instance"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format a record"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return (super(RedactingFormatter, self).format(record))


def get_logger() -> logging.Logger:
    """Return new Logger object instance"""
    new_logger = logging.getLogger("user_data")
    new_logger.setLevel(logging.INFO)
    new_logger.propagate = False
    new_handler = logging.StreamHandler()
    new_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    new_logger.addHandler(new_handler)
    return (new_logger)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to a protected sql database"""
    uname = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    pw = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    dbname = os.environ.get("PERSONAL_DATA_DB_NAME")

    connect = f"server={host};user={uname};database={dbname};\
port=3306;password={pw}"
    return (mysql.connector.connect(host=host,
                                    user=uname,
                                    database=dbname,
                                    password=pw))
