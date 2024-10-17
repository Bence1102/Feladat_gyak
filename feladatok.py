'''adott egy lista
lista=[12, 21, 56, 32, -5, -23, 35]
Az alábbi metódusok paraméterként kapják a fenti listát.
1.Hány pozítiv szám van?
2.Mennyi a negatív számok összege?
3.Mennyi az öttel osztható számok összege?
'''
import random


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



'''Készíts függvényt, mely az érme dobás szimulálja és legenerál 10 db fej vagy írást
és az eredmény eltárolja egy listában. A függvény térjen vissza a listával
Továbbiakban ezzel a listával dolgozz az alábbi függvényekben: 
számold meg hány fej dobás van a listában
'''


def ermedobas():
    
    eredmeny_lista=[]
    i:int =0
    while (i<10):
        erem:int=int(random.random()*2+1)
        if (erem==1):
            eredmeny_lista.append("F")
        elif (erem==2):
            eredmeny_lista.append("Í")
        i+=1
    return eredmeny_lista

def fej_dobas(eredmeny_lista):
    i:int=0
    fej:int=0
    while (i<len(eredmeny_lista)):
        if(eredmeny_lista[i]=="F"):
            fej+=1
        i+=1
    return fej




def kockadobas():
    kocka_lista=[]
    i:int =0
    while (i<200):
        kocka:int=int(random.random()*7)+1
        if(kocka==1):
            kocka_lista.append(1)
        elif(kocka==2):                                                                                                                                                                                                                             
            kocka_lista.append(2)
        elif(kocka==3):                                                                                                                                                                                                                                
            kocka_lista.append(3)
        elif(kocka==4):                                                                                                                                                                                                                                  
            kocka_lista.append(4)
        elif(kocka==5):                                                                                                                                                                                                                                  
            kocka_lista.append(5)
        elif(kocka==6):
            kocka_lista.append(6)
        i+=1
    return kocka_lista





        

        
    
            
    