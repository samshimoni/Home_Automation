from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def is_alive(self):
        raise NotImplementedError
