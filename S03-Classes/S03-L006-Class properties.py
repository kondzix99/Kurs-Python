brandonSale = 'Opel'

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

    #ukrywamy funkcje getIsOnSale on setIsOnSale przez dodanie __
    def __getIsOnSale(self):
        return self.__isOnSale

    def __setIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandonSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing sale status to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status isonsale. Sale valid only for {}'.format(brandonSale))

#Funkcja property() przyjmuje cztery argumenty:
# fget: Funkcja, która zwraca wartość atrybutu (getter).
# fset: Funkcja, która ustawia wartość atrybutu (setter).
# fdel: Funkcja, która usuwa atrybut (deleter).
# doc: Opcjonalny opis właściwości.

    IsOnSale = property(__getIsOnSale, __setIsOnSale, None, 'if set to true, the car is available in sale/promo')


car_01 = Car('Seat','Ibiza', True,True, True, False)
car_02 = Car('Opel','Corsa', True,False, True, True)

# print("Status of cars: ", car_01.__getIsOnSale(), car_02.__getIsOnSale())
# car_01.setIsOnSale(True)
# car_02.setIsOnSale(False)
# print("Status of cars: ", car_01.getIsOnSale(), car_02.getIsOnSale())

car_01.IsOnSale = True
car_02.IsOnSale = True
print("Status of cars: ", car_01.IsOnSale, car_02.IsOnSale)