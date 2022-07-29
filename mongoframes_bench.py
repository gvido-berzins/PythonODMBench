from mongoframes import Q, Frame, In, SubFrame, NotIn, And, Or
from pymongo import MongoClient

from settings import DATABASE_URL

# Connect MongoFrames to the database

MONGOFRAME = Frame._client = MongoClient(DATABASE_URL)


class TestScenario(SubFrame):
    _field = {
        "call_type",
        "app",
        "platform",
        "participants",
        "condition",
    }


class TestData(SubFrame):
    _field = {
        "test_id",
        "path",
        "datetime",
        "metric",
        "data",
        "time",
    }


class Test(Frame):
    _fields = {
        "day",
        "path",
        "test_scenario",
        "test_data",
    }


def all_records():
    res = Test.many()
    return res
