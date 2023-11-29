file = '/home/leocoder_magic/p_lang/files_exceptions/programming_poll.txt'

try:
    with open(file) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, file {file} not found.")
else:
    #Count the approximate number of words in file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {file} has {num_words} words.")
