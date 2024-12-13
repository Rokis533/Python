import sys
import os

from ..test.test



# viskas = [ 1,1,[2,2,3],1 ]


# viskas = [ 0,1,2,3,4,5,6,7,8,9,10 ]


# #imam nuo 1(imtinai) iki 3(bet ne imtinai)
# # print(viskas[1:3])

# #[start:end:step]
# #[::2]

# print(viskas[:6:2])
# print(viskas[6::3])
# print("----------------------------")


# bum = [5, 6, 15, [5, 58, 21], 2 ]
# print(bum[3][0] + 2)


# input_count = int(input("iveskite kieki saraso elmentu: "))
# sarasas = []


# for i in range(input_count):
#     element = int(input("iveskite elmenta: "))
#     sarasas.append(element)





# print(sarasas)




# sarasas = [1,2,3,4,6]

# sarasas.append(9)
# sarasas.append(8)

# sarasas[0] = 8

# ismestas = sarasas.pop(1)

# sarasas.remove(6)

# print(ismestas)

# sarasas.insert(1,99)
# # 0,1,2,3,4
# #[1,2,3,4,6]

# ilgis = len(sarasas)

# print(sarasas)
# sarasas.sort(reverse=True)

# print(ilgis)
# print(sarasas)

# [1,2,3,4,6]

# for (elementas is saraso) in (sarasas)




# for skaicius in range(99):
#     print(skaicius)

# sarasas.sort(reverse=True)

# for skaicius in sarasas:
#     print(skaicius)


# sarasas_naujas = []

# for skaicius in range(99):
#     sarasas_naujas.append(skaicius)


# print(sarasas_naujas)



# if tekstas.isdigit():
#     print(tekstas)
# print
# is_successfully_converted = False

# while is_successfully_converted == False:
#     try:
#         tekstas = input("tekstas: ")
#         skaicius = int(tekstas)
#         is_successfully_converted = True
#         print("pavyko")

#     except:
#         print("nepavyko")


# studentas1 = {
#     "vardas": "Rokas",
#     "amzius": 99
# }
# studentas2 = {
#     "vardas": "Lukas",
#     "amzius": 23
# }

# studentu_sarasas = [studentas1, studentas2]

# sarasas zodynu

import copy

studentu_sarasas = [
    {
    "vardas": "Rokas",
    "amzius": 99
    }, 
    {
    "vardas": "Lukas",
    "amzius": 32,
    "pazymius": [2,5,6]
    },
    {
    "vardas": "Jonas",
    "amzius": 99
    },  
    {
    "vardas": "Tomas",
    "amzius": 99
    }
]

naujas = copy.deepcopy(studentu_sarasas)

naujas.clear()

print(studentu_sarasas)



# print(studentu_sarasas)

# studentas["pazymiai"] = [9,5,8,6,9]

# print(studentas)

# studentas["pazymiai"] = [5,2]

# print(studentas)

# for (key, value) in studentas.items():
#     print(f'*{key}: {value}*')

# print(studentas)


# list = [1,2,3]


# for naujas in list:
#     print(naujas)

# i = 0

# while i < 5:
#     print(i)
#     i+=1

# tekstas = ""
# is_digit = False

# while not is_digit:
#     tekstas = input("Ivesk skaiciu: ")
#     if tekstas.isdigit():
#         is_digit = True
#     else:
#         print("tai nera skaicius")
    

# for i in range(10):
#     print(i)


# print("---------------")

# for i in range(10):
#     if i == 5:
#         break
#     print(i)


# print("---------------")

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
# else:
#     print("Ciklas baigtas")

