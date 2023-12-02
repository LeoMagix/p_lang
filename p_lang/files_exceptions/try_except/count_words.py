def count_words(filename):
    """Count the approximate numberb of words in a file."""
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        #failing in silence
        pass
        #print(f"{filename} Can't be located.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"{filename} has {num_words} words.")
#filename = 'learning_python.txt'
#count_words(filename)
filenames = ['guest_book.txt', 'learning_python.txt', 'alice.txt', 'programming_python.txt']
filenames += ['programming_poll.txt']
for filename in filenames:
    count_words(filename)
