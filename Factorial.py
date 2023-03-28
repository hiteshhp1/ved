# The program takes an input number num and calculates its factorial using a recursive function factorial(n). The function factorial(n) takes an integer n as input and returns n! (the factorial of n). The function returns 1 if n is 0, otherwise it returns n multiplied by factorial(n-1), which calculates the factorial of n-1. This process continues until the factorial of 0 is reached, and the results are multiplied together to get the final answer.

# The program calculates the factorial of a number, which is a special mathematical calculation that tells us how many ways we can arrange a certain number of things. For example, the factorial of 5 (written as 5!) is equal to 5 x 4 x 3 x 2 x 1, which is 120.

# The way the program works is by using a function called factorial(n). This function takes a number n and returns its factorial. The function works by calling itself repeatedly, each time with a smaller number, until it reaches the number 0.

# When the function is called with the number 0, it returns the number 1, because 0! is equal to 1. When the function is called with any other number, it calculates the factorial of n-1 by calling factorial(n-1), and then multiplies the result by n to get the final answer.

# So, for example, if you call factorial(5), the function will first call itself with the number 4 (factorial(4)), then with the number 3 (factorial(3)), and so on, until it reaches 0 and returns 1. The function then uses the results of these calls to calculate the final answer of 5!.

# The program then asks the user to enter a number, and prints the factorial of that number by calling the factorial(n) function with the entered number as the input.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print("The factorial of", num, "is", factorial(num))
