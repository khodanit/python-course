"""
Given the set: fruits = {"apple", "banana", "cherry"}

16. Add more_fruits = ["orange", "mango", "grapes"] to the 'fruits' set
17. Use two different methods to remove 2 different fruit items from the set
"""

fruits = {"apple", "banana", "cherry"}
print(fruits)

more_fruits = ["orange", "mango", "grapes"]

fruits.update(more_fruits)
print(fruits)
