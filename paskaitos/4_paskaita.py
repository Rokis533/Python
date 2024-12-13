# def fibonaci(index):
     
#      if (index <= 0):
#           return 0
     
#      if(index == 1):
#           return 1
     
#      return fibonaci(index-1) + fibonaci(index -2)


# skaicius = fibonaci(6)
# print(skaicius)

#indexai = 0,1,2,3,4,5,6
#skaiciai fibo = 0,1,1,2,3,5,8 


# ========================================================================================
# ========================================================================================
# ========================================================================================
# ========================================================================================


# def paduginta_is_saves(skaicius):
#     return skaicius * skaicius

# paduginta_is_saves_lambda = lambda skaicius: skaicius * skaicius


# sarasas = [2,5,6,52,45,5,45,6,45]

# #atitikmuo mapo -->  nauja_sarasas = list(map(lambda skaicius: skaicius * skaicius, sarasas))
# nauja_sarasas = []
# for sk in sarasas:
#     naujas_sk = paduginta_is_saves(sk)
#     nauja_sarasas.append(naujas_sk)


# print(nauja_sarasas)

# nauja_sarasas = list(map(lambda skaicius: skaicius * skaicius, sarasas))

# print(nauja_sarasas)

# ========================================================================================
# ========================================================================================
# ========================================================================================
# ========================================================================================
# def is_even(skaicius):
#     return skaicius % 2 == 0



# sarasas = [2,5,6,52,45,5,45,6,45]
# print(sarasas)

# nauja_sarasas_lyginis = []
# # nauja_sarasas_nelyginis = []
# for sk in sarasas:
#     if(is_even(sk)):
#         nauja_sarasas_lyginis.append(sk)


# print(f"Lyginis: {nauja_sarasas_lyginis}")
# print(f"Nelyginis: {nauja_sarasas_nelyginis}")

# ar_lyginis = lambda skaicius: skaicius % 2 == 0

# lyginis_nauja_sarasas = list(filter(lambda skaicius: skaicius % 2 == 0, sarasas))

# nauja_sarasas_daugiau_nei_18 = list(filter(lambda skaicius: skaicius > 18 and skaicius < 50, sarasas))

# print(f"NELYGINIS: {lyginis_nauja_sarasas}")

# ========================================================================================
# ========================================================================================
# ========================================================================================
# ========================================================================================
# skaiciai = [-2,-5,-6,52,45,5,45,6,45, -10]

# nauji_skaiciai = []

# for x in skaiciai:
#     if x > 0:
#         nauji_skaiciai.append(x)
#     else:
#         nauji_skaiciai.append(0)

# print(f"nauji_skaiciai: {nauji_skaiciai}")

# rezultatas = [x if x > 0 else 0 for x in skaiciai]


# print(f"rezultatas:     {rezultatas}")

# ========================================================================================
# ========================================================================================
# ========================================================================================
# ========================================================================================
# skaiciai = [-2,-5,-6,52,45,5,45,6,45, -10]

# nauji_skaiciai = []

# for x in skaiciai:
#     if x % 2 == 0:
#         nauji_skaiciai.append(x)

# print(f"nauji_skaiciai: {nauji_skaiciai}")

# rezultatas = [x for x in skaiciai if x % 2 == 0]


# print(f"rezultatas:     {rezultatas}")

# ========================================================================================
# ========================================================================================
# ========================================================================================
# ========================================================================================

nauji_skaiciai = []

for i in range(1,5):
    for j in range(1,3):
        nauji_skaiciai.append( i + j )
        print(f"i:{i} j:{j} = {i + j}")

print(f"nauji_skaiciai: {nauji_skaiciai}")

# rezultatas = [99,999,99]
# rezultatas.extend([i + j for i in range(1,5) for j in range(1,3)])

rezultatas = [i + j for i in range(1,5) for j in range(1,3)]


print(f"rezultatas:     {rezultatas}")