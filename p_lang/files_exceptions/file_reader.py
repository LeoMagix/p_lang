#Learning to how to open() and read() a file with Python.
file = 'pi_digits.txt'

with open(file) as file_object:
    contents = file_object.read()
    print(contents)

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file) as file_object:
    lines = file_object.readlines()
    #print(lines)
for line in lines:
    print(line)

with open(file) as fo:
    lines = fo.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
