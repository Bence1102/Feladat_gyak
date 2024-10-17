import feladatok

lista=[12, 21, 56, 32, -5, -23, 35]
print("1.feladat")
db:int=feladatok.poz_szamok_szama(lista)
print(f"A pozítiv számok száma {db}")

lista=[12, 21, 56, 32, -5, -23, 35]
print("2.feladat")
vego:int=feladatok.negativ_szamok_osszege(lista)
print(f"A negatív számok {vego}")


lista=[12, 21, 56, 32, -5, -23, 35]
print("3.feladat")
atlag:int=feladatok.ottel_oszthatoak(lista)
print(f"5-tel osztható számok átlaga: {atlag}")



print("4.feladat")
eredmeny_lista=feladatok.ermedobas()
print(f"Érme dobás: {eredmeny_lista}")

 
print("4.feladat 2.része")
Fej=feladatok.fej_dobas(eredmeny_lista)
print(f"Mennyi fejet dobtunk: {Fej}")


print("5.feladat")
dobo_kocka=feladatok.kockadobas(eredmeny_lista)
print(f"Dobások: {dobo_kocka}")