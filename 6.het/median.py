#!usr/bin/env python3


def median(li):
    med=0
    li.sort()

    if len(li)%2==0:
        i=len(li)/2
        i=int(i)
        med=(li[i-1]+li[i])/2

    else:
        i=len(li)/2
        i=int(i)
        med=li[i]
    return li, "mediánja -> ", med
def main():

    li1=[1, 300, 2, 200, 1]
    li2=[3, 6, 20, 99, 10, 15]

    print(median(li1))
    print(median(li2))

if __name__ == "__main__":
    main()