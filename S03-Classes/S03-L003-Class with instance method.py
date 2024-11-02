class Car:

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self. isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

    def isDamaged(self):
        return not(self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def getInfo(self):
        #upper zamienia na wielkie litery
        print("{} {}".format(self.brand, self.model).upper())

car_01 = Car('Seat','Ibiza', True,True, True)
car_02 = Car('Opel','Corsa', True,False, True)

print(car_01.brand, car_01.model, car_01.isDamaged())
print(car_02.brand, car_02.model, car_02.isDamaged())

car_01.getInfo()
car_02.getInfo()

print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK, car_01. isMechanicOK)
print(car_02.brand, car_02.model, car_02.isAirBagOK, car_02.isPaintingOK, car_02. isMechanicOK)