#!/usr/bin/env python3


def main():

    with open("numbers.csv", "r") as be:
        input = list(be)
        nums = []
        parts = []
        hun_num = 0
        eng_num = 0
        hun_num_sum = 0
        eng_num_sum = 0

        for line in input:
            for part in line.strip().split(';'):
                parts.append(part)

        for i in range(len(parts)):
            if ((i+1) % 4) != 0:
                nums.append(parts[i])

        for num in nums:

            if "." in num:

                eng_num += 1
                osszeadhato = float(num)
                eng_num_sum += osszeadhato

            if "," in num:

                hun_num += 1
                osszeadhato = float(num.replace(",", '.'))
                hun_num_sum += osszeadhato


        print(f"A fájlban {eng_num} db angol és {hun_num} db magyar szám található.")

        print(f"Angol számok összege: {eng_num_sum}")
        print(f"Magyar számok összege: {hun_num_sum}")


if __name__ == '__main__':
    main()
