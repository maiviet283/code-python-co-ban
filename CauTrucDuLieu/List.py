lst = [[1,2],[3,4],[5,6],[6,7],[7,8],[9,0],[1,12]]
lst2 = [[1,2],[3,4],[5,6],[6,7],[7,8]]

def duyet(arr):
    arr2 = []
    to_remove = set()
    for i in arr:
        for j in i:
            arr2.append(j)
    for i, sublist in enumerate(arr):
        for j in sublist:
            if arr2.count(j) >= 2:
                to_remove.add(i)
                arr2.remove(j)
    new_arr = [sublist for i, sublist in enumerate(arr) if i not in to_remove]
    return new_arr

print(duyet(lst))
print(lst)
