#!/usr/bin/env python3

from typing import List
import itertools

SZAMLISTA = list(range(1,46))


OSSZEG = 90
SZORZAT = 996300

def szorzat(lista):
    sz = 1
    for number in lista:
        sz *= number
    return sz


def main():
    szamok = []
    for sz in itertools.combinations(SZAMLISTA, 6):
        if sum(sz) == OSSZEG and szorzat(sz)==SZORZAT:
            print(sz)



if __name__== '__main__':
    main()