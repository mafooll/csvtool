from abc import ABC, abstractmethod

from src.core.base.strategy import BaseStrategy


class BaseFilterStrategy(ABC):
    @abstractmethod
    def apply(
        self, data: list[dict[str, str]], column: str, value: str
    ) -> list[dict[str, str]]:
        pass


class EqStrategy(BaseFilterStrategy):
    def apply(self, data, column, value):
        return [row for row in data if row[column] == value]


class GtStrategy(BaseFilterStrategy):
    def apply(self, data, column, value):
        return [row for row in data if float(row[column]) > float(value)]


class LtStrategy(BaseFilterStrategy):
    def apply(self, data, column, value):
        return [row for row in data if float(row[column]) < float(value)]


class LogicStrategy(BaseStrategy):
    def __init__(self, op: str, children: list[BaseStrategy]):
        self.op = op.lower()
        self.children = children

    def apply(self, data: list[dict[str, str]]) -> list[dict[str, str]]:
        if self.op == "and":
            result = data
            for child in self.children:
                result = child.apply(result)
            return result
        elif self.op == "or":
            sets = [set(map(id, child.apply(data))) for child in self.children]
            combined_ids = set().union(*sets)
            return [row for row in data if id(row) in combined_ids]
        else:
            raise ValueError(f"Unknown logic operator {self.op}")


class ComparisonStrategy(BaseStrategy):
    def __init__(self, column: str, op: str, value: str):
        self.column = column
        self.value = value
        self.strategy = self._select_strategy(op)

    def _select_strategy(self, op: str) -> BaseFilterStrategy:
        strategies = {
            "=": EqStrategy(),
            ">": GtStrategy(),
            "<": LtStrategy(),
        }
        if op not in strategies:
            raise ValueError(f"Unsupported filter operation '{op}'")
        return strategies[op]

    def apply(self, data: list[dict[str, str]]) -> list[dict[str, str]]:
        return self.strategy.apply(data, self.column, self.value)
