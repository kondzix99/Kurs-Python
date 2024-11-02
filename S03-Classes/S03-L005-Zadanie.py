class Cake:

    know_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, product, kind, taste, additives, filling, gluten_free):
        self.product =  product
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.__gluten_free = gluten_free

        if self.kind not in self.know_kinds:
            self.kind = 'other'

        #równie dobrze może być zamiast 1 self CAKE
        self.bakery_offer.append(self)

    def show_info(self):
        print(
            "{} - ({}) main taste: {} with additives of {}, filled with {} and gluten_free is {}".format(self.product, self.kind, self.taste,
                                                                                   self.additives, self.filling, self.__gluten_free))
    def set_filling(self, filling_name):
        self.filling = filling_name

    def add_additives(self, additives_list):
        #można też append
         self.additives.extend(additives_list)


cake01= Cake('Vanilla_Cake','cake', 'vanilla', ['chocolade', 'nuts'],'cream', False)
cake02 = Cake('Chocolade_Muffin','muffin', 'chocolade', ['chocolade'],'', False)
cake03 = Cake('Super_Sweet_Maringue', 'meringue', 'very sweet', [],'', True)
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False)

print("TODAY IN OUR OFFER")
for cake in Cake.bakery_offer:
    cake.show_info()
print("-"*100)

cake03.__gluten_free = False # w ten sposób nie zmodyfikujemy bezy na glutenową, wartość i tak TRUE
print(vars(cake03))
cake03.show_info()

print("-"*20)

cake03._Cake__gluten_free = False # ale w ten sposób już zmodyfikujemy bezę na glutenową, wartość FALSE
print(vars(cake03))
cake03.show_info()