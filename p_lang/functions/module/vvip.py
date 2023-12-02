#FUNCTIONS TO CLEAR INVITED GUESTS USING A SECURITY CODE.
def list_guests(guests):
    """Prints the list of invited persons."""
    
    msg = "This is the list of invited persons."
    
    print(f'{msg.title()}')
    
    for invited in guests:
        print(f"\t{invited.title()}")
    
    print('\n')

def confirm_keys(guests, sent_keys):
    """
        Send guests their invitation for the event.
        Also sends them their keycodes for confirmation.
    """
    
    invite = guests[:]
    
    while invite:
        sent = invite.pop()
        
        if sent == 'usain bolt':
            print(f"{sent.title()}, You have an invite to diner at Precept Resorts, "
                    "Calaba at 8:30PM.")
            
            print(f"Your confirmation keycode required for entry is:\n\t'lighteningbolt9.58'")
            
            print()
       
        elif sent == 'zara hadid':
             print(f"{sent.title()}, You have an invite to diner at Precept Resorts, "
                    "Calaba at 8:30PM.")
             
             print(f"Your confirmation keycode required for entry is:\n\t'arch.queenofcurves'")
             
             print()
        
        elif sent == 'elon musk':
             print(f"{sent.title()}, You have an invite to diner at Precept Resorts, "
                    "Calaba at 8:30PM.")
             
             print(f"Your confirmation keycode required for entry is:\n\t'techking01'")
             
             print()
        
        elif sent == 'nikola tesla':
            print(f"{sent.title()}, You have an invite to diner at Precept Resorts, "
                    "Calaba at 8:30PM.")
            
            print(f"Your confirmation keycode required for entry is:\n\t'masteroflightening")
            
            print()
        
        elif sent == 'michael jordan':
            print(f"{sent.title()}, You have an invite to diner at Precept Resorts, "
                    "Calaba at 8:30PM.")
            
            print(f"Your confirmation keycode required for entry is:\n\t'airjordan23'")
            
            print()
        
        sent_keys.append(sent)
    
    print("\nThe following guests have received their keycodes-")
    
    for key in sorted(sent_keys):
        print(f"\t{key.upper()}")

def check_guest(invitee):
    """
    Security check to confirm if a person is on the guest list.
    Prompts user for a keycode, extra confirmation. 
    """
    
    name = input("\nPlease enter first and last name.\n")

    for guest in invitee:
        print(guest[name])
