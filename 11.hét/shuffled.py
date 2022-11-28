#!usr/bin/env python3

import random


def shuffled(li):
    valami=list(li)
    random.shuffle(valami)
    return valami


def main():

    li = [24,32,89,11,73,21,12]
    print("Összekevert lista utolsó eleme: ",shuffled(li)[-1])
    print("Eredeti Lista: ",li)
    

if __name__ == "__main__":
    main()