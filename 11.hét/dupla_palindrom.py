#!/usr/bin/env python3

def is_palindrome(d: str) -> str:
    return d==d[::-1]


def D2B(n: int) -> str:
    s = str(bin(n)).replace('0b', '')
    return s


def teszt(sz: int) -> bool:
    bi = D2B(sz)
    sz = str(sz)
    if is_palindrome(sz)==True and is_palindrome(bi)==True:
        return True
    else: return False


def main():
    osszeg = 0
    for i in range(1000000):
        if teszt(i)==True:
            osszeg += i
    print(osszeg)


if __name__== '__main__':
    main()