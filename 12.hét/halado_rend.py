#!usr/bin/env python3


#   def my_func(li):
#       return li[1]


def main():

    li=[ [2,6],[1,3],[5,4] ]

    print(li)
    # print(sorted(li,key=my_func))
    print(sorted(li,key=lambda li: li[1]))

if __name__ == "__main__":
    main()