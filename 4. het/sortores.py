import sys
import random as r

UPTO = 101


def main():
    for i in range(1,UPTO):
        print(r.randint(0, 9), end="")
        if i%10==0:
            print("")
    
    
if __name__ == "__main__":
    main()