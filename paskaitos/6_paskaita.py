import datetime

class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirbo_nuo = dirba_nuo
        self._darbo_dienos_per_sav = 7
         
    def __paskaiciuoti_dienas(self):
        today = datetime.datetime.today()
        difference =  today - self.dirbo_nuo
        return difference.days
    
    def paskaiciuoti_atlyginima(self):
        dienos = self.__paskaiciuoti_dienas()
        savaites = dienos / 7
        darbo_dienos = savaites * self._darbo_dienos_per_sav
        atlyginimas = darbo_dienos * 8 * self.valandos_ikainis
        return atlyginimas
    
class NormalusDarbuotojas(Darbuotojas):

    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        super().__init__(vardas, valandos_ikainis, dirba_nuo)
        self._darbo_dienos_per_sav = 5



# darbuotojas = Darbuotojas("Rokas", 10, datetime.datetime(2024,11,4))
# print(darbuotojas.paskaiciuoti_atlyginima())

# darbuotojas_normalus = NormalusDarbuotojas("Jonas", 10, datetime.datetime(2024,11,4))
# print(darbuotojas_normalus.paskaiciuoti_atlyginima())
def valandinio_ivestis():
    while True:
        try:
            valandinis = int(input("Iveskite valandini: "))
            if(valandinis > 0):
                print("ivestas valandinis nera teigiamas")
                continue
            return valandinis
        except:
            print("ivestas valandinis nera sveikas skaicius")
            continue


darbuotojai = []
while True:
    vardas = input("Iveskite varda: ")
    if(vardas == "exit"):
        break

    valandinis = valandinio_ivestis()

    darb =  Darbuotojas(vardas, valandinis, datetime.datetime(2024,11,4))
    darbuotojai.append(darb)

for darbuotojas in darbuotojai:
    print(darbuotojas.paskaiciuoti_atlyginima())