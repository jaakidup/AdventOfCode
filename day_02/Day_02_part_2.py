#=================================================================#
#
# North Pole Inventory Management, box finder, 
#   used to find two consecutive box ids
#   
#       Crafter: jAAkiT      
#       
#=================================================================#


def words_compare(first, second):
    common = ""
    i, diff = 0, 0
    if first == second: return False, common
    for char in first:
        if char != second[i]:
            diff += 1
            if diff == 2:
                return False, common
        else:
            common += char
        i += 1
    if diff == 1:
        return True, common


file = open("input.txt", 'r')
ids = []
for id in file:
    ids.append(id)


for index, id in enumerate(ids):
    for next in ids[index+1:len(ids)]:
        seq, common = words_compare(id, next)
        if seq:
            print("Matching ID chars: ", common)











