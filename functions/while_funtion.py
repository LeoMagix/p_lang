#Using Funtions With while Loops.
def get_formatted_name(first_name, last_name, middle_name=''):
    """Function to print a formatted name of the user."""
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    
    return full_name

#This a while loop:
respond = True
while respond:
    print("Please Enter Your Full Name:")
    #print("You can enter 'q' to quit.")
        
    first = input("\tFirst name: ")
    #if first == 'q':
        #break
    last = input("\tLast name: ")
    #if last == 'q':
        #break
    middle = input("\tMiddle name: ")
    #if middle == 'q':
        #break
            
    format_name = get_formatted_name(first, last, middle)
    print(f"Oshe!!, {format_name}.\n")
    
    ans = input("Is there anybody else (y/n)\n")
    
    if ans == 'n':
        respond = False
    
        print("Thanks for your participation. ^-")

