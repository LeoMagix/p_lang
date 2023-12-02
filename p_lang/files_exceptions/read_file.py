#learning_python.txt.replace('Python', 'C')
file = 'learning_python.txt'

with open(file) as text:
    txt_file = text.read()
    print(txt_file.rstrip())
    print()

with open(file) as texts:
    for text in texts:
        met = text.rstrip()
        print(met.replace('Python', 'C'))

with open(file) as texts:
    txt_file = texts.readlines()
    print()

for text in txt_file:
    print(text.strip())
    replace = text.replace('Python', 'C')
    print(replace)
