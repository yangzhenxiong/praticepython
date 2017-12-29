#!Versions/2.7/python2
'''
Ex 2:
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Extras:
If the number is a multiple of 4, print out a different message. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
num = int(input('Please input a number:'))
check = int(input('Please input a number to divide by:'))
mod = num%2
if(num%4==0):
    print('num:',num,' is a multiple of 4')
if(0==mod):
    print('num:',num,' is even')
else:
    print('num:',num,' is odd')
if(num%check==0):
    print('num:',num,' divides evenly by',check)
else:
    print('num:', num, ' does not divide evenly by',check)