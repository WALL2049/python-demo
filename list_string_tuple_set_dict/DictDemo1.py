# coding=utf-8

class DictDemo1:
    def __init__(self):
        pass

if __name__ == "__main__":
    dict1 = {"size" : "38", "height" : 168, "weight" : "110", "name" : "Marry"}
    dict2 = dict()

    dict2["age"] = "18"
    dict2["gender"] = "famale"
    print(dict2)

    dict1.update(dict2)
    print(dict1)

    dict1.pop("size")
    print(dict1)
    dict1.popitem()
    print(dict1)
    del dict1["name"]
    print(dict1)

    dict1["weight"] = "115"
    print(dict1)
    print(dict1.get("weight"))
    print(dict1["weight"])

    print(list(dict1.keys()))
    for key in dict1.keys():
        print(key, end="")
    print(list(dict1.values()))
    for value in dict1.values():
        print(value, end="")
    print("\n=========\t========")
    for key, value in dict1.items():
        print(f"{key}的值是{value}")