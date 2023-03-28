def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

num = int(input("Enter a number: "))
print("The factorial of", num, "is", factorial(num))
