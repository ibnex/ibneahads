def sum_of_natural_numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_of_natural_numbers(n - 1)

# Test the function
num = int(input("Enter a positive integer: "))
if num < 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_natural_numbers(num)
    print("The sum of natural numbers up to", num, "is:", result)