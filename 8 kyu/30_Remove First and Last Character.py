# Remove First and Last Character

def remove_char(s):
    list_s = list(s)
    list_s[0] = ''
    list_s[-1] = ''
    return ''.join(list_s)

print(remove_char('world'))
print(remove_char('English'))