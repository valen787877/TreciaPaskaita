# Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.
from hmac import new

for i in range(10):
    print("labas")

# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.

for i in range(10):
    print(i)

# Sukurkite masyvą iš dešimties augalų pavadinimų.

augalai = ["rope" , "svogunas" , "ridikas" , "kukuruzas" , "piene" , "agurkas" , "braske" , "kaktusas" ,
           "citrina" , "berzas"]
print(augalai)

# Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.

# print(augalai)
for i in augalai:
    print(i)

# Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir
# baigiant pirmuoju. (atvirkščias ciklas).

# for i in augalai:
print(augalai[::-1])

# Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);

# for i in range(51):
#     print(i)
#     print([::1])
#     # print([10:50:2])

for i in range(10, 51, 2):
    print(i)

# Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi
# iš 10 be liekanos jo nespausdinkite. ( naudokite continue.) (atspausdinti visus porinus
# skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)

for i in range(10, 51, 2):
    if i % 10 == 0:
        continue
    print(i)

# Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i
# turėjo porinę reikšmę;

kiekis = 0

for i in range(21):
    print(i)
    if i % 2 == 0:
        kiekis += 1

print("Poriniu skaiciu kiekis:", kiekis)


# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai,
# ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)



trumpesni_nei_5 = 0
ilgesni_nei_7 = 0

augalai = ["rope" , "svogunas" , "ridikas" , "kukuruzas" , "piene" , "agurkas" , "braske" , "kaktusas" ,
           "citrina" , "berzas"]

for zodis in augalai:
    if len(zodis) < 5:
        trumpesni_nei_5 += 1
    if len(zodis) > 7:
        ilgesni_nei_7 +=1

print("Trumpesni nei 5:", trumpesni_nei_5)
print("Ilgesni nei 7:", ilgesni_nei_7)

# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių
# nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)



augalai = ["rope" , "svogunas" , "ridikas" , "kukuruzas" , "piene" , "agurkas" , "braske" , "kaktusas" ,
           "citrina" , "berzas"]
kiekis = 0

for zodis in augalai:
    if  5 < len(zodis) < 10:
        kiekis += 1

print("Zodziu kiekis:", kiekis)

#Sunkesni

# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus
# tarpais vienoje eilutėje ir suskaičiuokite kiek tarp jų yra didesnių už 150.  Skaičiai
# didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.


import random

kiek_didesniu_nei_150 = 0
rezultatas = ""

for _ in range(300):
    x = random.randint(0, 300)

    if x > 150:
        kiek_didesniu_nei_150 += 1

    if x > 275:
        rezultatas += f"[{x}] "
    else:
        rezultatas += str(x) + " "

print(rezultatas)
print("Didesniu nei 150 skaiciu kiekis:", kiek_didesniu_nei_150)


# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos.
# Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.

# pirmas = True
#
# for i in range(1, 3001):
#     if i % 77 == 0:
#         if pirmas:
#             print(i, end="")
#             pirmas = False
#         else:
#             print(", " + str(i), end="")

pirmas = True

for i in range(1, 3001):
    if i % 77 != 0:
        continue
    if pirmas:
        print(i, end="")
        pirmas = False
    else:
        print(", " + str(i), end="")

# Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.

for _ in range(25):
    print("*" * 25)

# Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.

dydis = 25

for ei in range(dydis):
    eilute = ""
    for st in range(dydis):
        if ei == st or ei + st == dydis - 1:
            eilute += "x"
        else:
            eilute += "*"
    print(eilute)

# Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas,
# o 1 - skaičius. Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito
# skaičius ir “H” jeigu herbas. Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;

import random

while True:
    m = random.randint(0, 1)
    if m == 0:
        print("h")
        break
    else:
        print("s")

###################################

import random

herbai = 0

while herbai < 3:
    m = random.randint(0, 1)
    if m == 0:
        print("h")
        herbai += 1
    else:
        print("s")
########################################

# import random
#
# is_eiles = 0
#
# while is eiles < 3:
#     m = random.randint(0, 1)







# Reikia nupaišyti pilnavidurį rombą, taip pat, kaip ir pilnavidurį kvadratą , kurio aukštis 21 eilutė.


# Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29), kurių reikšmės yra atsitiktiniai
# skaičiai nuo 5 iki 25.


# import random
#
# masyvas = []
# for i in range(30):
#     print(i)
#     random.randint()

import random

masyvas = [
    random.randint(5, 25 )
    for _ in range(30)
]
print(masyvas)

# Suskaičiuokite kiek masyve yra reikšmių didesnių už 10

x = len(masyvas)

print(x)

kiek = 0

for y in masyvas:
    if y > 10:
        kiek += 1

print("Didesni nei 10,", kiek)
#
# Raskite didžiausią masyvo reikšmę;

# import random
#
# masyvas = [
#     random.randint(5, 25 )
#     for _ in range(30)
# ]
# print(masyvas)
didziausias_sk = max(masyvas)

print("Didziausias sk,", didziausias_sk)

# Suskaičiuokite visų reikšmių sumą;


print(sum(masyvas))


# Sukurkite naują masyvą, kurio reikšmės yra 1 uždavinio masyvo reikšmes minus tos reikšmės indeksas;

import random

masyvas = [
    random.randint(5, 25 )
    for _ in range(30)
]
print(masyvas)
# a = len(masyvas)
b = enumerate(masyvas)
print(list(b))

masyvas2 = []

for ind, reiksm in enumerate(masyvas):
    masyvas2.append(reiksm - ind)

print(masyvas2)


# Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25, kad bendras masyvas
# padidėtų iki indekso 39;

import random

masyvas = [
    random.randint(5, 25 )
    for _ in range(30)
]


for _ in range(10):
    masyvas.append(random.randint(5, 25 ))

print("po,", len(masyvas), masyvas)


import random

masyvas = [random.randint(5, 25 ) for _ in range(30)]
for _ in range(10):
    masyvas.append(random.randint(5, 25 ))

print("po to,", len(masyvas), masyvas)


# Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių
# indekso reikšmių, o kitas iš porinių;


poriniai = []
neporiniai = []

for i in range(len(masyvas)):
    if i % 2 == 0:
        poriniai.append(masyvas[i])
    else:
        neporiniai.append(masyvas[i])
print("poriniai indeksai:", poriniai)
print("neporiniai indeksai", neporiniai)

#############################################
poriniai = []
neporiniai = []

for i, x in enumerate(masyvas):
    if i % 2 == 0:
        poriniai.append(x)
    else:
        neporiniai.append(x)

# Masyvo elementus su poriniais indeksais padarykite lygius 0 jeigu jie didesni už 15;

for i in range(len(masyvas)):
    if i % 2 == 0 and masyvas[i] > 15:
        masyvas[i] = 0

print(masyvas)


# Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10;

indeksas = -1  # jeigu liktu -1 , reiskia nieko nerado

for i in range(len(masyvas)):
    if masyvas[i] > 10:
        indeksas = i
        break  #####suranda pirma, o ne paskutine

print("Pirmas indeksas, kur reiksme > 10:", indeksas)

################################

indeksas = -1

for i, x in enumerate(masyvas): # duoda poras
    if x > 10:            #kai randa x > 10 , issaugo i ir nutraukia cikla
        indeksas = i
        break

print("Pirmas indeksas, kur reiksme > 10:", indeksas)


# Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D, o ilgis 200.
# Suskaičiuokite kiek yra kiekvienos raidės.

import  random

raides = ["A", "B", "C", "D"]
masyvas = [random.choice(raides) for _ in range(200)]

print(masyvas)

print("A:", masyvas.count("A"))
print("B:", masyvas.count("B"))
print("C:", masyvas.count("C"))
print("D:", masyvas.count("D"))


# Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.

naujas = sorted(masyvas) #sukuria nauja surusiuota masyva

print(naujas)

# Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes.
# (turi gautis masyvas, kurio elementai, kaip pvz atrodo taip: “AAB”, “CBC”, “DDA”, 200 reikšmių).
# Paskaičiuokite kiek skirtingų reikšmių kombinacijų gavote.

import random

raides = ["A", "B", "C", "D"]

mas1 = [random.choice(raides) for _ in range(200)]
mas2 = [random.choice(raides) for _ in range(200)]
mas3 = [random.choice(raides) for _ in range(200)]

kombinacijos = [a + b + c for a, b, c in zip(mas1, mas2, mas3)]
#               suklijuoja i viena stringa. tada paima po viena elementa tuo paciu indeksu
print(kombinacijos)

skirtingu_kiekis = len(set(kombinacijos)) # palieka tik unikalias kombinacijas

print("Skirtingu kombinaciju:", skirtingu_kiekis)


# Sugeneruokite du masyvus, kurių reikšmės yra atsitiktiniai skaičiai nuo 100 iki 999.
# Masyvų ilgiai 100. Masyvų reikšmės turi būti unikalios savo masyve (t.y. neturi kartotis).

import random

masyvas1 = random.sample(range(100, 1000), 100) # k100 yra masyvo ilgis
masyvas2 = random.sample(range(100, 1000), 100) # sample-nesikartojantys elementai

print("Pirmas masyvas:")
print(masyvas1)

print("\nAntras masyvas:")
print(masyvas2)

print("\nUnikalus 1 masyve:", len(set(masyvas1)) == len(masyvas1))
print("\nUnikalus 2 masyve:", len(set(masyvas2)) == len(masyvas2))


# Sugeneruokite masyvą, kuris būtų sudarytas iš reikšmių, kurios yra pirmame 6 uždavinio masyve,
# bet nėra antrame 6 uždavinio masyve.

naujas = []

for x in masyvas1:
    if x not in masyvas2:
        naujas.append(x)

print(naujas)

# Sugeneruokite masyvą iš elementų, kurie kartojasi abiejuose 6 uždavinio masyvuose.

bendri = []

for x in masyvas1:
    if x in masyvas2:
        bendri.append(x)

print("Bendri elementai:", bendri)
print("Kiek bendru:", len(bendri))

##############################


bendri = list(set(masyvas1) & set(masyvas2))#set(masyvas1) pavercia i aibe; & -kas bendra

print("Bendri elementai:", bendri)
print("Kiek bendru:", len(bendri))

# Sugeneruokite 10 skaičių masyvą pagal taisyklę: Du pirmi skaičiai- atsitiktiniai nuo 5 iki 25.
# Trečias, pirmo ir antro suma. Ketvirtas- antro ir trečio suma. Penktas trečio ir ketvirto suma ir t.t.


import random

masyvas = []

masyvas.append(random.randint(5, 25))
masyvas.append(random.randint(5, 25))

for i in range(2, 10):
    masyvas.append(masyvas[i-1] + masyvas[i-2]) # i yra dabartinis index, i-1 yra buves, i-2 dar pries tai

print(masyvas)
#