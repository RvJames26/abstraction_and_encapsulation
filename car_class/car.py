class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def get_speed(self):
        return self.__speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

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