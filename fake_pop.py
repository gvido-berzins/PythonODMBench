from mongoframes.factory import Factory, quotas
from mongoframes.factory.blueprints import Blueprint
from mongoframes.factory.makers import ListOf, SubFactory, dates as date_makers
from mongoframes.factory.makers import numbers as number_makers
from mongoframes.factory.makers import text as text_makers
from mongoframes.factory.makers import Faker
from mongoframes import Frame, SubFrame

from mongoframes_bench import MONGOFRAME, Test, TestData, TestScenario
from settings import DATABASE_URL


class TestScenarioBlueprint(Blueprint):
    _frame_cls = TestScenario
    call_type = text_makers.Sequence("call_type-{index}", start_from=1)
    app = text_makers.Sequence("app-{index}", start_from=1)
    platform = text_makers.Sequence("platform-{index}", start_from=1)
    participants = text_makers.Sequence("participants-{index}", start_from=1)
    condition = text_makers.Sequence("condition-{index}", start_from=1)


class TestDataBlueprint(Blueprint):
    _frame_cls = TestData
    test_id = text_makers.Join([text_makers.Code(5), text_makers.Code(5)], sep="-")
    path = Faker("file_path")
    datetime = text_makers.Join([Faker("date"), Faker("time")], sep="-")
    metric = text_makers.Sequence("metric-{index}", start_from=1)
    data = ListOf(number_makers.Float(0, 600), 300)
    time = ListOf(number_makers.Float(0, 600), 300)


class TestBlueprint(Blueprint):
    _frame_cls = Test

    day = Faker("date")
    path = Faker("file_path")
    test_scenario = SubFactory(TestScenarioBlueprint)
    test_data = SubFactory(TestDataBlueprint)


def populate_fakes():
    print("Populating fake data")
    factory = Factory()
    docs = factory.assemble(TestBlueprint, quotas.Quota(760))
    tests = factory.populate(TestBlueprint, docs)
    print("Done")
