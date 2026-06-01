class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, fan_speed=1, fan_status=False):
        self.__fan_speed = fan_speed
        self.__fan_status = fan_status

    def get_fan_speed(self):
        return self.__fan_speed

    def set_fan_speed(self, fan_speed):
        self.__fan_speed = fan_speed

    def get_fan_status(self):
        return self.__fan_status

    def set_fan_status(self, fan_status):
        self.__fan_status = fan_status

my_fan = Fan()

my_fan.set_fan_status(True)

print(my_fan.get_fan_speed())
print(my_fan.get_fan_status())
