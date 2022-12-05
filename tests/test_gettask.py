import pytest
from api.main.routers import controllers


class Test:
    def test_get_task(self):
        result = controllers.get_task(1)

        assert result == [{"id": 1, "task": "ローソンに行く", "limitd": "2022-10-01"}]
