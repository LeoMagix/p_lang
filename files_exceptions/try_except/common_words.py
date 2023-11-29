#Program to count the most commonly used words in our document."
with open('programming_poll.txt') as f:
    read = f.read()
    count =  read.count('I ')
    print(count)
