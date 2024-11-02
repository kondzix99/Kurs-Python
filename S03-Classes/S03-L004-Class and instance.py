class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self. isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def isDamaged(self):
        return not(self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def getInfo(self):
        #upper zamienia na wielkie litery
        print("{} {}".format(self.brand, self.model).upper())

print("Przed utworzeniem obiektów: ",Car.numberOfCars, Car.listOfCars)

car_01 = Car('Seat','Ibiza', True,True, True)
car_02 = Car('Opel','Corsa', True,False, True)

print("Po utworzeniu obiektów: ",Car.numberOfCars, Car.listOfCars)

print('Id of class is: ',id(Car))
print('Id of instances are:', id(car_01), id(car_02))
#sprawdzanie czy instancja nalezy do klasy rozne metody
print('Check of object belonges to class:', isinstance(car_01,Car))
print('Check of object belonges to class using type:', type(car_01) is Car)

print('Check class of object using __class__:', car_01.__class__)

print("List of instance attributes with values", vars(car_01))
print("List of class attributes with values", vars(Car))

print("List of instance attributes with values", dir(car_01))
print("List of class attributes with values", dir(Car))

print('Value taken from instance: ', car_01.numberOfCars, 'Value taken from class', Car.numberOfCars)
