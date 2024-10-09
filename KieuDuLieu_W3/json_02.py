import json
lst = [1,2,3,4,"enter"]
sv = {
    "name" : "Mai Quoc Viet",
    "age" : 20,
    "address" : "Ha tinh",
    "flame" : True
}
json_lst = json.dumps(lst)
json_sv = json.dumps(sv,indent=4,separators=(","," = "))
print(json_sv)