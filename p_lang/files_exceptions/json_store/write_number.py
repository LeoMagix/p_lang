#Learning to store data in python using json.dump()
import json

numbers = [23, 34, 24, 34]
filename = 'numbers.json'

with open(filename, 'w') as fo:
    json.dump(numbers, fo)
