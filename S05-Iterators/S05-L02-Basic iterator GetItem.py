class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __getitem__(self, item):
        if item <= (len(self.products) * len(self.promotions) * len(self.customers)):
            pos_products = item // (len(self.promotions)*len(self.customers))
            item %= len(self.promotions)*len(self.customers)
            pos_promotions = item // len(self.customers)
            item %= len(self.customers)
            pos_customers = item
        else:
            raise StopIteration

        return "{} - {} -{}".format(self.products[pos_products],
                                              self.promotions[pos_promotions],
                                              self.customers[pos_customers])


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 5)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)

#for i in range(0, 31):
#print(i, combinations[i])

#combinations iterator
it = iter(combinations)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

print("-"*30)

for c in combinations:
    print(c)
