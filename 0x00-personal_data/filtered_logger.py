#!/usr/bin/env python3
"""Filter datum function"""
import logging
import re
from typing import List, Sequence


PII_FIELDS = ("phone", "ssn", "password", "ip", "email")


def filter_datum(fields: Sequence[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscate important personal data"""
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]+{separator}", f"{field}={redaction}{separator}", message)
    return (message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Sequence[str]):
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
