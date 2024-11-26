'''
Funkcja yield w Pythonie jest używana do tworzenia generatorów – specjalnych funkcji, które zwracają wartości po jednej na raz, zamiast zwracać całą kolekcję od razu.
Dzięki temu umożliwia oszczędność pamięci i bardziej efektywne przetwarzanie danych w przypadku dużych zbiorów.

Jak działa yield?
yield zatrzymuje wykonanie funkcji, „zapamiętując” jej aktualny stan.
Przy kolejnym wywołaniu generatora, wykonanie funkcji wznawia się od miejsca, w którym zostało przerwane przez yield.
Funkcja z yield zwraca obiekt typu generator zamiast zwykłej wartości.

'''

def Combinations(products, promotions, customers):
    for i in products:
        for j in promotions:
            for k in customers:
                yield "{} - {} -{}".format(i,j,k)

products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1,3)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

combinations = Combinations(products, promotions, customers)

for c in combinations:
    print(c)