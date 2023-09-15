# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a = name1.lower()
b = name2.lower()
c = a + b

t = c.count("t")
r = c.count("r")
u = c.count("u")
e = c.count("e")

true = t+r+u+e

l= c.count("l")
o = c.count("o")
v = c.count("v")
e = c.count("e")

love = l+o+v+e

true_love = int(str(true)+str(love))

if (true_love<10) or (true_love>90):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >=40 and true_love<=50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")
