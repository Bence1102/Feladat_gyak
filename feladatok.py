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
        if(lista[0]>0):
            db+=1
        i+=1
    return db