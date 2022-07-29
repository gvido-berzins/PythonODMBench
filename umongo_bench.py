import asyncio
from typing import List

from pymongo import MongoClient
from umongo import Document, EmbeddedDocument
from umongo.fields import StrField, ListField, FloatField, EmbeddedField
from umongo.frameworks import PyMongoInstance

from settings import DATABASE_URL

db = MongoClient(host=DATABASE_URL).test
instance = PyMongoInstance(db)


@instance.register
class TestScenario(EmbeddedDocument):
    call_type: str = StrField()
    app: str = StrField()
    platform: str = StrField()
    participants: str = StrField()
    condition: str = StrField()


@instance.register
class TestData(EmbeddedDocument):
    test_id: str = StrField()
    datetime: str = StrField()
    metric: str = StrField()
    path: str = StrField()
    data: List[float] = ListField(FloatField())
    time: List[float] = ListField(FloatField())


@instance.register
class Test(Document):
    day: str = StrField()
    path: str = StrField()
    test_scenario: TestScenario = EmbeddedField(TestScenario)
    test_data: TestData = EmbeddedField(TestData)

    class Meta:
        collection_name = "Test"


def all_records() -> List[Test]:
    records = Test.find()
    return list(records)


# print(list(all_records()))
