from abc import ABC, abstractmethod

class BaseProvider(ABC):

    @abstractmethod
    def load(self):
        pass

    def get_laps(self):
        pass

    def get_drivers(self):
        pass

    def get_weather(self):
        pass

    def get_Gap(self):
        pass