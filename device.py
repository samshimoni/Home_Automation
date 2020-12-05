from abc import ABC, abstractmethod
import logger
import cfg_automation


class Device(ABC):
    @abstractmethod
    def is_alive(self):
        raise NotImplementedError

    def __init__(self, service_name):
        self.service_name = service_name
        self.logger = logger.Logger(service_name).logger
        self.cfg = cfg_automation.Cfg
