sarasas = []
for x in range (0,8):
    sarasas.append(x)
 
# sarasas = list(range(0,51))
 
print(f"Skaiciu sarasas: \n{sarasas}")
 
# naujas_sarasas = []
# for skaicius in sarasas:
#     naujas_sarasas.append(skaicius * 10)
 
 
naujas_sarasas = list(map(lambda x: x * 10, sarasas))

 
print(f"Skaiciu naujas_sarasas: \n{naujas_sarasas}")
print(f"Skaiciu naujas_sarasas: \n{naujas_sarasas}")













# print(f"Naujas skaiciu sarasas, kuriame visi skaiciai padauginti is 10: \n{naujas_sarasas}")
 
# naujas_sarasas2 = filter(lambda x : x % 7 == 0, naujas_sarasas)
 
# print(f"Naujas skaiciu sarasas, kuriame tik skaiciai, kurie dalinasi is 7: \n{list(naujas_sarasas2)}")