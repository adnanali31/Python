import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

payer = random.choice(names)
print(f"{payer} is going to buy the meal today!")
