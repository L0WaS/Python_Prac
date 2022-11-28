#!usr/bin/env python3


def binary(szam):
    ossz=0
    i=128
    for szamjegy in szam:
        ossz+=int(szamjegy)*i
        i=i/2
    
    return ossz

def Translate(li):

    szoveg=""

    for letter in li:
        
        szoveg+=chr(int(binary(letter)))
    
    return szoveg

def main():

    TEXT="""01111001 01101111
01110101 01110100
01110101 00101110
01100010 01100101
00101111 01100100
01010001 01110111
00110100 01110111
00111001 01010111
01100111 01011000
01100011 01010001""".split()

    print(Translate(TEXT))

    

    
    

if __name__ == "__main__":
    main()