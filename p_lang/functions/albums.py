def make_album(artist, title, songs=None):
    """Creating an album using a dictionary."""
    album = {}
    if songs:
        album['artist name'] = artist
        album['album title'] = title
        album['number of songs'] = songs
    else:
        album['artist name'] = artist
        album['album title'] = title
    
    return album

yea = make_album('kanye', 'donda')
print(yea)

for data, info in yea.items():
    print(f"{data.title()} -{info.title()}")

print('\n')

burna = make_album('burna boy', 'african giant', '16')
print(f'{burna}')

for data, info in burna.items():
    print(f'{data.title()} -{info.title()}')

while True:
    print("\nEnter the name of your favorite artist and album.\n "
           "You can always enter 'yes' to exit.")
    
    artist = input("Please enter name of Artist:\n")
    album = input("Enter name of Album:\n")
    songs = input("Number of Songs:\n")

    user = make_album(artist, album, songs)
    #print(user)

    for artist, desc in user.items():
            print(f"{artist.title()}")
            print(f"\t{str(desc).title()}")
    
    interact = input("would you like to exit?- ")
    if interact == 'yes' or interact == 'YES'  or interact == 'Yes':
        break

