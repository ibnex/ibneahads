# exponential function power (x,y)

def power(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
    else:
        return x * power(x, y // 2) * power(x, y // 2)

# Test the function
base = float(input("Enter the base (x): "))
exponent = int(input("Enter the exponent (y): "))

result = power(base, exponent)
print("Result:", result)