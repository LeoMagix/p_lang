#WORKING A while LOOP WITH A DICTIONARY.

response = {}

#Set a flag to indicate that the poll is active
poll_active = True

while poll_active:
    #prompt for person's name and opinion
    nom = input("What's your name?\n")
    print()
    opinion = input("Who do you prefer, Messi or Ronaldo?\n")
    print()

#store opinions in the dictionary
    response[nom] = opinion

    #Find out if anyone else is interested i the poll.
    others = input("Anybody else interested in taking the poll? (yes/no)\n")
    print()
    if others == 'no':
        poll_active = False

#Poll is complete.
print("\n---Poll Results---")
for name, responses in response.items():
    print(f"{name} prefers {responses}.")
