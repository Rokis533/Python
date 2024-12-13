import pickle
import datetime
import os

class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        """
        Bazinė klasė, aprašanti darbuotoją ir jo darbo užmokesčio skaičiavimą.
        Pagal nutylėjimą darbuotojas dirba 7 dienas per savaitę.
        """
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirbo_nuo = dirba_nuo
        self._darbo_dienos_per_sav = 7 # Protected kintamasis, nurodantis darbo dienų skaičių per savaitę
         
    def __paskaiciuoti_dienas(self):
        """
        Privatus metodas, skaičiuojantis kiek dienų darbuotojas dirba.
        """
        today = datetime.datetime.today()
        difference =  today - self.dirbo_nuo
        return difference.days
    
    def paskaiciuoti_atlyginima(self):
        """
        Viešas metodas atlyginimo skaičiavimui.
        """
        dienos = self.__paskaiciuoti_dienas()
        savaites = dienos / 7
        darbo_dienos = savaites * self._darbo_dienos_per_sav
        atlyginimas = darbo_dienos * 8 * self.valandos_ikainis
        return atlyginimas


# Paveldėta klasė normaliam darbo grafikui  
class NormalusDarbuotojas(Darbuotojas):

    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        super().__init__(vardas, valandos_ikainis, dirba_nuo) # Iškviečiame tėvinės klasės konstruktorių
        self._darbo_dienos_per_sav = 5 # Perrašome darbo dienų skaičių į 5



# Pagalbinė funkcija valandinio įkainio įvedimui su klaidų tikrinimu
def valandinio_ivestis():
    while True:
        try:
            valandinis = int(input("Iveskite valandini: "))
            if(valandinis < 0):
                print("ivestas valandinis nera teigiamas")
                continue
            return valandinis
        except:
            print("ivestas valandinis nera sveikas skaicius")
            continue


# Pagrindinis programos vykdymas
darbuotojai = []  # Sukuriame tuščią sąrašą darbuotojams

file_path = "paskaitos/duomenys/darbuotojai.pkl"
if os.path.isfile(file_path):
    # Jei failas egzistuoja, įkrauname ankstesnius duomenis
    with open(file_path, "rb") as failas:
        darbuotojai = pickle.load(failas)


while True:
    vardas = input("Iveskite varda: ")
    if(vardas == "exit"): # Išėjimo sąlyga - įvedus "exit"
        break

    valandinis = valandinio_ivestis()

    darb =  Darbuotojas(vardas, valandinis, datetime.datetime(2024,11,4))
    darbuotojai.append(darb)

    # Išsaugome visus darbuotojus į failą
    with open(file_path, "wb") as failas:
        pickle.dump(darbuotojai, failas)

# Atspausdiname visų darbuotojų informaciją
for darbuotojas in darbuotojai:
    print(darbuotojas.vardas)
    print(darbuotojas.paskaiciuoti_atlyginima())
