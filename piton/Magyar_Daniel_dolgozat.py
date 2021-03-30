print("Adj meg szavakat amikben van f én kicserélem ph-ra.")
a = str(input("Adj meg karaktersorozatot:   "))
b = "ph"
for cv in range(len(a)):
    print(a.replace("f", b))
    break
