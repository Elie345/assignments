from abc import ABC, abstractmethod
import json

# =========================
# BASE CLASS (MUST COME FIRST)
# =========================
class Drone(ABC):

    def __init__(self):
        self._internal_temperature = 25
        self.__battery_level = 100

    @abstractmethod
    def Maps(self, destination):
        pass

    def update_battery(self, consumption):
        self.__battery_level -= consumption
        print(f"Battery updated: {self.__battery_level}% remaining")

    @property
    def battery_level(self):
        return self.__battery_level


# =========================
# SUBCLASS
# =========================
class DeliveryDrone(Drone):

    def __init__(self):
        super().__init__()
        self.sensors = []

    def Maps(self, destination):
        print(f"Navigating to {destination}")

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def serialize(self, filename):
        data = {
            "temperature": self._internal_temperature,
            "battery": self.battery_level,
            "sensors": [sensor.name for sensor in self.sensors]
        }

        with open(filename, "w") as file:
            json.dump(data, file)

        print("Drone state saved.")

    @classmethod
    def reboot(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)

        drone = cls()
        drone._internal_temperature = data["temperature"]
        drone._Drone__battery_level = data["battery"]

        print("Drone rebooted.")
        return drone


# =========================
# SENSOR CLASSES
# =========================
class Lidar:
    name = "Lidar"

class GPS:
    name = "GPS"


# =========================
# TEST CODE
# =========================
if __name__ == "__main__":
    drone = DeliveryDrone()

    drone.add_sensor(Lidar())
    drone.add_sensor(GPS())

    drone.Maps("Harare")
    drone.update_battery(20)

    drone.serialize("drone.json")

    new_drone = DeliveryDrone.reboot("drone.json")
    print("Restored Battery:", new_drone.battery_level)