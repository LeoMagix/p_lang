mvps = ['air jordan', 'greek freak', 'king james', 'the dream', 'chef curry']
mvps[5:] = 'shaq diesel', 'black mamba'
dpoys = ['air jordan', 'the dream', 'greek freak']
'''
for mvp in mvps[0: ]:
    if mvp in dpoys:
        dpoy = 'defensive player of the year'
        vp = 'most valuable player'
        print(f"{mvp.upper()}, won {vp} and {dpoy} awards.")
        print()
    else:
        print(f"{mvp.title()}, won {vp} award.")
        print()

print(mvps[3] is dpoys[1])

rm = mvps[4]
mvps.remove(rm)
print(f"\nI removed {rm} from the list.")
'''
for  fmvp in mvps:
    for dvp in dpoys:
        print(dvp, end=' ')
    print(fmvp)

fmvps = [mvp for mvp in mvps if mvp in dpoys]
print(fmvps)
