#=================================================================#
#
# North Pole Inventory Management, 
#   used to scan warehouse boxes for ****** new prototype red suit
#   
#       Crafter: jAAkiT      
#       
#=================================================================#


def letter_count(word):
    counts = {}
    for char in word:
        if char not in counts: 
            counts[char] = 1
        else:
            counts[char] += 1
    return counts


def contains_doubles_and_triples(dictionary):
    '''
        returns double = True/False, triple = True/False
    '''
    double = False
    triple = False
    for val in dictionary.values():
        if val == 2:
            double = True
        if val == 3:
            triple = True 
    return double, triple


def position_in_alphabet(char):
    return ord(char) - 96
    

#=================
# Run


doubleCount = 0
tripleCount = 0

file = open("input.txt", 'r')
for id in file:
    counts = letter_count(id)

    double, triple = contains_doubles_and_triples(counts)
    if double:
        doubleCount += 1 
    if triple:
        tripleCount += 1 

print(doubleCount, tripleCount)
print(doubleCount * tripleCount)






