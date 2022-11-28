#!/usr/bin/env python3

def main():
    with open ('string1.py', 'r') as befile, open('string1_clean.py', 'w') as kifile:
        
        szoveg = befile.read().strip()

        sorok = szoveg.split('\n')

        for sor in sorok:

            if len(sor) == 0: 

                print(sor, file=kifile)

            elif sor.strip()[0] !=  '#':

                print(sor, file=kifile)


if __name__== '__main__':
    main()