class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, fan_speed, fan_status=False):
        self.__fan_speed = fan_speed
        self.__fan_status = fan_status

    def get_fan_speed(self):
        return self.__fan_speed

    def get_fan_speed(self, fan_speed):
        self.__fan_speed = fan_speed

    def get_fan_status(self):
        return self.__fan_status

    def set_fan_status(self, fan_status):

