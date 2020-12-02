from abc import ABC, abstractmethod
import Logger


class Device(ABC):
    @abstractmethod
    def is_alive(self):
        raise NotImplementedError

    def __init__(self, service_name):
        self.service_name = service_name
        self.logger = Logger.Logger(service_name).logger
