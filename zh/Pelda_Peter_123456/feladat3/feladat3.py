#!/usr/bin/env python3
import math

def feldolg(f):

    li = []
    sorok = []

    string = ""
    for line in f:

        sorok.append(line)

        line = line.split(";")

        if math.sqrt(int(line[0])).is_integer():  

            li.append(int(line[0]))
    li.sort()

    for i in li:
        for j in sorok:
            j = j.split(";")
            if i == int(j[0]):
                string += j[1][0]

    print(string.replace("_" , " "))


def main():

    f = open("input.txt", "r")

    feldolg(f)
   

    f.close()


if __name__ == "__main__":
    main()