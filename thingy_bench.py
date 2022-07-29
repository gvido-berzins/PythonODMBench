import asyncio
from typing import List

from mongo_thingy import connect, Thingy

from settings import DATABASE_URL


class TestScenario(Thingy):
    call_type: str
    app: str
    platform: str
    participants: str
    condition: str


class TestData(Thingy):
    test_id: str
    datetime: str
    metric: str
    path: str
    data: List[float]
    time: List[float]


class Test(Thingy):
    collection_name = "Test"

    day: str
    path: str
    test_scenario: TestScenario
    test_data: TestData


def all_records() -> List[Test]:
    connect(host=DATABASE_URL)
    records = Test.find()
    return list(records)


# print(all_records())
