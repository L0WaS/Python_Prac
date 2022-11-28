#!/usr/bin/env python3


class Sor:
    def __init__(self):
        self.verem1 = []
        self.verem2 = []

    def append_ertek(self, num):
        self.verem1.append(num)
        self.verem2 = self.verem1


    def popleft_ertek(self):
        vissza = self.verem2[0]
        self.verem1 = self.verem1[1:]
        self.verem2 = self.verem2[1:]

        return vissza

    def is_empty(self):
        return self.verem1 == [] and self.verem2 == []

    def size_sor(self):
        return len(self.verem1)


    def __str__(self):
        return str(self.verem1)

def main():
    s = Sor()
    print(s)
    print(s.is_empty())
    print(s.size_sor())
    s.append_ertek(2)
    s.append_ertek(8)
    print(s)
    s.append_ertek(6)
    print(s)
    print(s.popleft_ertek())
    print(s)
    print(s.is_empty())
    print(s.size_sor())




if __name__ == "__main__":
    main()
