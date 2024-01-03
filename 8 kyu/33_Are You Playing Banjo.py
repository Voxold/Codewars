# Create a function which answers the question "Are you playing banjo?".

def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"
    
print(are_you_playing_banjo('Green'))
print(are_you_playing_banjo('Red'))
print(are_you_playing_banjo('red'))