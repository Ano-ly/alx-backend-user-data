#!/usr/bin/env python3
"""Filter datum function"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """Obfuscate important personal data"""
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]+{separator}", f"{field}={redaction}{separator}", message)
    return(message)

