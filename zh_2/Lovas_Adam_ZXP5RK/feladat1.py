#!usr/bin/env python3


JO_PW=0

def legit(pw):
    global JO_PW
    

    pw=pw.split(":")
    szamok=pw[0].split("-")
    szam1=int(szamok[0])
    szam2=int(szamok[1][:2])
    

    if pw[1][szam1]==pw[0][-1]:
        if pw[1][szam2]==pw[0][-1]:
            pass
        else:
            JO_PW+=1

    elif pw[1][szam2]==pw[0][-1]:
        if pw[1][szam1]==pw[0][-1]:
            pass
        else:
            JO_PW+=1
    
        
    
   

def main():
    f =open('passwords.txt')

    for line in f:
        
        legit(line)

    print(JO_PW)
    
    f.close()

if __name__ == "__main__":
    main()