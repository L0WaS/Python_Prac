#!usr/bin/env python3


def main():
    str1="Valami"
    str2=""

    if bool(str1)==True and bool(str2)==False or bool(str1)==False and bool(str2)==True:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()