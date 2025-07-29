# To remove dublicates from a list 
def removing_dublicates(lst):
    #lst = [1,1,2,2,3,3,4,4,5,5]
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
data = [1,1,2,2,3,3,4,4,5,5]
cleared = removing_dublicates(data)
print(data)
print(cleared)




