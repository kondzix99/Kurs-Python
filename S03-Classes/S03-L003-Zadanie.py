class Cake:

    def __init__(self, product, kind, taste, additives, filling):
        self.product =  product
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

    def show_info(self):
        print(
            "{} - ({}) main taste: {} with additives of {}, filled with {}".format(self.product, self.kind, self.taste,
                                                                                   self.additives, self.filling))
    def set_filling(self, filling_name):
        self.filling = filling_name

    def add_additives(self, additives_list):
        #można też append
         self.additives.extend(additives_list)


Vanilla_Cake = Cake('Vanilla_Cake','cake', 'vanilla', ['chocolade', 'nuts'],'cream')
Chocolade_Muffin = Cake('Chocolade_Muffin','muffin', 'chocolade', ['chocolade'],'')
Super_Sweet_Maringue = Cake('Super_Sweet_Maringue', 'meringue', 'very sweet', [],'')

#bakery_offer = [Vanilla_Cake, Chocolade_Muffin, Super_Sweet_Maringue]
bakery_offer = []
bakery_offer.append(Vanilla_Cake)
bakery_offer.append(Chocolade_Muffin)
bakery_offer.append(Super_Sweet_Maringue)

Chocolade_Muffin.set_filling('cream')
Super_Sweet_Maringue.add_additives(['coconut','cocoa'])

print("TODAY IN OUR OFFER")
for cake in bakery_offer:
    cake.show_info()