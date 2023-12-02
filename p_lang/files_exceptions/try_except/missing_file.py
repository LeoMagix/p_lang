filename = 'programming.txt'
try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Can't locate {filename}.")
