'''adott egy lista
lista=[12, 21, 56, 32, -5, -23, 35]
Az alábbi metódusok paraméterként kapják a fenti listát.
1.Hány pozítiv szám van?
2.Mennyi a negatív számok összege?
3.Mennyi az öttel osztható számok összege?
'''



def poz_szamok_szama(lista):
    print(lista)
    i:int=0
    db:int=0
    while(i<len(lista)):
        """print(lista[i])"""
        if(lista[i]>0):
            db+=1
        i+=1
    return db


def negativ_szamok_osszege(lista):
    print(lista)
    i:int=0
    ossz:int=0
    while(i<len(lista)):
        if(lista[i]<0):
            ossz += lista[i]
        i+=1
    return ossz


def ottel_oszthatoak(lista):
    print(lista)
    i:int=0
    db:int=0
    oszt:int=0
    while(i<len(lista)):
        if(lista[i]%5==0):
            oszt+=lista[i]
            db+=1
        i+=1
        
    return oszt


    