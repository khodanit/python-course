"""
Given the set: fruits = {"apple", "banana", "cherry"}

16. Add the more_fruits = ["orange", "mango", "grapes"] to the 'fruits' set
17. Use two different methods to remove 2 different fruit items from the set
"""

fruits = {"apple", "banana", "cherry"}
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.discard("cherry")
print(fruits)
