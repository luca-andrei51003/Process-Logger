import re

from datetime import time
from enum import Enum


class LogStatus(Enum):
    INFO = "INFO"
    DEBUG = "DEBUG"
    ERROR = "ERROR"


class Log:
    REGEX = r'^(?P<ts>([0-9]{2}:){2}[0-9]{2}) - \[(?P<status>[A-Z]+)\] - (?P<app>[^ ]+) .*'

    def __init__(self, app: str, status: LogStatus, timestamp: time):
        self.app = app
        self.status = status
        self.timestamp = timestamp

    @classmethod
    def from_string(cls, log_line: str):
        match = re.fullmatch(Log.REGEX, log_line)
        if not match:
            return None
        return cls(match["app"], match["status"], time.fromisoformat(match["ts"]))

    def __str__(self):
        return f'TS: {self.timestamp}; APP: {self.app}; STATUS: {self.status}'
