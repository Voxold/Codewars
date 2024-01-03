# Write a function that checks if a given string (case insensitive) is a palindrome. 

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

print(is_palindrome('Madam'))
print(is_palindrome('Racecar'))
print(is_palindrome('121'))

