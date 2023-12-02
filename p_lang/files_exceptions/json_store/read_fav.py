import json

fave_file = 'fav_numba.json'
with open(fave_file) as ff:
    numba = json.load(ff)
    msg = f"I  know your favorite number! It's {numba}."
    print(msg)
