#!usr/bin/env python3


def negyzet(ossz):
    ossz1=0
    ossz2=0
    res=0
    for n in ossz:
        ossz1+=n*n
        ossz2+=n
    ossz2=ossz2*ossz2
    res=ossz2-ossz1
    return res

def main():

    ossz=range(1,101)

    print(negyzet(ossz))


if __name__ == "__main__":
    main()