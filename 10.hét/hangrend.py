#!/usr/bin/env python3
from enum import Enum, auto


class Hangrend(Enum):

    MELY = auto()

    MAGAS = auto()

    VEGYES = auto()

    SEMMILYEN = auto()


def hangrend(s):
	mely_mghk = ["u", "ú", "a", "á", "o", "ó"]
	magas_mghk = ["e", "é", "i", "í", "ü", "ű", "ö", "ő"]
	nincs_benne_mgh = False
	magas = 0
	mely = 0
	for c in s:
		if c in mely_mghk:
			mely += 1
	for c in s:
		if c in magas_mghk:
			magas += 1
	if mely== 0 and magas ==0:
		nincs_benne_mgh = True

	if mely == 0 and magas != 0:
		return Hangrend.MAGAS
	elif mely != 0 and magas == 0:
		return Hangrend.MELY
	elif mely !=0 and magas !=0:
		return Hangrend.VEGYES
	if nincs_benne_mgh:
		return Hangrend.SEMMILYEN 


def main():
	szavak = ["ablak", "erkély", "kisvasút", "magas", "mély", "hmmmm"]
	for i in szavak:
		print(i, hangrend(i))


if __name__ == "__main__":
	main()