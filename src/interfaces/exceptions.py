from abc import ABC, abstractmethod


class AppException(Exception, ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass
