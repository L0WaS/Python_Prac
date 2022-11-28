#!usr/bin/env python3


def kereso(lista,betuk):

    for szo in lista:
        talalat=0
        elozo=-1
        for betu in betuk:
            if szo.find(betu)>elozo:
                elozo=szo.find(betu)
                talalat+=1
            if talalat==len(betuk):
                return szo
    


def main():

    f=open("DT2.csv",'r')
    szavak = []
    for line in f:
        szavak.append(line.split(",",1)[0].replace("Ăˇ","á").replace("Ă©","é").replace("Ăł","ó").replace("Ă´","ő").replace("Ăş","ú").replace("ăľ","ű").replace("ĂĽ","ű").replace("Ă­","í").replace("Ĺ±","ű").replace("Ă¶","ö"))

    f.close()
    

    bolygok=["j","s","u","n"]
    print(kereso(szavak,bolygok))
    

if __name__ == "__main__":
    main()