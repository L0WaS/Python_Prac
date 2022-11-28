#!usr/bin/env python3



TEXT="""A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""


def ekezet(text):
    ekezetes="áéíóöőúüűÁÉÍÓÖŐÚÜŰ"
    sima="aeiooouuuAEIOOOUUU"
    for i in range(len(ekezetes)):
        text=text.replace(ekezetes[i],sima[i])
    return text


def main():
    print(ekezet(TEXT))
    


if __name__ == "__main__":
    main()