class Cake:

    def __init__(self, product, kind, taste, additives, filling):
        self.product =  product
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling


Vanilla_Cake = Cake('Vanilla_Cake','cake', 'vanilla', ['chocolade', 'nuts'],'cream')
Chocolade_Muffin = Cake('Chocolade_Muffin','muffin', 'chocolade', ['chocolade'],'')
Super_Sweet_Maringue = Cake('Super_Sweet_Maringue', 'meringue', 'very sweet', '[]','')

#bakery_offer = [Vanilla_Cake, Chocolade_Muffin, Super_Sweet_Maringue]
bakery_offer = []
bakery_offer.append(Vanilla_Cake)
bakery_offer.append(Chocolade_Muffin)
bakery_offer.append(Super_Sweet_Maringue)

print("TODAY IN OUR OFFER")
for cake in bakery_offer:
    print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(cake.product, cake.kind, cake.taste, cake.additives, cake.filling))