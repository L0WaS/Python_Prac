#!usr/bin/env python3

def szamjegyossz(szam):
    ossz=0
    szam=str(szam)

    for i in szam:
        ossz+=int(i)

    return ossz

def main():

    szam=2**1000

    print(szamjegyossz(szam))

if __name__ == "__main__":
    main()