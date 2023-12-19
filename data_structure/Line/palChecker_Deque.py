from Deque import Deque

def palChecker(astring):
    chardeque = Deque()

    for i in list(astring):       #for ch in astring ¼´¿É
        chardeque.addRear(i)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


if __name__ == '__main__':

    print(palchecher('abcba'))
