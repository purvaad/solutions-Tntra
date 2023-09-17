#Swap two numbers without using a temporary variable

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("Before swapping: ")
print("Value of first number : ", n1, " and second number : ", n2)

n1 = n1+n2
n2 = n1-n2
n1 = n1-n2

print("After swapping: ")
print("Value of first number : ", n1, " and second number : ", n2)
