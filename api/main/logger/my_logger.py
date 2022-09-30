import logging
from pythonjsonlogger import jsonlogger
import datetime
from pytz import timezone


class JsonFormatter(jsonlogger.JsonFormatter):
    def parse(self):
        return [
            "level",
            "funcName",
            "process",
            "timestamp",
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
    # loggerの設定
    logger = logging.getLogger(module_name)
    # ログが重複して出ないようクリア
    logger.handlers.clear()

    # handkerの設定
    streamHandler = logging.StreamHandler()

    # ログ出力のフォーマッターの設定
    formatter = JsonFormatter()
    streamHandler.setFormatter(formatter)

    # ログレベルの設定
    logger.setLevel(logging.DEBUG)
    streamHandler.setLevel(logging.DEBUG)

    # loggerにhanderを追加
    logger.addHandler(streamHandler)

    return logger
