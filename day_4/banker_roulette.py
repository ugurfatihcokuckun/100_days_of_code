import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

a = random.randint(0, len(names) - 1)

print(f"{names[a]} is going to buy the meal today!")