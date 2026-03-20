from abc import ABC, abstractmethod

# FIRST: Base class
class Drone(ABC):

    def __init__(self):
        self._internal_temperature = 25
        self.__battery_level = 100

    @abstractmethod
    def Maps(self, destination):
        pass

    def update_battery(self, consumption):
        self.__battery_level -= consumption

    @property
    def battery_level(self):
        return self.__battery_level


# SECOND: Subclass
class DeliveryDrone(Drone):

    def __init__(self):
        super().__init__()
        self.sensors = []

    def Maps(self, destination):
        print(f"Navigating to {destination}")

    def add_sensor(self, sensor):
        self.sensors.append(sensor)