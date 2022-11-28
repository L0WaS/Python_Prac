#!/usr/bin/env python3


from os import set_inheritable


def fel_1():
    """Nagybetűsen, ! véggel írja ki a kapott szót"""
    words = ['auto', 'villamos', 'metro']
    result = [w.upper()+'!' for w in words]
    print(words, ' --> ', result)


def fel_2():
    """Nagy kezdőbetűvel írja ki a kapott szót"""
    names = ['aladar', 'bela', 'cecil']
    result = [n.capitalize() for n in names]
    print(names, " --> ", result)


def fel_3():
    """Kiír 10 darab 0-t"""
    result = [0 for i in range(10)]
    print(result)


def fel_4():
    """Kiírja a kapott szám dupláját"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = [2*n for n in nums]
    print(result)


def fel_5():
    """Intté alakítja a kapott string formájú számot"""
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    result = [int(n) for n in nums]
    print(result)


def fel_6():
    """Számjegyeire bontja a kapott intet"""
    string = "1234567"
    result = [int(n) for n in string]
    print(string, ' --> ', result)


def fel_7():
    """Kiírja a kapott string szavainak hosszát"""
    sent = 'The quick brown fox jumps over the lazy dog'
    result = [len(word) for word in sent.split()]
    print(sent, " --> ", result)


def fel_8():
    """Kiírja a kapott string szavainak első betűit"""
    sent = "python is an awesome language"
    result = [word[0] for word in sent.split()]
    print(sent, " --> ", result)


def fel_9():
    """Kiírja a kapott string szavait, és azoknak hosszát"""
    sent = 'The quick brown fox jumps over the lazy dog'
    result = [(word, len(word)) for word in sent.split()]
    print(sent, " --> ", result)


def fel_10():
    """Kilistázza a 10-nél kisebb páros számokat"""
    result = [i for i in range(10) if i%2==0]
    print(result)


def fel_11():
    """Kilistázza a 20-nál kisebb számok páros négyzeteit"""
    result = [i*i for i in range(20) if (i*i)%2==0]
    print(result)


def fel_12():
    """Kilistázza a 20-nál kisebb számok 4-re végződő négyzeteit"""
    result = [i*i for i in range(20) if (i*i)%10==4 ]
    print(result)


def fel_13():
    """Összefűzi az angol ABC nagybetűit egy stringgé
    
    Bemenetként a szavak karakter unicode kódját kapja"""
    not_result = [chr(i) for i in range(65, 91)]
    characters = ""
    for betu in not_result:
        characters+=betu
    print(characters)


def fel_14():
    """Eltávolítja a szavak elejéről és végéről a whitespace karaktereket"""
    lista = [' apple ', ' banana ', ' kiwi']
    result = [word.strip() for word in lista]
    print(result)


def fel_15():
    """Egy sztrinngé fűzi össze a kapott számjegyeket"""
    digits = [1, 0, 1, 1, 0, 1, 0, 0]
    result = [str(i) for i in digits]
    bin = ""
    for betu in result:
        bin+=betu
    print(bin)


def main():
    elv = '__'*20
    fel_1()
    print(elv)
    fel_2()
    print(elv)
    fel_3()
    print(elv)
    fel_4()
    print(elv)
    fel_5()
    print(elv)
    fel_6()
    print(elv)
    fel_7()
    print(elv)
    fel_8()
    print(elv)
    fel_9()
    print(elv)
    fel_10()
    print(elv)
    fel_11()
    print(elv)
    fel_12()
    print(elv)
    fel_13()
    print(elv)
    fel_14()
    print(elv)
    fel_15()
    print(elv)
    


if __name__== '__main__':
    main()