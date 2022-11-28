#!/usr/bin/env python3
import sys

SZAMOK = "123456789"

def double_digits(text: str) ->str:
    global SZAMOK

    word = ''

    for karakter in text:

        if karakter in SZAMOK:

            word += karakter*2

        else:

            word += karakter

    return word
    
def main():

    if len(sys.argv) <2 or len(sys.argv)>2:
        print("Hibás paraméterezés! Egyetlen sztringet kell megadni!")
    else:
        word = sys.argv[1]   
        print(double_digits(word))



if __name__== '__main__':
    main()