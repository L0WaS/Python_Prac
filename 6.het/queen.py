#!/usr/bin/env python3

lista = [7, 3, 0, 2, 5, 1, 6, 4]

def main():
    jatekter = [['.' for i in range(8)] for j in range(8)]
    #print(tabla)

    ind = 0
    keret = "+ "+'- '*8+'+\n'
    tabla = keret
    for elem in lista:
        
        jatekter[7-elem][ind] = "Q"
        ind += 1
    for i in range(8):
        tabla += "| "
        for j in range(8):
            tabla += jatekter[i][j]
            tabla += ' '
        tabla += "|\n"
    tabla += keret
    print(tabla)

    
if __name__== '__main__':
    main()