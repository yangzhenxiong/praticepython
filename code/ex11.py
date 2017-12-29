#coding=utf-8
'''
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!)
use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

Discussion

Concepts for this week:

Functions
Reusable functions
Default arguments
'''
def get_number(prompt):
    return int(input(prompt))

def is_prime(number):
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    else:
        prime = True
        for check_number in range(2, (number/2)+1):
            if number % check_number == 0:
                prime=False
                break
    return prime

def print_prime(number):
    prime = is_prime(number)
    if prime:
        descriptor = " "
    else:
        descriptor ="not "
    print(number," is ", descriptor,"prime.")

print_prime(get_number("Enter a number to check."))