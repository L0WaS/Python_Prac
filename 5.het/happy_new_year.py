#!/usr/bin/env python3

def main():
    """A függvény az unicode karakterek segítségével generál számot
    
    Fogom a '.' karaktert aminek az értéke 46 ezt megszorzam egy pontal (46) és kivonok 95-t '_'. """
    print(ord('.')*ord('.')-ord('_'))
    


if __name__== '__main__':
    main()