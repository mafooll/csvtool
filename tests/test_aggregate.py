from src.commands.aggregate.command import AggregateCommand


def test_aggregate_max():
    data = [{"price": "10"}, {"price": "20"}, {"price": "15"}]
    cmd = AggregateCommand("price", "max")
    assert cmd.execute(data) == 20.0


def test_aggregate_min():
    data = [{"price": "5"}, {"price": "1"}, {"price": "10"}]
    cmd = AggregateCommand("price", "min")
    assert cmd.execute(data) == 1.0


def test_aggregate_avg():
    data = [{"price": "10"}, {"price": "20"}, {"price": "30"}]
    cmd = AggregateCommand("price", "avg")
    assert cmd.execute(data) == 20.0
