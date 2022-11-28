#!usr/bin/env python3

def normalize(szo):

    szo=szo.lower().strip().replace(" ","")

    return szo

def anagramma(szo,szo2):

    szo00=sorted(normalize(szo))
    szo002=sorted(normalize(szo2))

    if szo00==szo002:
        return szo, "==", szo2, "Ezek a szavak anagrammák"

    else:
        return szo, "==", szo2, "Ezek a szavak nem anagrammák"

    

def main():

    szo="Clint Eastwood"
    szo2="Old west action"
    szo3="kecske"

    print(anagramma(szo,szo2))
    print(anagramma(szo,szo3))


if __name__ == "__main__":
    main()