def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('madam'))
print(is_palindrome('racecar'))
print(is_palindrome('121'))