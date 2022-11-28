#!/usr/bin/env python3

from random import choice as c

start = ['A megoldás, hogy ', 'Fontosnak tartjuk, hogy ', 'Képtelenség volna, hogy ', 'Célunk, hogy ', 'Szeretném ', 'Elegem van abból, hogy ']
valami1 = ['a gyermekek ', 'a vállalatunk ügyfelei ', 'a feleségeink ', 'az Európai Unió ', 'a Rickroll, mint fogalom ', 'a dinoszauruszok ']
valami2 = ['feláldozzák ', 'megismerjék ', 'örökítsük ', 'megdöntsük ', 'halálnak halálával haljon ', 'eltűnjön ', 'a konyhában merengjenek tovább']
veg = ['a föld színéről.', '', 'a kacsák csodálatos világát.', 'a nihilbe.']

def get_bullshit():
    return c(start)+c(valami1)+c(valami2)+c(veg)