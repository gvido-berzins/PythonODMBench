import asyncio
from typing import List

from minimongo import Model

from settings import DATABASE_URL


class TestScenario(Model):
    call_type: str
    app: str
    platform: str
    participants: str
    condition: str


class TestData(Model):
    test_id: str
    datetime: str
    metric: str
    path: str
    data: List[float]
    time: List[float]


class Test(Model):
    database = "test"
    collection = "Test"

    # day: str
    # path: str
    # test_scenario: TestScenario
    # test_data: TestData


def all_records() -> List[Test]:
    connect(host=DATABASE_URL)
    records = Test.collection.find()
    return list(records)


print(all_records())
