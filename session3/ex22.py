"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""
x=input()
for i in range(0, len(x), 2):
    x=x[i].lower()

print(x)


#nu functioneaza lower