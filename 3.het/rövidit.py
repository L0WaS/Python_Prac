#!/usr/bin/env python3
# encoding: utf-8

import sys


def main():
    y=['y','Y','yes']
    inp = input("Do you really want to quit [y/Y/yes]? ")
    if inp in y: 
        print('bye')
        sys.exit(0)
    
    print('The show goes on...')



if __name__ == "__main__":
    main()