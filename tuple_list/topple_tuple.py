great_men = ('michael jordan', 'nikola tesla', 'elon musk')
print(f"There are {len(great_men)} men that inspire me to achieve greatness.")

for great_man in sorted(great_men):
    print(f'\t~{great_man.title()}.')

print(f"{great_men[0].title()} inspires me the most.\n")

mj = '1-dpoy, 5-mvps, 6-fmvps, 6-rings'
lbj = '0-dpoy, 4-mvps, 4-fmvpd, 4-rings'
kob = '0-dpoy, 1-mvp, 2-fmvp, 5-rings'

top3 = (mj, lbj, kob)
print(top3)

old_cats = top3 + ('mj23', 'lbj6', 'kob24')
print(old_cats)
