from starlette.requests import Request
from fastapi import Depends, Body
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from main.connection import get_connection
from main.query import (
    get_date_summary,
    get_time_summary,
    delete_id,
    insert_data,
    get_json_data,
)
from main.logger.my_logger import logging_function, set_logger


logger = set_logger("uvicorn")

router = APIRouter()


@router.get("/day")
@logging_function(logger)
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

    # logger.info(response_data)

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


@router.post("/insertdata")
def insertdata(input_data: dict):
    conn = get_connection()
    cur = conn.cursor()

    input_id = int(input_data["id"])
    input_opsdate = input_data["opsdate"]
    input_value = int(input_data["value"])

    print(input_id)
    print(input_opsdate)
    print(input_value)

    insert_data(conn, cur, input_id, input_opsdate, input_value)

    cur.close()
    conn.close()


@router.get("/task/{is_first}")
@logging_function(logger)
def get_task(request: Request, is_first):
    if is_first == "1":
        response_data = [{"id": 1, "task": "ローソンに行く", "limitd": "2022-10-01"}]
    else:
        response_data = [{"id": 2, "task": "ファミマに行く", "limitd": "2022-11-01"}]

    return JSONResponse(content=response_data)


@router.get("/jsondata")
@logging_function(logger)
def get_json(request: Request):
    conn = get_connection()
    cur = conn.cursor()
    result_json = get_json_data(cur)

    return JSONResponse(content=result_json)


@router.get("/get_member/{id}")
@logging_function(logger)
def get_member_name(request: Request, id):
    conn = get_connection()
    cur = conn.cursor()
    result_json = get_member_name(cur, id)

    cur.close()
    conn.close()

    return JSONResponse(content=result_json)
