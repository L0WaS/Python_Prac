#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """A függvény két stringsorozat karaktereinek egyezését adja vissza
    
    Ezt olyan módon teszi, hogy a text sztring karakterein végigmegy,
    és az ott látottakat összehasonlítja a karakterlista elemeivel.
    Amennyiben egyezést talál, egy gyűjtősztringbe (benne) helyezi ezeket,
    és visszatérésként megkapjuk az egyező karaktereket. A karaktersorozat megadása
    opiconális."""

    benne = ''
    for c in text:
        if c in chars and c not in benne:
            benne += c
    return benne



def main():

    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))


if __name__== '__main__':
    main()