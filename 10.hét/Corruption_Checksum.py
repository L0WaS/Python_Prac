#!usr/bin/env python3


def main():
    
    f=open("day02.txt")
    ell_ossz=0
    for line in f:
        res = [int(i) for i in line.split()]
        lk=min(res)
        ln=max(res)
        ell_ossz+=(ln-lk)
       
    
    print("Az ellenorző összeg: ",ell_ossz)

    f.close()
if __name__ == "__main__":
    main()