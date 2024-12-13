import random
import json

class Phone:
    def __init__(self, manifacturer, camera):
        self.manifacturer = manifacturer
        self.camera = camera


class Car:
    def __init__(self, colorYO:str, speed:int = 0, history_of_repair:list[str] = []):
        self.color:str = colorYO
        self.speed:int = speed
        self.history_of_repair:list[str] = history_of_repair

    def __str__(self):
        return f"STR:{self.speed} {self.color} lalalalal {self.history_of_repair} {self.get_speed_in_miles()}"
    
    def __repr__(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)
    
    def get_speed_in_miles(self) -> float:
        return self.speed / 1.6

    def repaint(self, new_color):
        self.color = new_color

    def add_repair_to_history(self, repair_record : str):
        self.history_of_repair.append(repair_record)

    def drive(self):
        try:
            sounds = ["Wrroom", "Kleklekle", "bzzzzzzzz"]
            for i in range(10):
                index = random.randint(0 ,3)
                print(sounds[index])
        except:
            print("stop")

    
    # def __str__(self):
    #     all_properties = []
    #     for prop  in dir(self):
    #         if(not prop.startswith("__")):
    #             all_properties.append(self.__getattribute__(prop))

    #     return f"{all_properties}"





telefonas = Phone("Nokia", "3MP")
telefonas2 = Phone("Samsung", "48MP")

car_history = ["Oil change", "Trasmition change", "Tire change"]

masina = Car("Melyna", 280, car_history)
masina2 = Car("Raudona", history_of_repair=car_history)
masina3 = Car("Geltona", 160)
masina4 = Car("Rozine", 77)





masina2.add_repair_to_history("Engine failiure")
masina2.add_repair_to_history("Screen broken")
masina2.add_repair_to_history("Broken tire")

try:
    masina2.engine = "4.2L"
except:
    pass

masina2.drive()


print(masina2)

print(id(masina2))
print(type(masina2))


print(masina2.get_speed_in_miles())


# list_cars : list[Car] = []
# list_cars.append(masina)
# list_cars.append(masina2)
# list_cars.append(masina3)
# list_cars.append(masina4)

# for car in list_cars:
#     print(car.color)
#     print(car.speed)
#     print(car.get_speed_in_miles())