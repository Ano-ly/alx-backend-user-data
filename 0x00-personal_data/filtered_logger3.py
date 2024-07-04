#!/usr/bin/env python3
"""Filter datum function"""
import logging
import re
from typing import List, Sequence


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """Obfuscate important personal data"""
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]+{separator}", f"{field}={redaction}{separator}", message)
    return(message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Sequence):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format a record""" 
        new_str = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        record.msg = new_str
        return (super(RedactingFormatter, self).format(record))


