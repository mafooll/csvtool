from argparse import Namespace
from src.core.build import CommandBuilder


def test_builder_all():
    args = Namespace(
        filter="price>10",
        sort="price:desc",
        aggregate="price:max",
        filepath="fake.csv",
    )
    data = [{"price": "data"}]
    filter_cmd, sort_cmd, agg_cmd = CommandBuilder(args).build(data)

    assert filter_cmd is not None
    assert sort_cmd is not None
    assert agg_cmd is not None
