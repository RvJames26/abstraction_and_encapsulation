from pet import Pet

input_name = input("Enter your pet's name:")

while True:
    try:
        input_age = int(input("Enter pet's age:"))
        break
    except ValueError:
        print(f"Age should be a number")
    else:
        continue

input_animal_type = input("Enter pet's animal type:")

my_pet = Pet(input_name, input_animal_type, input_age)

my_pet.get_name()
my_pet.get_age()
my_pet.get_animal_type()

print(f"Your pet is {my_pet.get_name()}")
print(f"Your pet is {my_pet.get_age()} years old")
print(f"Your pet is {my_pet.get_animal_type()} type")
