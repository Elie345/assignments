# Define the Dog class
class Dog:
    def make_sound(self):
        print("Woof! Woof!")  # Dog-specific sound

# Define the Cat class
class Cat:
    def make_sound(self):
        print("Meow! Meow!")  # Cat-specific sound

# Function that works with any object that has make_sound()
def process_sound(sound_object):
    sound_object.make_sound()  # Call the method without knowing the type

# Create instances
my_dog = Dog()
my_cat = Cat()

# Call process_sound with different objects
process_sound(my_dog)  # Expected output: Woof! Woof!
process_sound(my_cat)  # Expected output: Meow! Meow!
