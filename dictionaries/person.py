#Person details
pikin = {
    'first name' : 'usain',
    'middle name' : 'st.leo',
    'last name' : 'bolt',
    'country' : 'jamaica',
    }
pikin['occupation'] = 'track & field'
pikin['100metres'] = str(9.58)
pikin['200metres'] = str(19.19)

for data, info in pikin.items():
    print(f'{data.title()}: {info.title()}')
    #if info == float:
        #print(f'{data.title()}: {info}')
    #else:
        #print(f'{data.title()}: {info.title()}')

