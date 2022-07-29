from typing import List

from attrs import define
from cattrs import structure
import pymongo

from settings import DATABASE_URL


@define
class TestScenario:
    call_type: str
    app: str
    platform: str
    participants: str
    condition: str


@define
class TestData:
    test_id: str
    datetime: str
    metric: str
    path: str
    data: List[float]
    time: List[float]


@define
class Test:
    day: str
    path: str
    test_scenario: TestScenario
    test_data: TestData


def all_records() -> List[Test]:
    client = pymongo.MongoClient(DATABASE_URL)
    records = client.test.Test.find()
    tests = structure(records, List[Test])
    return tests
