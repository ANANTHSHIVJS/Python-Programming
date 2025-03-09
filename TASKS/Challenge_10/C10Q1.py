class vehicle:
    def __init__(self,car,bike):
        self.car=car
        self.bike=bike

    def enter(self):
        self.carname=input("Enter the car name : ") 
        self.carmodel=int(input("Enter the model year : "))
        self.bikename = input("Enter the bike name : ")
        self.carmodel = int(input("Enter the model year : "))


class cars(vehicle):
    def c(self):
        print("CAR")
        print("Car names is : ",self.carname)
        print("Car model is : ",self.carmodel)
class bikes(vehicle):
    def b(self):
        print("BIKE")
        print("Bike names is : ",self.bikename)
        print("Bike model is : ",self.bikemodel)

object=vehicle('','')
object.enter()
object.c()
object.b()