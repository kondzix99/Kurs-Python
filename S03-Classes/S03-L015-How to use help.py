class Cake:
    '''
     Cake class for our bakery solution
    '''
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        '''
        :param name: pl nazwa
        :param kind: pl rodzaj
        :param taste: pl smak
        :param additives: pl dodatki
        :param filling: pl wypełnienie
        '''
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

    @property
    def full_name(self):
        '''
        wyswietla nazwe z duzej litery
        '''
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

help(Cake)
print("*"*30)
help(Cake.full_name)