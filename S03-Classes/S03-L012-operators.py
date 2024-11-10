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
        print('-' * 20)

    #definicja metody operatora umozliwiajaca wyswietlanie tekstu
    def __str__(self):
        return str(self.kind) + str(self.name) + str(self.additives)

    #definicja metody operatora +=
    def __iadd__(self, other):
        if type(other) == str:
            self.additives.append(other)
            return self
        elif type(other) == list:
            # new_additives = self.additives
            # for i in other:
            #     new_additives.append(i)
            # self.additives =  new_additives
            self.additives.extend(other)
            return self
        else:
            #print("ERROR - BAD TYPE OF ADDITIVE")
            raise Exception("ERROR - BAD TYPE OF ADDITIVE")
        

cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')

#sprawdzenie formatowanie obiektów klasy Cake do postaci tekstu
print(cake01)

#metodę pozwalającą na dodawanie do klasy napisu
cake01 += 'skladnik0'
cake01.show_info()

#metoda skonstruowana tak, aby możliwe było przekazanie na raz większej ilości  dodatków.
cake01 += ['skladnik1','skladnik2']
cake01.show_info()

#zmienne innych typow, zgodnie z oczekiwaniami jest blad
#cake01 += 45