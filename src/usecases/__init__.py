# I have no time to create real model, so I've create just model stub
import abc


class Model(abc.ABC):
    @abc.abstractmethod
    def answer(self, question: str) -> str:
        pass
