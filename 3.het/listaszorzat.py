#!/usr/bin/env python3



def szorzas(li):

    a = 1

    for szam in li:
        a = a*szam

    return a


def main():
    li = [2, 3, 4,] 
    li2 = []
    li3 = [20, 30, 40, 50, 60, 2, 13]
    
    print(szorzas(li))
    print(szorzas(li2))
    print(szorzas(li3))


if __name__ == "__main__":
    main()