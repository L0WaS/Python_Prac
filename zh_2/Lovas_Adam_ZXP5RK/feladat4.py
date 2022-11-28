#!usr/bin/env python3

def palindrome(sor):
    
    sor=sor.split()
    for word in sor:
        if word==word[::-1]:
            print(word," ",end="")
        else:
            word2=""
            for i in range(len(word)):
                word2+="X"
            print(word2," ",end="")
    print("")


def main():

    f = open('szoveg.txt')

    for line in f:
        palindrome(line)
    
    f.close()

if __name__ == "__main__":
    main()