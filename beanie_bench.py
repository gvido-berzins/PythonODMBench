import asyncio
from typing import Any, List

import motor.motor_asyncio
import pymongo
from beanie import init_beanie
from beanie.odm.operators.find.comparison import BaseFindComparisonOperator
from beanie.operators import GTE, LT, In
from settings import DATABASE_URL
from typing import List, Optional, Sequence, Union

from beanie import Document, Indexed
from pydantic import BaseModel, Field


class TestScenario(BaseModel):
    call_type: str
    app: str
    platform: str
    participants: str
    condition: str


class TestData(BaseModel):
    datetime: str
    metric: str
    path: Indexed(str, unique=True) = Field(repr=False)
    data: List[float] = Field(repr=False)
    time: List[float] = Field(repr=False)


class Test(Document):
    day: str
    path: Indexed(str, unique=True) = Field(repr=False)
    test_scenario: TestScenario
    test_data: TestData

    class Config:
        orm_mode = True


def all_records() -> List[Test]:
    """Get test data from the database"""
    return asyncio.run(a_get())


async def a_get() -> List[Test]:
    """Asynchronously get test data"""
    client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
    await init_beanie(database=client.test, document_models=[Test])

    test_docs = await Test.find().to_list()
    return test_docs
