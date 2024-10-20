from random import choice

num1 = float(input("Enter the first number here: "))
num2 = float(input("Enter the second number here: "))
print("\n Press 1 for addition \n Press 2 for subtraction \n Press 3 for multiplication \n Press 4 for division \n ")

choice =int(input("Enter your choice from 1-4: "))

if choice == 1:
    print("The sum of the given two numbers is: ", num1 + num2)
elif choice == 2:
    print("The difference of the given two numbers is: ", num1 - num2)
elif choice == 3:
    print("The product of the given two numbers is: ", num1 * num2)
elif choice == 4:
    print("The quotient of the given two numbers is: ", num1 / num2)
else:
    print("Input is Invalid.")
