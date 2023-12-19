# Write a function that takes a list of strings as an argument and returns a filtered list containing the same elements but with the 'geese' removed.

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    flt_words = []
    for word in birds :
        if word not in geese:
            flt_words.append(word)
    return flt_words
            
print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))