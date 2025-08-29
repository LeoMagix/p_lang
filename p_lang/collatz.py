def collatz(number):
    """
    If the number is even divide by 2.
    if number is odd; multiply by 3 and add 1
    """
    if number == 0:
        return 1
    
    if number % 2 == 0:
        return number // 2

    else:
        return 3 * number + 1

#Write a code that keeps calling collatz until its return value is equal to one(1).
try:
    #We ask the user for the integer number
    num = int(input("Please Enter A Number:\n"))

except ValueError:
    print("Enter an Integer")

else:
    while True:
        collatz_num = collatz(num)
    
        if collatz_num == 1:
            print(collatz_num)
            break
    
        else:
             print(collatz_num)
             num = collatz_num
         
