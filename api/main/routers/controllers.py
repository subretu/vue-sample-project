from starlette.requests import Request
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from main.connection import get_connection
from main.query import get_date_summary, get_time_summary, delete_id
import logging
from logging import getLogger, StreamHandler, Formatter
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
            # https://qiita.com/yoppe/items/4260cf4ddde69287a632
            now = datetime.datetime.now(timezone("Asia/Tokyo")).strftime(
                "%Y-%m-%dT%H:%M:%S%z"
            )
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


# loggerの設定
logger = getLogger("uvicorn")
logger.setLevel(logging.DEBUG)
# handlerの生成
stream_handler = StreamHandler()
stream_handler.setLevel(logging.DEBUG)
# ログ出力フォーマット設定
"""
handler_format = Formatter(
    '{"name": %(name)s, "asctime": %(asctime)s, "level": %(levelname)s, "message": %(message)s}'
)
stream_handler.setFormatter(handler_format)
"""
formatter = JsonFormatter()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

router = APIRouter()


@router.get("/day")
def get_day(request: Request):
    conn = get_connection()
    cur = conn.cursor()
    result_data_day = get_date_summary(cur)

    response_data = []

    for item, item1, item2 in result_data_day:
        response_data.append(
            {"id": item, "label": item1.strftime("%Y-%m-%d"), "data": item2}
        )

    cur.close()
    conn.close()

    logger.info(response_data)

    return JSONResponse(content=response_data)


@router.get("/time")
def get_time(request: Request):
    conn = get_connection()
    cur = conn.cursor()
    result_data_time = get_time_summary(cur)

    labels1, values1 = [], []

    for item1, item2 in result_data_time:
        labels1.append(item1.strftime("%Y-%m-%d %H:%M:%S"))
        values1.append(item2)

    cur.close()
    conn.close()

    return JSONResponse(
        content={
            "label": labels1,
            "data": values1,
        }
    )


@router.get("/delete/{id}")
def detele(request: Request, id):
    conn = get_connection()
    cur = conn.cursor()
    delete_id(conn, cur, id)

    cur.close()
    conn.close()
