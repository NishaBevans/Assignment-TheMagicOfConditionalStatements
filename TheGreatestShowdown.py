#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)


#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

if (num1 <= num2) and (num1 <= num3):
   smallest = num1
elif (num2 <= num1) and (num2 <= num3):
   smallest = num3

print("The smallest number is", smallest)