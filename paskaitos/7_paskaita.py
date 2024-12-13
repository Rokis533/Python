import os
import this
file_path = "tekstai/tekstas.txt"

with open(file_path, "r", encoding="UTF-8") as dialogo_failas:
    print(dialogo_failas.read(10))
    print(dialogo_failas.read(50))

# with open(file_path, "r", encoding="UTF-8") as dialogo_failas:
#     for eilute in dialogo_failas.readlines():
#         print(eilute, end="")

# with open(file_path, "w", encoding="UTF-8") as dialogo_failas:
#     dialogo_failas.write("Labas" + "\n")
#     dialogo_failas.seek(0)
#     dialogo_failas.write("Ne" + "\n")
    

# with open(file_path, "a+", encoding="UTF-8") as dialogo_failas:
#     while True:
#         tekstas = input("Iveskite: ")
#         if(tekstas == "exit"):
#             break
#         dialogo_failas.write(tekstas + "\n")

#     dialogo_failas.seek(0)
#     print(dialogo_failas.read())
    



# print("-------------------------------")
# with open(file_path, "r") as dialogo_failas:
#     print(dialogo_failas.read())
    


# failas = open("C:/CodeAcademy/AIU3/Python/tekstas2.txt", "w")
# while True:
#     tekstas = input("Iveskite: ")
#     if(tekstas == "exit"):
#         break
#     failas.write(tekstas + "\n")

    
# failas.close()