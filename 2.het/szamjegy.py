#!usr/bin/env python3


def szamjegy(s):
    s=str(s) #ez itt a nagy trükk
    s=len(s)
    return s

def main():
    s=2**256
    print(szamjegy(s))

if __name__ == "__main__":
    main()