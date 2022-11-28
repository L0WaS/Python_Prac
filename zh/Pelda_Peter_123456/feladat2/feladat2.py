#!usr/bin/env python3
MAX=0
MIN=0

def legmagasabb(szint):
    global MAX
    if szint>MAX:
        MAX=szint
    return MAX


def legmelyebb(szint):
    global MIN
    if szint<MIN:
        MIN=szint
    return MIN


def emelet(text):
    szint=0
    for line in text:
        for zarojel in line:
            if zarojel=="(":
                szint+=1
                legmagasabb(szint)
            elif zarojel==")":
                legmelyebb(szint)
                szint-=1
    return szint


def main():
    f = open('input.txt', "r")

  
    print("Cél emelet:", emelet(f))
    print("A legmagasabb emelet:",MAX)
    print("A legmelyebb emelet:",MIN)
    
    f.close()

if __name__ == "__main__":
    main()