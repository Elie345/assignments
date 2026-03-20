# Base class
class SmartDevice:
    def __init__(self, name):
        self.name = name

    def reset(self):
        print(f"{self.name} (SmartDevice) is resetting to factory settings...")

# Subclass
class SmartLight(SmartDevice):
    def reset(self):
        print(f"{self.name} (SmartLight) is resetting brightness and color settings...")

# Polymorphic function
def reset_all_devices(devices_list):
    for device in devices_list:
        device.reset()  # Calls the correct .reset() based on object type

# Example usage
device1 = SmartDevice("Thermostat")
device2 = SmartLight("Living Room Light")
device3 = SmartLight("Bedroom Light")

all_devices = [device1, device2, device3]

reset_all_devices(all_devices)