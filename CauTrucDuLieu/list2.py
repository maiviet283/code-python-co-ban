lst = [[1,2],[3,4],[5,6]]
lst2 = [[1,2],[3,4],[5,6],[6,7],[7,8]]

def duyet_lai(a,arr):
    for i in arr:
        if a in i:
            arr.remove(i)
    return arr

print(duyet_lai(2,lst))
print(lst)
