def toCoin(total, coinlist):
    presenttotal = total
    coinnumberlist = []

    for coin in coinlist:
        coinnumber = presenttotal // coin
        presenttotal = presenttotal % coin
        coinnumberlist.append(coinnumber)

    print(coinnumberlist)


if __name__ == '__main__':
    coinlist = [25,10,1]
    toCoin(63, coinlist)