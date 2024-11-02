class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self. isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        #taki zapis __ umożliwia że nie zmodyfikujemy tej zmiennej
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def isDamaged(self):
        return not(self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def getInfo(self):
        #upper zamienia na wielkie litery
        print("{} {}".format(self.brand, self.model).upper())
        print("IS ON SALE      {}".format(self.__isOnSale))
        print("-"*20)

car_01 = Car('Seat','Ibiza', True,True, True, False)
car_02 = Car('Opel','Corsa', True,False, True, True)

#car_02.isOnSale = False
car_02._Car__isOnSale = False
car_02.YearProduction = 2005
del car_02.YearProduction

#dodanie nowej wlasciwosci do obiektu
setattr(car_02, 'TAXI', False)
#sprawdza czy obiekt posiada dany atrybut
print(hasattr(car_02,'TAXI'))
#usuwanie atrubytu
delattr(car_02,'TAXI')
print(hasattr(car_02,'TAXI'))

car_02.getInfo()
print(vars(car_02))