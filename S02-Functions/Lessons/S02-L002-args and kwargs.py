def BuyMe(prefix='Please buy me', what='something nice',*args, **kwargs):
    #argument poprzedzony słowem kluczowym
    print(prefix, what)
    print(args)
    print(kwargs)

BuyMe('Please buy me','a new car', ' super', animal = 'a cat', animal2 = 'a dog')

products = ['milk','bread','flakes']
parameters = {'price':'low','time':'now'}

BuyMe('Buy me', 'newspaper', *products, **parameters)

#ZADANIE 1
def calculate_paint(efficency_ltr_per_m2, *area):
    result = 0
    for i in area:
        paint_area = efficency_ltr_per_m2*i
        result += paint_area
    return result

print(calculate_paint(0.25, 42, 28, 30))
rooms = [42, 28, 30]
print((0.25, *rooms))

def calculate_paint2(efficency_ltr_per_m2, *rooms):
    total_area = sum(rooms)
    paint = total_area * efficency_ltr_per_m2
    return paint

print(calculate_paint2(0.25, 42, 28, 30))
rooms = [42, 28, 30]
print(calculate_paint2(0.25, *rooms))

#ZADANIE 2

def log_it(*args):
    # plik = open('wynik.txt', 'w')
    # x_nowe = []
    # for i in x: x_nowe.append(i + '\n')
    # plik.writelines(x_nowe)
    # plik.close()
    #
    result = []
    path = r'C:\Users\konra\OneDrive\Dokumenty\zadanie.txt'
    with open(path, 'a') as file:  # a - append dodaje na sam koniec pliku czyli dopisuje za każdym razem
        for i in args:
            file.writelines(i + ' ')

        file.write("\n") #kolejne wywołanie da od nowej linijki

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')
log_it('Nie wiem co bedzie z tego mojego zycia')
