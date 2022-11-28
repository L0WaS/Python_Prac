#!usr/bin/env python3



def diamond(i):
    dia=""
    i2=i/2+1
    csillag=1
    
    

    if i%2==0:

        return "Nem lehet paros a magassag!"
        
    else:
        while i>0:
            if i>i2:
                print((csillag*"*").center(100))
                csillag+=2
                
            
            else:
                print((csillag*"*").center(100))
                csillag-=2

            
            i-=1
        return ""


def main():
    i=11

    print(diamond(i).center(10))


if __name__ == "__main__":
    main()