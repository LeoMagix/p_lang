#Function to manage invites to a party.
def invite(invitees, sent_invites):
    """
    This prints a list of invited guests.
    Then sends an invite to invited persons.
    """
    
    header = "The list of invited persons-"
    
    print(f'{header.title()}')
    
    for invited in invitees:
        print(f'\t{invited.title()}')
    
    print('\n')

    while invitees:
        sent = invitees.pop(0)
        
        print(f"{sent.title()}, we would like your presence at the Precepts resorts.")
        
        print()
        
        sent_invites.append(sent)
    
    print("The following guests have been sent their invites:")
    
    for invites in sent_invites:
        print(f'\t{invites.upper()}')
    
    return

def confirm_invite(guest, invitees):
    """To check for uninvited persons."""
    
    if guest in invitees:
        print('Welcome!')
    
    elif guest not in invitees:
        print('You are not on the invited guests list.')

