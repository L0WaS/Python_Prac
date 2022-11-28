#!usr/bin/env python3


class Verem():

    def __init__(self):
        self.data=[]

    
    def ures(self):
        return  len(self.data)==0


    def betesz(self,szam):
        self.data.append(szam)

    
    def kivesz(self):
        if len(self.data)>0:
            return self.data.pop()
        else: 
            return
            

    def meret(self):
        return len(self.data)


    def __str__(self):
         return str(self.data)


def main():
    v = Verem()      # üres verem létrehozása
    print(v)  
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)

if __name__ == "__main__":
    main()