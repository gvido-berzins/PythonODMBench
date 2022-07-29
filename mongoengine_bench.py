import asyncio
from typing import List

from mongoengine import (
    EmbeddedDocument,
    Document,
    EmbeddedDocumentField,
    ListField,
    FloatField,
    StringField,
    connect,
)

from settings import DATABASE_URL


class TestScenario(EmbeddedDocument):
    call_type: str = StringField()
    app: str = StringField()
    platform: str = StringField()
    participants: str = StringField()
    condition: str = StringField()


class TestData(EmbeddedDocument):
    test_id: str = StringField()
    datetime: str = StringField()
    metric: str = StringField()
    path: str = StringField()
    data: List[float] = ListField(FloatField())
    time: List[float] = ListField(FloatField())


class Test(Document):
    day: str = StringField()
    path: str = StringField()
    test_scenario: TestScenario = EmbeddedDocumentField(TestScenario)
    test_data: TestData = EmbeddedDocumentField(TestData)

    meta = {"collection": "Test"}


def all_records() -> List[Test]:
    connect(host=DATABASE_URL)
    records = Test.objects
    return records
