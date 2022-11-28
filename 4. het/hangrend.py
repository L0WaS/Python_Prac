#!usr/bin/env python3



def hangrend(words):
    
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'

    for s in words:
        mely = 0
        magas = 0

        for c in s:
            if c in MELY_MGHK:

                mely+=1

            if c in MAGAS_MGHK:

                magas+=1

        if mely>=1 and magas>=1:
            print(s,": Vegyes hangredű a szó!", sep="")

        elif mely>=1 and magas==0:
            print(s,": Mely hangredu a szó!", sep="")

        elif magas>=1 and mely==0:
            print(s,": Magas hangredu a szó!", sep="")
        else:
            print(s,": Semmilyen hangredű a szó!", sep="")
            
    return ""
def main():

    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pfff"]

    print(hangrend(words))

if __name__ == "__main__":
    main()