#!usr/bin/env python3



def test(li):
    nyito = ["(", "{", "["]
    zaro = [")", "}", "]"]
    szamlalo=0
    utolso=[]
    for s in li:

        for i in range(3):
            
            
            if s == nyito[i]:
                szamlalo=szamlalo+(i+1)
                utolso.append(i+1)
            
            elif s == zaro[i]:
                szamlalo=szamlalo-(i+1)

                if utolso[len(utolso)-1]!=(i+1):
                    return False

                else:
                    utolso.pop()

            if szamlalo<0:
                return False

    if szamlalo ==0:
        return True

    else:
        return False
    

def main():

    
    print("((5+3)*2+1)",test("((5+3)*2+1)"))
    print("{[(3+1)+2]+}",test("{[(3+1)+2]+}"))
    print("(3+{1-1)}",test("(3+{1-1)}"))
    print("[1+1]+(2*2)-{3/3}",test("[1+1]+(2*2)-{3/3}"))
    print("(({[(((1)-2)+3)-3]/3}-3)",test("(({[(((1)-2)+3)-3]/3}-3)"))

    
if __name__ == "__main__":
    main()