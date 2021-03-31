print("Adj meg szavakat amikben van f én kicserélem ph-ra.")
a = str(input("Adj meg karaktersorozatot:   "))
b = "ph"
#for cv in range(len(a)):
print(a.replace("f", b))
  #  break
print("------")
print("Értékelés")
print("Dani, ha metódust - beépített függvényt használsz, akkor nem kell ciklus.. - Nézd meg a kódodat...\n Ha ciklust használsz, akkor így kellene: ")
sor:str =''
a = input("Kezdjük. Add meg a karaktersorozatot!    :")
for cv in range(len(a)):  #A beírt sorozat végéig ismétli , hogy....
    if a[cv] == 'f':  # Minden egyes elemnél megvizsgálja, hogy egyenlő-é f-fel, 
        sor += 'ph'  #s ha igen, beírja a sor nevű változóba, ahol tároljuk az a sorozat betűit...
    else:
        sor += a[cv]  # ha az elem nem f, akkor beleírja az elemet a sor változóba
print(sor)
print("A tiéd egyszerűbb, elegánsabb - csak kevésbé szólt a for és az if gyakorlásáról - a replace esetében nem kell minden elemen végigmenni...")