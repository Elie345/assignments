from abc import ABC, abstractmethod


class Drone(ABC):

    def __init__(self):
        self.battery_level = 100  # initial battery level

    # Abstract method (must be implemented in subclasses)
    @abstractmethod
    def Maps(self, destination):
        pass

    # Concrete method (already implemented)
    def update_battery(self, consumption):
        self.battery_level -= consumption
        print(f"Battery updated: {self.battery_level}% remaining")