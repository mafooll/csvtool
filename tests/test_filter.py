from src.commands.filter.command import FilterCommand


def test_simple_filter_eq():
    data = [{"name": "Alice"}, {"name": "Bob"}]
    cmd = FilterCommand("name=Alice")
    result = cmd.execute(data)
    assert result == [{"name": "Alice"}]


def test_filter_gt_and_eq():
    data = [
        {"price": "10", "stock": "yes"},
        {"price": "20", "stock": "no"},
        {"price": "30", "stock": "yes"},
    ]
    cmd = FilterCommand("price>10 AND stock=yes")
    result = cmd.execute(data)
    assert result == [{"price": "30", "stock": "yes"}]


def test_filter_or():
    data = [{"x": "1"}, {"x": "2"}, {"x": "3"}]
    cmd = FilterCommand("x=1 OR x=3")
    result = cmd.execute(data)
    assert result == [{"x": "1"}, {"x": "3"}]
