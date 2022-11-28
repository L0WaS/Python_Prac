#!usr/bin/env python3


def clean(s):
    i=0
    if "\n" in s:
        i=s.find("\n")
        s=list(s)
        s.pop(i)
        s=str(s)
        s=s.replace("'", "")
        s=s.replace(",", "")
        s=s.replace(" ", "")
        s=s.replace("[", "")
        s=s.replace("]", "")
        
        
    
    return s 

def main():
    s="192.20.246.138:\n 6666"
    s=clean(s)
    
    print(s) 

if __name__ == "__main__":
    main()