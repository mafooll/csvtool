from src.commands.aggregate.strategy import (
    MaxStrategy,
    MinStrategy,
    AvgStrategy,
)


def parse_aggregate_arg(arg: str) -> tuple[str, str]:
    try:
        column, agg_type = arg.split(":")
        return column.strip(), agg_type.strip()
    except ValueError:
        raise ValueError("Invalid format. Use 'column:aggregate_type'")


class AggregateCommand:
    def __init__(self, column: str, agg_type: str):
        self.column = column
        self.strategy = self._select_strategy(agg_type)

    def _select_strategy(self, agg_type: str):
        strategies = {
            "max": MaxStrategy(),
            "min": MinStrategy(),
            "avg": AvgStrategy(),
        }
        if agg_type not in strategies:
            raise ValueError(f"Unknown aggregation: {agg_type}")
        return strategies[agg_type]

    def execute(self, data: list[dict[str, str]]) -> float:
        values = [float(row[self.column]) for row in data if row[self.column]]
        return self.strategy.apply(values)
