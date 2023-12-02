dominance = ['mvp_fmvp.txt', 'finals.txt', 'dpoy_mvp_fmvp.txt']
dominance += ['mvps.txt']

for player_files in dominance:
    try:
        with open(player_files) as pf:
            lst = pf.read()
    except FileNotFoundError:
        #print(f"The file {player_files} doesn't exist.")
        pass
    else:
        print(lst)
