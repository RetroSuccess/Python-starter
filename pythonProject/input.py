# input() = A function that prompts the user to enter data
#           Returns the entered data as string

name = input("What is your name: ")
age = int(input("How old are you?: "))

age = age + 1

print(f"Hello {name}")
print("Happy Birthday!!")
print(f"You are {age}")
print("")

# Exercise 1 Rectangle Area Calc
print("Below is a exercise to find out the area of a triangle with length of 6.5 and a width of 3.2")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area is {area}cm²")
print("")

# Exercise 2 Shopping Cart Program
print("Below calculate the total amount Sam paid if he bought 5 pizza's and one pizza costs 30.00")
item = input("What item would you like to buy?: ")
price = float(input("What is the price of the item?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"Your total is R{total}")