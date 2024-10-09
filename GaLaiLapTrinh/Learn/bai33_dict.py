d = {
    # key : value
    # value có thể lặp lại
    "mot": 1,
    "hai": 2,
    "ba": 3,
}
d2 = {
    # chỉ lấy key sau cùng thôi
    "tung": 1.75,
    "tung": 1.50,
    "linh": 1.60,
}
d3 = {
    "d": {"mot": 1, "hai": 2, "ba": 3},
    "d2": {
        "tung": 1.75,
        "tung": 1.50,
        "linh": 1.60,
    },
}
d2["tung"] = 1.7
print(d2["tung"])
d2["viet"] = 1.88
print(d2)
del d2["tung"]
print(d2)
del d # xóa hết luôn
print(len(d2))
print(d2)
d2.clear()
print(d2)