from abc import ABC, abstractmethod
from typing import Sequence


class AggregateStrategy(ABC):
    @abstractmethod
    def apply(self, values: Sequence[float]) -> float:
        pass


class MaxStrategy(AggregateStrategy):
    def apply(self, values: Sequence[float]) -> float:
        return max(values)


class MinStrategy(AggregateStrategy):
    def apply(self, values: Sequence[float]) -> float:
        return min(values)


class AvgStrategy(AggregateStrategy):
    def apply(self, values: Sequence[float]) -> float:
        return sum(values) / len(values) if values else 0.0
