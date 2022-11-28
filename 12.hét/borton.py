#!usr/bin/env python3


def fordit(cell,counter):
    
    for i in range(600):
        if (i+1)%counter==0 :
            if cell[i]==0 :
                cell[i]=1
            elif cell[i]==1:
                cell[i]=0
    return cell

def szabad(cell):
    free=""
    for i in range(len(cell)):
        if cell[i]==1:
            free+=str(i+1)+" "
    return free

def main():

    cellak = []
    for i in range(600):
        cellak.append(0)
    
    for k in range(1,600+1):
        
        cellak=fordit(cellak,k)
    
    print(cellak)
    print("A következő cellák rabjai szabadok: ",szabad(cellak))


if __name__ == "__main__":
    main()