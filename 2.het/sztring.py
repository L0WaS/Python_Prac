#!/usr/bin/env python 3
#Ez a metódus megnézi, hogy az adott string "üres"-e, pontosabban, hogy csak whitespace-ket tartalmaz-e. 
# Onnantól kezdve hogy tartalmaz 1 karaktert is ami nem space (a tabulátor is spacnek számít), az eredmény hamis lesz.

def main():
    print("asd".isspace())
    print(" asd ".isspace())
    print("  a s d  ".isspace())
    print("  a  ".isspace())
    print(" ".isspace())
    print("         ".isspace()) 

if __name__ == "__main__":
    main()