class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, fan_speed, fan_status=False):
        self.fan_speed = fan_speed
        self.fan_status = fan_status
