#Writing to a file in Python.
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love to write programs.\n")

with open(filename, 'a') as file_object:
    file_object.write('You still de here')

with open('READ.md', 'w') as file:
    file.write("Exploring files and exceptions\n")
