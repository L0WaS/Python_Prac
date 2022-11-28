#!usr/bin/env python3
import sys

def osszefuz(text1,text2,text3,hossz):
    

    for i in range(hossz):
        print(text1[i],text2[i],text3[i], sep="", end="")
    
    

def main():

    if len(sys.argv) != 4:
        print("Hiba! Pontosan harom sztringet adj meg.")
    
    k=max(len(sys.argv[1]),len(sys.argv[2]),len(sys.argv[3]))
    

    m1=k-len(sys.argv[1])
    m2=k-len(sys.argv[2])
    m3=k-len(sys.argv[3])

    szoveg1=sys.argv[1]
    szoveg2=sys.argv[2]
    szoveg3=sys.argv[3]

    

    for i in range(m1):
        szoveg1+="X"

    for i in range(m2):
        szoveg2+="X"

    for i in range(m3):
        szoveg3+="X"

    osszefuz(szoveg1,szoveg2,szoveg3,k)

    

if __name__ == "__main__":
    main()