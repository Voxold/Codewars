# Convert a hash into an array. Nothing more, Nothing less.

def convert_hash_to_array(h):
    new_list = list(map(list, h.items()))    
    return sorted(new_list)

print(convert_hash_to_array({'name': 'Jeremy', 'age': 24, 'role': 'Software Engineer'}))