#!usr/bin/env python3


def dekod(s):
    alphabet="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCc"
    

    for szo in s:
        if alphabet.find(szo) >=0:
            betu=alphabet.find(szo)+4
            s=s.replace(szo,alphabet[betu])

    return s
def main():

    s="""Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""

    

    print(dekod(s))


if __name__ == "__main__":
    main()


    #Ezt nem tudtam tökéletesíteni sajnos. 