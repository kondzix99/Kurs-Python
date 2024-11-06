brandonSale = 'Opel'

class Car:

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self. isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale
    def __getIsOnSale(self):
        return self.__isOnSale

    @property #dekorator do odczytywania
    def IsOnSale(self):
        return self.__isOnSale


    @IsOnSale.setter #dekorator do modyfikowania
    def IsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandonSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing sale status to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status isonsale. Sale valid only for {}'.format(brandonSale))

    @IsOnSale.deleter #dekorator do usuwania
    def IsOnSale(self):
        self.__isOnSale = None

    @property
    def CarTitle(self):
        return "Brand: {}, Model: {}".format(self.brand, self.model).title()


car_01 = Car('Seat','Ibiza',True,True,True,False)
print(car_01.IsOnSale)
car_01.IsOnSale = True
del car_01.IsOnSale
print(car_01.IsOnSale)
print(car_01.CarTitle)