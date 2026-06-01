from asyncio import base_futures

bg_yellow = "\033[43m"
reset = "\033[0m"

class FanOne:
    slow = 1
    medium = 2
    fast = 3
    bg_yellow = "\033[43m"
    reset = "\033[0m"

    def __init__(self, fan_speed=1, fan_status=False, fan_radius=5, fan_color="yellow"):
        self.__fan_speed = fan_speed
        self.__fan_status = fan_status
        self.__fan_radius = fan_radius
        self.__fan_color = fan_color

    def get_fan_speed(self):
        return self.__fan_speed

    def set_fan_speed(self, fan_speed):
        self.__fan_speed = fan_speed

    def get_fan_status(self):
        return self.__fan_status

    def set_fan_status(self, fan_status):
        self.__fan_status = fan_status

    def get_fan_radius(self):
        return self.__fan_radius

    def set_fan_radius(self, fan_radius):
        self.__fan_radius = fan_radius

    def get_fan_color(self):
        return self.__fan_color

    def set_fan_color(self, fan_color):
        self.__fan_color = fan_color

my_fan = FanOne()
my_fan.set_fan_status(True)

print(f"{bg_yellow}Fan One{reset}")
curent_status = my_fan.get_fan_status()
if curent_status == True:
    print(f"{bg_yellow}Fan status: On{reset}")
elif curent_status == False:
    print(f"{bg_yellow}Fan status: Off{reset}")

current_speed = my_fan.get_fan_speed()
if current_speed == 1:
    print(f"{bg_yellow}Fan speed: SLOW{reset}")
elif current_speed == 2:
    print(f"{bg_yellow}Fan speed: MEDIUM{reset}")
elif current_speed == 3:
    print(f"{bg_yellow}Fan speed: FAST{reset}")

print(f"{bg_yellow}Fan radius: {my_fan.get_fan_radius()}{reset}")
print(f"{bg_yellow}Fan color: {my_fan.get_fan_color()}{reset}")

