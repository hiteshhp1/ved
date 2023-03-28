""" In this program, the times_table(n) function takes an integer n as input and prints its times table using a for loop. 
The loop iterates from 1 to 10 and calculates the product of n and i (the current iteration number), and prints the result 
in the desired format. The program then takes an input number num and calls the times_table(num) function, which prints 
the times table of number """


def times_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

num = int(input("Enter a number to generate its times table: "))
times_table(num) 




    
