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

# Call collatz until its return value is equal to one(1).
# Refactoring the code that handles the user's input and collatz() function call.
# We are putting the code that prompts user for a number into the function call_collatz().

def call_collatz():
    """
    This function requests User to enter an integer; value entered must be a number.
    Employ a Try-Except block to catch all errorneous or malicious inputs.
    Return the computed collatz number to the User.
    """
    # Ask User to enter a number
    try:
        # Checks if User entered a number 
        # If they have, then convert it to an integer
        int_num = int(input("Please Enter A Number:\n"))

    # Print a warning if the value is anything but a number
    except ValueError:
        print("Wrong value.\nEnter an Integer")

    # Main code that utilizes the collatz() function
    else:
        while True:
            collatz_num = collatz(int_num)
    
            if collatz_num == 1:
                return collatz_num
                #break
    
            else:
                print(f"COLLATZ NUMBER=={collatz_num}")
                int_num = collatz_num   #Sets int_num to new value

ret_num = call_collatz()
if ret_num != None:
    print(f"COLLATZ NUMBER--{ret_num}")
#print(ret_num)
