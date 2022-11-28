#!usr/bin/env python3



def binar(i):
    b=[]
    while i >= 1:
        
        i=int(i)
        print(i)
        if i%2==0:
            b.append("0")
            
        else:
            b.append("1")

        i=i/2
        res= " ".join(b)
    return res[::-1]

def main():

    i=423
    print("A bináris formálya: ", binar(i))


if __name__ == "__main__":
    main()
