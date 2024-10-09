lst = [1,2,3,4,54,65,6,7,8,98]
solo = [[1,2],[3,4],[5,6],[6,7]]
id  = 1

def duyet_solo(id,arr):
    newarr = []
    for i in duyet(arr):
        for j in i:
            newarr.append(j)
    print(newarr)
    return id in newarr


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


print(duyet_solo(id,solo))