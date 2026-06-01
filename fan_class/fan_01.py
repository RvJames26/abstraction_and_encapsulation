class FanOne:
    slow = 1
    medium = 2
    fast = 3

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

curent_status = my_fan.get_fan_status()
if curent_status == True:
    print("Fan status: On")
elif curent_status == False:
    print("Fan status: Off")

current_speed = my_fan.get_fan_speed()
if current_speed == 1:
    print(f"Fan speed: SLOW")
elif current_speed == 2:
    print(f"Fan speed: MEDIUM")
elif current_speed == 3:
    print(f"Fan speed: FAST")

print(f"Fan radius: {my_fan.get_fan_radius()}")
print(f"Fan color: {my_fan.get_fan_color()}")

