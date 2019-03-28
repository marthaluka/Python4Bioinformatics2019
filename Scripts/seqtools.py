def remove_at(pos, seq):
'''
Removes acharacter at a specified postion in a string
'''
    return seq[:pos] + seq[pos+1:] #From position, skip one then print to the end