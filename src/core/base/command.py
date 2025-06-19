from abc import ABC, abstractmethod

DataRow = dict[str, str]
DataTable = list[DataRow]
Result = DataTable | float | int


class BaseCommand(ABC):
    @abstractmethod
    def execute(self, data: DataTable) -> Result: ...
