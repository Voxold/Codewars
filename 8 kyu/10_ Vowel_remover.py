# Create a function called shortcut to remove the lowercase vowels 
# (a, e, i, o, u ) in a given string.

def shortcut( s ):
    lowercase = ['a','e','i','o','u']
    result = [] 
    for letter in s :
        if letter not in lowercase:
            result.append(letter)
    return ''.join(result)


print(shortcut("hello"))
print(shortcut("codewars"))
print(shortcut("goodbye"))
print(shortcut("HELLO"))
