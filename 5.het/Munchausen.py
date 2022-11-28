#!usr/bin/env python3


def Munche(meddig):
    """Összeadja az adott számjegyeket a önmaguk hatványára emelve pl 152-nél 
    x=1**1+5**5+2**2 ami nem egyenlő 152-vel vagyis nem Münhausen szám."""

    for i in meddig:

        x=0
        if i==0:
            print(i)
        for c in str(i):

            c=int(c)
            x=x+(c**c)
           
            
        
        if x==i:
            print(i)

    
def main():
    Munche(range(440000000))


if __name__ == "__main__":
    main()