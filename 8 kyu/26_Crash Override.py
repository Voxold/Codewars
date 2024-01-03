# Every budding hacker needs an alias!

def alias_gen(f_name, l_name):
    FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache'}
    SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst'}
    if f_name[0].upper() not in FIRST_NAME or l_name[0].upper() not in SURNAME:
        return 'Your name must start with a letter from A - Z.'
    else:
        return FIRST_NAME[f_name[0].upper()] + ' ' + SURNAME[l_name[0].upper()]

print(alias_gen('Aarry', 'Brentwood'))
print(alias_gen('123abc', 'Petrovic'))