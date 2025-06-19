from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(
        self, data: list[dict[str, str]], column: str, numeric: bool = False
    ) -> list[dict[str, str]]: ...


class AscStrategy(SortStrategy):
    def sort(
        self, data: list[dict[str, str]], column: str, numeric: bool = False
    ) -> list[dict[str, str]]:
        key_fn = (
            (lambda row: float(row[column]))
            if numeric
            else (lambda row: row[column])
        )
        return sorted(data, key=key_fn)


class DescStrategy(SortStrategy):
    def sort(
        self, data: list[dict[str, str]], column: str, numeric: bool = False
    ) -> list[dict[str, str]]:
        key_fn = (
            (lambda row: float(row[column]))
            if numeric
            else (lambda row: row[column])
        )
        return sorted(data, key=key_fn, reverse=True)
