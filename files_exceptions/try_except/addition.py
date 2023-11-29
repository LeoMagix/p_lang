#Tackling ValueError in your programs.
print("Provide two numbers to get their sum.")
print("Enter 'q' to quit the program.\n")

while True:
    first_num = input('First number:\n')
    if first_num == 'q':
        break
    
    second_num = input('Second number:\n')
    if second_num == 'q':
        break
    
    try:
        answer =int(first_num) + int(second_num)
    except ValueError:
        print("You have entered text(s) instead of number(s).\n")
    else:
        print(f"The answer is \n{answer}")
