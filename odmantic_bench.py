import asyncio
from typing import List, Optional

import motor
from odmantic import Field, Model
from odmantic import AIOEngine
from pydantic import BaseModel

from settings import DATABASE_URL


class TestScenario(BaseModel):
    call_type: str
    app: str
    platform: str
    participants: str
    condition: str


class TestData(BaseModel):
    datetime: str
    metric: str
    path: str = Field(repr=False)
    data: List[float] = Field(repr=False)
    time: List[float] = Field(repr=False)


class Test(Model):
    __collection__ = "Test"

    day: str
    path: str = Field(repr=False)
    test_scenario: TestScenario
    test_data: TestData


async def a_get() -> List[Test]:
    engine = AIOEngine()
    records = await engine.find(Test)
    return records


def all_records() -> List[Test]:
    return asyncio.run(a_get())
