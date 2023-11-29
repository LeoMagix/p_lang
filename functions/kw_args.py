#Working With Arbitrary Keyword Arguments
#> Kwargs**
'''
def try_kwargs(**lsts):
    """Does **kwargs really only build dictionaries?"""
    for lst in lsts:
        print(lst)
#THE ANSWER IS YES
lev = ['a', '23', 'box']
try_kwargs(lev)
'''

def build_profile(first, last, **user_info):
    """Build a dictionary with everything about a user."""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', 
                            location = 'princeton', fields = 'physics')
print(user_profile)
