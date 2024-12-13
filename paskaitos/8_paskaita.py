# tekstas = "2020-12-05"

# metai, menesiai, dienos = map(int, tekstas.split("-"))

# print(metai)
# print(menesiai)
# print(dienos)

# tekstas = "vienas du trys"

# pirmas, antras, trecias = map(str, tekstas.split(" "))

# print(pirmas)
# print(antras)
# print(trecias)

# sarasas = [4561,564,8564,564,8964,8949,84,3,123,5,984,98]
# isfiltruotas_sarasas = filter(lambda x : x % 2 == 0 and x < 1000, sarasas )

# print(list(isfiltruotas_sarasas))
# import calendar

# sarasas = range(1970, 2024)
# isfiltruotas_sarasas = filter(lambda x: not calendar.isleap(x), sarasas )

# print(list(isfiltruotas_sarasas))

# from functools import reduce


# sarasas = [1,2,3,4,5]
# #Pirma iteracija x = 1, y = 2,     return 1 + 2 ( x + y) =3
# #Antra iteracija x = 3, y = 3,     return 3 + 3 ( x + y) = 6
# #Trecia iteracija x = 3, y = 4,     return 6 + 4 ( x + y) = 10
# #Ketvirta iteracija x = 4, y = 5,     return 10 + 5 ( x + y) = 15
# # result = 15

# isfiltruotas_sarasas = reduce(lambda x, y: x * y, sarasas)

# print(isfiltruotas_sarasas)
# def naujas_sarasas_daugiau_nei_trys_ir_padalinta_is_dvieju(sarasas):
#     naujas = []
#     for elementas in sarasas:
#         if elementas > 3:
#             naujas.append(elementas/2)

#     return naujas


# sarasas = [1,2,3,4,5]


# naujas_sarasas = [elementas/2 for elementas in sarasas if elementas > 3 ]

# print(naujas_sarasas)

# sarasas = [ int, int, Bool, str, float ]
# sarasas = [ 1, 5, True, "Rokas", 2.3 ]

# sarasas_tik_skaiciai = [type(x) is int for x in sarasas ]
# print(sarasas)
# print(sarasas_tik_skaiciai)
# suma = sum(sarasas_tik_skaiciai)
# print(suma)

# sarasas = [ 1, 5, True, "Rokas", 2.3 ]

# sarasas_tik_tekstas, sarasas_tik_skaiciai = [type(x) is str for x in sarasas ], [type(x) is int for x in sarasas ]
# print(sarasas)
# print(sarasas_tik_tekstas)
# print(sarasas_tik_skaiciai)
# suma = sum(sarasas_tik_skaiciai)
# print(suma)


# sarasas = [4561,564,8564,564,8964,8949,84,3,123,5,984,98]

# print(sarasas)

# sarasas.sort(reverse= True)
# naujas = sorted(sarasas, reverse= True)


# print(naujas)


# zodynas = {
#     "Vardas": "Rokas", 
#     "Amzius": 21, 
#     "Gimimo metai": 1999
#     }

# rikiuotas_sarasas = sorted(zodynas, reverse=True)

# print(rikiuotas_sarasas)

# sarasas = [-1, 28, 68, 1, -15, 1, -5]

# def rikiavimas_paprastai(zodis):
#     return  zodis

# def pagal_ar_pirma_raide_balse(zodis):
#     balses = "aeuioAEUIO"
#     if zodis[0] in balses:
#         return (0, zodis)
    
#     return (1, zodis)

# # (1), (0), (1), (0)
# #  ["Rokas",    "Egidijus",    "Jeronimas",     "Orijus"]
# # (1,"Rokas"), (0,"Egidijus"), (1,"Jeronimas"), (0,"Orijus")

# # kitas žingsnis rušiuojam pagal skaiciu tai yra tik pagal 1 arba 0
# # (0,"Egidijus"), (0,"Orijus"),(1,"Rokas"), (1,"Jeronimas")

# # kitas žingsnis rušiuojam pagal antra tuble reikšme tai yra pagal abecele
# # (0,"Egidijus"), (0,"Orijus"),(1,"Jeronimas"),(1,"Rokas")



# #           1           1           1           0       0           1       1       0       1           1       1
# #         ["Rokas", "Jeronimas", "Sabonis", "Orijus","Egidijus", "Jonas","Tome", "Antany", "Juozas","Zenius", "Diana"]

# sarasas = ["Rokas", "Jeronimas", "Jeronimas", "Jeronimas", "Sabonis", "Orijus","Egidijus", "Jonas","Tome", "Antany", "Juozas","Zenius", "Diana"]

# # naujas = sorted(sarasas, key=lambda x: x[-1] != "s" )

# # naujas = sorted(sarasas, key=lambda x: (x[0], len(x)) )

# naujas = sorted(sarasas, key=pagal_ar_pirma_raide_balse )
# print(naujas)

class Phone:
    def __init__(self, manifacturer, camera):
        self.manifacturer = manifacturer
        self.camera = camera

    def __str__(self):
        return f"{self.manifacturer}, {self.camera}"


telefonas1 = Phone("Nokia", "3MP")
telefonas2 = Phone("Samsung", "48MP")
telefonas3 = Phone("Apple", "48MP")

sarasas = [telefonas1, telefonas2, telefonas3]

naujas = sorted(sarasas, key=lambda x: x.camera)

for telef in naujas:
    print(telef)



