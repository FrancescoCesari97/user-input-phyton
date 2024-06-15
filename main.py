

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# # age = int(age)
# age = age + 1
#
# print(f"Hello {name}")
# print(f"You are {age } years old")

# mad libs game

# adjective1 = input("Enter an adjective:  ")
# adjective2 = input("Enter an adjective:  ")
# adjective3 = input("Enter an adjective:  ")
# noun = input("enter an noun: ")
# verb = input("enter an verb: ")
#
# print(f"Today I went to a {adjective1} zoo.")
# print(f"in an exhibit, I saw {noun}")
# print(f"{noun} was {adjective2} and {verb}ing")
# print(f"I was {adjective3}")


# Area calc rectangle

# length = float(input("Enter the length of a rectangle: "))
#
# width = float(input("Enter the width of a rectangle: "))
#
# height = float(input("Enter the height of a rectangle: "))
#
# volume = length * width * height
#
# print(f"the area is: {volume} cm^3")


# shopping cart program

item = input(" what item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"your total price for your order of {item} is {round(total, 2)} $")
