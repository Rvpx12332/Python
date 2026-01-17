num1 = int(input("Please enter a number you want to be divided:"))
num2 = int(input("Enter another number to check your previous number can be divided by:"))

result = num1%num2

if result == 0:
    print("It is divisible.")
else:
    print("It is not divisible.")    