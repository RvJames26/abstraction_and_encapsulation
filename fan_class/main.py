from fan_01 import FanOne
from fan_02 import FanTwo

bg_yellow = "\033[43m"
reset = "\033[0m"

my_fan = FanOne()
my_fan.set_fan_status(True)

my_fan_two = FanTwo()

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
