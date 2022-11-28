#!usr/bin/env python3


def megforditas(szam):
    szam = str(szam)
    szam = szam[::-1]
    return int(szam)

def main():
    szam = 1998 #ez a bemenet
        
    print("{0} -> {1}".format(szam, megforditas(szam)))   

if __name__ == "__main__":
    main()  