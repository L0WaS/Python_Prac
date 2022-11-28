#!usr/bin/env python3


def szamjegyossz(nums):

    osszeg=0
    osszefuz =""
    
    for n in nums:
        osszefuz=str(n)

        for i in osszefuz:
            osszeg+= int(i)

    return osszeg

def main():

    nums=(list(range(1,101)))
    print("Az elso szaz szam szamjegyeinek osszege: ", szamjegyossz(nums))


if __name__ == "__main__":
    main()