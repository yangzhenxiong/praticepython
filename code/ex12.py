#coding=utf-8
'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and
last elements of the given list. For practice, write this code inside a function.

Concepts to practice

Lists and properties of lists
List comprehensions (maybe)
Functions
'''
a = [5, 10, 15, 20, 25]
b=[a[0],a[len(a)-1]]
print(b)