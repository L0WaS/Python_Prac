#!/usr/bin/env python3


def is_palindrome_and_prime(s):
    szo = str(s)
    if szo==szo[::-1]:
        if s <= 1:
            return False
        else:
            for i in range(2, s):
                if s % i == 0:
                    return False
        return True
    else:
        return False


def test(szam):
    i = szam
    while is_palindrome_and_prime(i) == False:
            i += 1
    return i


def main():
    print(test(31) == 101)
    print(test(130) == 131)
    print(test(131) == 131)
    print(test(1977) == 10301)


if __name__== '__main__':
    main()