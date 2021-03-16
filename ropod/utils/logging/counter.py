# Taken from https://stackoverflow.com/questions/57803815/how-to-create-python-logger-with-record-number-in-the-log-file

import logging


class RecordCounter:
    _instance = None
    _count = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def count(self):
        self._count += 1
        return self._count


class ContextFilter(logging.Filter):
    def filter(self, record):
        record.record_number = RecordCounter().count()
        return True
