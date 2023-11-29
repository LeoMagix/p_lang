#kwargs** Nigga
def build_user(first, last, **user_info):
    """Creating a dictionary of personal infomation."""
    user_info['first name'] = first
    
    user_info['last name'] = last
    
    for profile, info in reversed(user_info.items()):
        print(f"\n{profile.title()}:")
        
        print(f"\t{info.title()}")
        
        print()
    
    return user_info


quote = "failure like chaos is nothng but a ladder."

bible = "look ahead in honest confidence, plan whatever you do carefully,\n"

bible += "\tand whatever you do will turn out fine.- prov. 4:26"

bio = build_user('david', 'adah', 
                 favorite_quote=quote,
                 favorite_bible_quote=bible,
                 life_goal='excellence')
print(bio)
