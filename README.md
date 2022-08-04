## Table
- [MongoFrames](https://mongoframes.com/)
	- [MongoFrames vs. MongoEngine](https://mongoframes.com/snippets/mongoframes-vs-mongoengine)
- [Beanie](https://roman-right.github.io/beanie/) - Using this right now
- [odmantic](https://github.com/art049/odmantic)
- [MongoEngine](http://mongoengine.org/)
- [μMongo](https://umongo.readthedocs.io/en/latest/index.html)
- [Mongo-Thingy](https://github.com/Refty/mongo-thingy)

Test conditions:
- Testing with 1000 documents
- get all records

## Results
### PyMongo
~0.06s

- ***Blazingly fast***
- More effort to transition

#### PyMongo + Pydantic loading
~0.80s

- 10x decrease :(
- Speed, same as Beanie

```python
from typing import List

from pydantic import BaseModel, parse_obj_as
import pymongo

from settings import DATABASE_URL


class TestScenario(BaseModel):
    call_type: str
    app: str
    platform: str
    participants: str
    condition: str


class TestData(BaseModel):
    test_id: str
    datetime: str
    metric: str
    path: str
    data: List[float]
    time: List[float]


class Test(BaseModel):
    day: str
    path: str
    test_scenario: TestScenario
    test_data: TestData


def all_records():
    client = pymongo.MongoClient(DATABASE_URL)
    records = client.test.Test.find()
    tests = parse_obj_as(List[Test], list(records))

    return tests

```

#### PyMongo + cattrs loading
~0.14s

- A lot better than using Pydantic
- Easy to convert
```python
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


def all_records():
    client = pymongo.MongoClient(DATABASE_URL)
    records = client.test.Test.find()
    tests = structure(records, List[Test])
    return tests

```

### MongoFrames
~0.067s

- ***Blazingly fast***
- More effort to transition

## Odmantic
~0.88s

- Very similar speed as with Beanie
- Easy transition from Beanie

## MongoEngine
~0.44s

- About 2x faster than Odmantic and Beanie
- Easy transition from Beanie

## μMongo
~0.31s

- A bit faster than MongoEngine
- Transition is not hard

## Mongo-Thingy
~1.20s

- Easy to use
- No schema
- Slow :(

## Resources
- [pymongo - Tools](https://pymongo.readthedocs.io/en/stable/tools.html)
- [awesome-mongodb - Python](https://project-awesome.org/ramnes/awesome-mongodb#python)
