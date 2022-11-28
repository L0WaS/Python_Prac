#!/usr/bin/env python3


def felsorol():

    """Felsorolja az 1000-nél kisebb egész számokat
    
    Ha azok oszthatóak 3-mal vagy 5-tel"""

    result = [i for i in range(1000) if (i%3==0 or i%5==0)]
    
    print(result)


def main():
    felsorol()


if __name__== '__main__':
    main()