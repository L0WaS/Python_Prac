#!usr/bin/env python3

OSSZ=0


def parossz(szam):
    global OSSZ
    if szam%2==0:
        OSSZ+=szam
    return OSSZ

def main():
    maxi=4_000_000
    i=1
    elozo=1
    ment=1

    while i<maxi:
        ment=i
        parossz(i)
        i=i+elozo
        elozo=ment

    print(OSSZ)
        

if __name__ == "__main__":
    main()