import fastf1
from providers.base_provider import BaseProvider


class LiveProvider(BaseProvider):
    def __init__(self, year, circuit, session_type):
        self.year = year
        self.circuit = circuit
        self.session_type = session_type
        self.session = None

    def load(self):
        self.session = fastf1.get_session(self.year, self.circuit, self.session_type)
        self.session.load()

    def get_laps(self):
        return self.session.laps
    
    def get_drivers(self):
        return self.session.drivers
    
    def get_weather(self):
        return None
    
    def get_Positions(self):
        return self.session._pos_data
    
    def get_Gap(self):
        pass
    