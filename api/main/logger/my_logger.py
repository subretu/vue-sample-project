import logging
from pythonjsonlogger import jsonlogger
import datetime
from pytz import timezone


class JsonFormatter(jsonlogger.JsonFormatter):
    def parse(self):
        return [
            "process",
            "timestamp",
            "level",
            "name",
            "message",
            "stack_info",
        ]

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            now = datetime.datetime.now(timezone("Asia/Tokyo")).strftime(
                "%Y-%m-%dT%H:%M:%S%z"
            )
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


def set_logger(module_name):
    logger = logging.getLogger(module_name)

    streamHandler = logging.StreamHandler()

    formatter = JsonFormatter()
    streamHandler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    streamHandler.setLevel(logging.DEBUG)

    logger.addHandler(streamHandler)

    return logger
