#Sampling try-except blocks.
print("Provide me two numbers, i'll divide them.")
print("Enter 'q' to quit.\n")

while True:
    first_no = input("\nFirst number: ")
    if first_no == 'q':
        break
    second_no = input("\nSecond number: ")
    if second_no == 'q':
        break
    try:
        ans = int(first_no) / int(second_no)
    except ZeroDivisionError:
        print("It's not possible to divide a number 0. Dumbass!")
    else:
        print(ans)
