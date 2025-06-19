from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    @abstractmethod
    def apply(self, *args, **kwargs): ...
