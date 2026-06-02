from car import Car

my_car = Car(2003, "Porsche 911 GT3 RS")

print(f"""
Make: {my_car.get_make()}
Year: {my_car.get_year_model()}""")

print("Accelerating")
for i in range(5):
    my_car.accelerate()
    print(f"Car Speed: {my_car.get_speed()}")

for i in range(5):
    my_car.brake()
    print(f"Car speed: {my_car.get_speed()}")
