# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

# Method 1 :
def remove_exclamation_marks(s):   
    return s.replace('!','')

# Method 2 :
def remove_exclamation_marks2(s):
   return ''.join([x for x in s if x != '!'])

print(remove_exclamation_marks('Bilal!Bilal!Bilal!'))
print(remove_exclamation_marks2('Bilal!Bilal!Bilal!'))



