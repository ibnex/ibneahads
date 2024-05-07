# GCD of two integers


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

# Test the function
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if num1 < 0 or num2 < 0:
    print("Please enter positive integers.")
else:
    result = gcd(num1, num2)
    print("The GCD of", num1, "and", num2, "is:", result)