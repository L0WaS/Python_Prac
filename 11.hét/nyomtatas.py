#!/usr/bin/env python3


def kibogozo(hosszustring: str) ->list:
    lista = hosszustring.split(',')
    szamlista = []
    for string in lista:
        if len(string) == 1:
            szamlista.append(int(string))
        else:
            szamok = string.split('-')
            szamok[0] = int(szamok[0])
            szamok[1] = int(szamok[1])
            for szam in range(int(szamok[0]), int(szamok[-1]+1)):
                if szam not in szamlista: 
                    szamlista.append(szam)
    return sorted(szamlista)


def main():
    print(kibogozo('1-4,7,9,11-15'))


if __name__== '__main__':
    main()