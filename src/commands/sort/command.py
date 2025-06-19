from src.commands.sort.strategy import SortStrategy, AscStrategy, DescStrategy


def parse_sort_arg(arg: str) -> tuple[str, str]:
    try:
        column, sort_type = arg.split(":")
        return column.strip(), sort_type.strip()
    except ValueError:
        raise ValueError("Invalid sort format. Use 'column:type[asc, desc]'")


def is_numeric_column(data: list[dict[str, str]], column: str) -> bool:
    for row in data:
        try:
            float(row[column])
        except ValueError:
            return False
    return True


class SortCommand:
    def __init__(self, column: str, sort_type: str, numeric: bool = False):
        self.column = column
        self.numeric = numeric
        self.strategy = self._select_strategy(sort_type)

    def _select_strategy(self, sort_type: str) -> SortStrategy:
        strategies = {
            "asc": AscStrategy(),
            "desc": DescStrategy(),
        }
        if sort_type not in strategies:
            raise ValueError(f"Unknown sort type: {sort_type}")
        return strategies[sort_type]

    def execute(self, data: list[dict[str, str]]) -> list[dict[str, str]]:
        return self.strategy.sort(data, self.column, numeric=self.numeric)
