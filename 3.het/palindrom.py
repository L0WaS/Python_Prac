#!usr/bin/env python3
def palindrom1(s):

    return (s==s[::-1])

def palindrom2(s):
    i = 0
    while i<len(s)/2 :
        if s[i] == s[(len(s)-i)-1]:
            i=i+1
        else:
            return False

    return True

def palindrom3(s, i):
        
    if i > len(s)/2-1:
        return True

    if s[(-1)-i] == s[i]:   
        return palindrom3(s, i+1)

    return False


def main():
    s1 = "radar"
    s2 = "kecske"

    print(s1,palindrom1(s1))
    print(s2,palindrom1(s2))

    print(s1,palindrom2(s1))
    print(s2,palindrom2(s2))
    
    print(s1,palindrom3(s1,0))
    print(s2,palindrom3(s2,0))


if __name__ == "__main__":
    main()