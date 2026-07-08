class Car :                                         # Basic class and object
    total_cars = 0
    def __init__(self,brand,model):
        self.__brand  = brand                       # Encapsulation  __brand and __getstate__ so user cant access brand directly but through a diff method.
        self.model = model
        Car.total_cars += 1

    def __getstate__(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model} {self.fuel_type()}"

    def fuel_type(self):
        return "Petrol or Diesel"

my_car = Car("Land Rover","Defender")
new_car = Car("Bugatti" ,"Chiron")
print(new_car.full_name())
print(my_car.full_name())

print(Car.total_cars)

# class ElectricCar(Car):                             # Inheritance
#     def __init__(self,__brand,model,battery):
#         super().__init__(__brand,model)
#         self.battery = battery
#
#     def full_name(self):
#         return f" {self.model} {self.battery} {self.fuel_type()}"
#
#     def fuel_type(self):                           # Polymorphism - one method and object can work diff in tow diff places
#         return "Electric"



# ev = ElectricCar("Tesla","S5","85Kwh")
# print(ev.__getstate__())
# print(ev.full_name())
