class Cake:

    know_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, product, kind, taste, additives, filling):
        self.product =  product
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

        if (self.kind not in
                # równie dobrze może być zamiast  self CAKE
                self.know_kinds):
            self.kind = 'other'

        #równie dobrze może być zamiast 1 self CAKE
        self.bakery_offer.append(self)

    def show_info(self):
        print(
            "{} - ({}) main taste: {} with additives of {}, filled with {}".format(self.product, self.kind, self.taste,
                                                                                   self.additives, self.filling))
    def set_filling(self, filling_name):
        self.filling = filling_name

    def add_additives(self, additives_list):
        #można też append
         self.additives.extend(additives_list)


cake01= Cake('Vanilla_Cake','cake', 'vanilla', ['chocolade', 'nuts'],'cream')
cake02 = Cake('Chocolade_Muffin','muffin', 'chocolade', ['chocolade'],'')
cake03 = Cake('Super_Sweet_Maringue', 'meringue', 'very sweet', [],'')

cake02.set_filling('cream')
cake03.add_additives(['coconut','cocoa'])

cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')
print(cake04.kind)

print("TODAY IN OUR OFFER")
for cake in Cake.bakery_offer:
    cake.show_info()

print('Check of object belonges to class:', isinstance(cake01,Cake))
print('Check of object belonges to class using type:', type(cake01) is Cake)

#vars() — zwraca słownik atrybutów obiektu wraz z ich wartościami (jeśli obiekt ma atrybuty, które można modyfikować).
print("List of instance attributes with values", vars(cake01))
print("List of class attributes with values", vars(Cake))

#dir() — zwraca listę dostępnych metod i atrybutów obiektu
print("List of instance attributes with values", dir(cake01))
print("List of class attributes with values", dir(Cake))