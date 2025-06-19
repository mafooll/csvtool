from src.commands.sort.command import SortCommand


def test_sort_asc_numeric():
    data = [{"x": "2"}, {"x": "1"}, {"x": "3"}]
    cmd = SortCommand("x", "asc", numeric=True)
    result = cmd.execute(data)
    assert [row["x"] for row in result] == ["1", "2", "3"]


def test_sort_desc_numeric():
    data = [{"x": "2"}, {"x": "1"}, {"x": "3"}]
    cmd = SortCommand("x", "desc", numeric=True)
    result = cmd.execute(data)
    assert [row["x"] for row in result] == ["3", "2", "1"]


def test_sort_asc_string():
    data = [{"name": "Charlie"}, {"name": "Alice"}, {"name": "Bob"}]
    cmd = SortCommand("name", "asc")
    result = cmd.execute(data)
    assert [row["name"] for row in result] == ["Alice", "Bob", "Charlie"]
