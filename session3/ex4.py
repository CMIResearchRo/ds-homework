"""
    Ex. 4: Modificati urmatoarea bucata de cod astfel incat
    la rulare, lista rezultata sa fie [1, 2, 2, 3, 4, 5]
"""

# In variabila t1 vom stoca un tuplu cu 2 elemente, 1 si 2
# iar in variabila t2 vom stoca un tuplu cu 3 element 3, 4, 5
t1 = (1, 2)
t2 = (3, 4, 5)

# Vom crea variabila l1 iar ca si valoare, va avea o lista compusa din
# concatenarea celor 2 tupluri. Primele elemente vor fi cele din l1.
# Vom converti cele 2 tupluri in liste, inainte sa le concatenam
x=list(t1)
x.append(2)
l1 = x + list(t2)

# Afisam lista
print(l1)