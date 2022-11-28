#!usr/bin/ens python3


class Sor():
    def __init__(self):
        self.data=[]

    
    def ures(self):
        return  len(self.data)==0


    def betesz(self,szam):
        self.data.append(szam)

    
    def kivesz(self,honnan):
        if len(self.data)>0 and honnan=="hátulról":
            return self.data.pop()
        
        elif len(self.data)>0 and honnan=="elölről":
            return self.data.pop(0)

        else: 
            return "elölről/hátulról vegyek ki elemet?"
            

    def rendez(self,hogyan):
        if hogyan=="csökk":
            self.data.sort(reverse=True)
        elif hogyan=="növ":
            self.data.sort()
        else:
            print("csökk/növ lehet a rendezés")


    def meret(self):
        return len(self.data)


    def elem(self, melyik):
        if melyik=="legnagyobb":
            return max(self.data)
        elif melyik=="legkisebb":
            return min(self.data)
        else:
            return "legnagyobb/legkissebb elemre vagy kiváncsi?"


    def __str__(self):
         return str(self.data)

def main():
    s = Sor()      # üres serem létrehozása
    print(s)  
    print(s.ures())  # True
    s.betesz(8)
    s.betesz(4)
    s.betesz(5)
    print(s)
    s.rendez("növ")
    print(s)
    print(s.meret()) # 3
    print(s.ures())  # False
    x = s.kivesz("elölről")
    print(x)
    print(s)
    print(s.elem("legkisebb"))


if __name__ == "__main__":
    main()