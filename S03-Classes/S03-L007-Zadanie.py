import pickle
import glob

class Cake:

    know_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, product, kind, taste, additives, filling, gluten_free, text):
        self.product =  product
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.__gluten_free = gluten_free
        if self.kind == 'cake' or '':
            self.__text = text
        else:
            self.__text = ''
            print("Nie spelniono warunkow - tekst mozna tylko ustawic dla cake")

        if self.kind not in self.know_kinds:
            self.kind = 'other'

        #równie dobrze może być zamiast 1 self CAKE
        self.bakery_offer.append(self)

    #metody instancji
    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake not for ({})'.format(self.product))

    #definiowanie właściwości property
    Text = property(__get_text, __set_text,  None, 'Text on the cake')

    def show_info(self):
        print(
            "{} - ({}) main taste: {} with additives of {}, filled with {} and gluten_free is {} and text is ({})".format(self.product, self.kind, self.taste,
                                                                                   self.additives, self.filling, self.__gluten_free, self.__text))
    def set_filling(self, filling_name):
        self.filling = filling_name

    def add_additives(self, additives_list):
        #można też append
         self.additives.extend(additives_list)

    def save_to_file(self, path):
        #wb - zapisz binarny
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    #metoda klasy
    @classmethod
    def read_from_file(cls, path):
        # rb - odczytaj binarny
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        #dodaje nowe ciastko do klasy
        cls.bakery_offer.append(new_cake)
        return new_cake

    #metoda statyczna
    @staticmethod
    #zwraca pliki z rozszerzeniem bakery
    def get_bakery_files(catalog_name):
        return glob.glob(catalog_name+'/*.bakery')

cake01= Cake('Vanilla_Cake','cake', 'vanilla', ['chocolade', 'nuts'],'cream', False, 'ciasteczko')
cake02 = Cake('Chocolade_Muffin','muffin', 'chocolade', ['chocolade'],'', False, 'czekoladka')
cake03 = Cake('Super_Sweet_Maringue', 'meringue', 'very sweet', [],'', True,'mufinka')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, 'wafelek')

print("TODAY IN OUR OFFER")
for cake in Cake.bakery_offer:
    cake.show_info()

cake01.save_to_file(r"C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\cake01.bakery")
cake02.save_to_file(r"C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\cake02.bakery")

cake05 = Cake.read_from_file(r"C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\cake01.bakery")
cake05.show_info()

print(Cake.get_bakery_files(r"C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki"))
