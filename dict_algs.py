ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 19,
    }, {
        "name": "petja",
        "age": 20,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 11,
    }, {
        "name": "pavel",
        "age": 15,
    }],
}

emps = [ivan, darja]
def d(emps):
    for key in range(len(emps)):
        k=False
        mas=emps[key]["children"]
        for key1 in range(len(mas)):
            if mas[key1]["age"]>18:
                k=True
        if (k==True):
            print (emps[key]["name"])
    return 0
a = d(emps)


