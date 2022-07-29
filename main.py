from time import perf_counter
from typing import Any, Callable, List

import pymongo_bench
import mongoframes_bench
import beanie_bench
import odmantic_bench
import mongoengine_bench
import umongo_bench
import thingy_bench

# import minimongo_bench


def bench(func: Callable[[], Any], name: str) -> List[Any]:
    print(f"Testing: {name}".center(70, "-"))
    s = perf_counter()
    records = func()
    print(f"Records: {len(records)}")
    print(f"Time: {perf_counter() - s}s")
    return records


bench(pymongo_bench.all_records, "PyMongo")
bench(mongoframes_bench.all_records, "MongoFrames")
bench(beanie_bench.all_records, "Beanie")
bench(odmantic_bench.all_records, "Odmantic")
bench(mongoengine_bench.all_records, "MongoEngine")
bench(umongo_bench.all_records, "uMongo")
bench(thingy_bench.all_records, "Mongo-Thingy")
# bench(minimongo_bench.all_records, "MiniMongo")
