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

    #to są metody powiązane z instancją/obiektem
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

    IsOnSale = property(__getIsOnSale, __setIsOnSale, None, 'if set to true, the car is available in sale/promo')

    #metoda klasy pracuje na poziomie klasy, nie instancji, ma dostęp do atrybutów i metod na poziomie klasy
    @classmethod
    def ReadFromText(cls, aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar

    #statyczne nie mają żadnego związku z klasą, tylko się w niej znajduje
    @staticmethod
    def CONVERT_KM_KW(KM):
        return KM * 0.735

    @staticmethod
    def CONVERT_KW_KM(KW):
        return KW*1.36

lineofText = 'Renault:Megane:True:True:False:False'
car_03 = Car.ReadFromText(lineofText)
car_03.getInfo()

print('converting 100 KM to KW',Car.CONVERT_KM_KW(100))
print('converting 90 KM to KW',Car.CONVERT_KW_KM(90))

print(car_03.ReadFromText(lineofText))
print(car_03.CONVERT_KM_KW())