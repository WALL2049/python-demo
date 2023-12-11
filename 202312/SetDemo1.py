class SetDemo1:
    def __init__(self):
        pass

if __name__ == "__main__":
    set1 = {1,2,3,4,4,4,5}
    print(set1)
    set1.add(9)
    print(set1)

    set1.remove(9)
    print(set1)
    set1.pop()
    print(set1)

    del set1
    print(set1)