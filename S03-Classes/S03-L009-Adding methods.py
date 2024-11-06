import csv
import types

brandonSale = 'Opel'

def exportToFile_Static(path, header, data):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
        print('>>> This is function exportToFile - static method')

def exportToFile_Class(cls,path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','IsOnSale'])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c. IsOnSale])
        print('>>> This is function exportToFile - class method')

def exportToFile_Instance(self,path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','IsOnSale'])
        writer.writerow([self.brand, self.model, self.IsOnSale])
        print('>>> This is function exportToFile - instance method')


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

    def __getIsOnSale(self):
        return self.__isOnSale

    def __setIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandonSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing sale status to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status isonsale. Sale valid only for {}'.format(brandonSale))

    IsOnSale = property(__getIsOnSale, __setIsOnSale, None, 'if set to true, the car is available in sale/promo')

car_01 = Car('Seat','Ibiza', True,True, True, False)
car_02 = Car('Opel','Corsa', True,False, True, True)

print('Static--------'*10)
Car.ExportToFile_Static = exportToFile_Static
#exportToFile_Static(r"C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\export_static.csv",['Brand','Model','IsOnSale'],[car_01.brand, car_01.model, car_01.IsOnSale])
Car.ExportToFile_Static(r"C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\export_static.csv",['Brand','Model','IsOnSale'],[car_01.brand, car_01.model, car_01.IsOnSale])
print(dir(Car))

print('Class------'*10)
Car.ExportToFile_Class = types.MethodType(exportToFile_Class,Car)
Car.ExportToFile_Class(path = r"C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\export_class.csv")
print(dir(Car))

print('Instance------'*10)
#car_01.ExportToFile_Instance = exportToFile_Instance
car_01.ExportToFile_Instance = types.MethodType(exportToFile_Instance,car_01)
car_01.ExportToFile_Instance(path = r"C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\export_instance.csv")
print(dir(car_01))

print('-'*50)
'''
hasattr(car_01, 'ExportToFile_Instance') — Sprawdza, czy obiekt car_01 posiada atrybut o nazwie 'ExportToFile_Instance'. Funkcja hasattr() zwraca True, jeśli atrybut o tej nazwie istnieje w danym obiekcie; w przeciwnym wypadku zwraca False.

'''
'''
callable(car_01.ExportToFile_Instance) — Jeśli car_01 ma atrybut ExportToFile_Instance, ten zapis sprawdza, czy jest on wywoływalny (czyli czy jest funkcją lub metodą). Funkcja callable() zwraca True, jeśli atrybut można wywołać, co oznacza, że można go użyć jak funkcji (np. car_01.ExportToFile_Instance()), a False w przeciwnym razie.
'''
if hasattr(car_01, 'ExportToFile_Static') and callable(car_01.ExportToFile_Static):
    print("The object has method ExportToFile_Static")
if hasattr(car_01, 'ExportToFile_Class') and callable(car_01.ExportToFile_Class):
    print("The object has method ExportToFile_class")
if hasattr(car_01,'ExportToFile_Instance') and callable(car_01.ExportToFile_Instance):
    print("The object has method ExportToFile_Instance")
if hasattr(car_01,'IsOnSale') and callable(car_01.IsOnSale):
    print("The object has method ExportToFile_Instance")
else:
    print('no such method')

