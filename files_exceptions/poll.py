que = "Why do you love programming?"

while True:
    print(que)
    reason = input()
    print()
    
    if reason == 'q':
        break

    with open('programming_poll.txt', 'a') as poll:
        poll.write(f'{reason}\n')
