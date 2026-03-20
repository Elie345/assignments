from abc import ABC, abstractmethod

class Drone(ABC):

    def __init__(self):
        self._internal_temperature = 25   # protected attribute
        self.__battery_level = 100        # private attribute

    # Abstract method
    @abstractmethod
    def Maps(self, destination):
        pass

    # Concrete method
    def update_battery(self, consumption):
        self.__battery_level -= consumption
        print(f"Battery updated: {self.__battery_level}% remaining")

    # Property (read-only access)
    @property
    def battery_level(self):
        return self.__battery_level