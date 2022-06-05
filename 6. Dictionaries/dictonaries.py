"""
Given the dictionary: 
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

14. Add the 'colour' attribute to the car dictionary and declare it as 'red'
"""
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(car)

car.update({"colour": "red"})

print(car)
