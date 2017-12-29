'''
Ex 6:
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

a=input('Please input a String:')
a=str(a)
rvr = a[::-1]
if a==rvr:
    print(a + " is a palindrome")
else:
    print(a + " is not a palindrome")
