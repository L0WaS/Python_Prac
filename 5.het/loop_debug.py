#!/usr/bin/env python3


def loop(num, debug=False):
    """Kiírja a számokat 1-től numig, szóközzel elválasztva.
    Ha a debug paramétert igaz értékre állítjuk, 
    kiírjuk, melyik fázisban jár éppen az eljárás"""
    if debug == True:
        print('#ciklus kezdete:')
    for i in range(num+1):
        if i != 0:
            print(i, end=" ")
    if debug == True:
        print('\n#ciklus vége')


def main():
    loop(5, debug=True)


if __name__== '__main__':
    main()