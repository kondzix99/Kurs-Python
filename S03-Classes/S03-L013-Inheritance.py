class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        #print('-' * 20)

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

class SpecialCake(Cake):
    def __init__(self,  name, kind, taste, additives, filling, occasion, shape, ornament, text):
        #funkcja super jakgdyby kopiuje atrubuty z klasy rodzica
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornament = ornament
        self.text = text

    def show_info(self):
        #funckja super kopiuje metodę show info z klasy rodzica
        super().show_info()
        print("occasion:    {}".format(self.occasion))
        print("shape:       {}".format(self.shape))
        print("ornament:    {}".format(self.ornament))
        print("text:        {}".format(self.text))

birthday = SpecialCake('Vanilla Cake','cake', 'vanilla', ['chocolate', 'nuts'], 'cream',
                       'birthday', 'standard', 'hearts', '15')
wedding  = SpecialCake('Vanilla Cake','cake', 'vanilla', ['whipped cream', 'coconut shirms'], 'strawberries cream',
                       'wedding', 'pyramid', 'pigeons', 'Patricia & Tom')

#birthday.show_info()
# print("\n"+"-"*30 +"\n")
# wedding.show_info()

for object in SpecialCake.bakery_offer:
    print(object.full_name)
    object.show_info()