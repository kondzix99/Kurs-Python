def BuyMe(what):
    print('Give me', what)

BuyMe('a new car')

StealForMe = BuyMe

print(type(StealForMe))

StealForMe('a new car')

#ZADANIE
def double(x):
    return 2 * x

def square(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2

number = 8
transformations = [double,square,div2,negative]
tmp_return_value = number

for trans in transformations:
    tmp_return_value = trans(tmp_return_value)
    print("Wartosc zmiennej dla liczby {} po operacji {} to {}".format(number, trans.__name__,tmp_return_value))#.__name__ wyświetla nazwe funkcji

print("-"*30)

number = 100
transformations = [double,square,div2,negative]
tmp_return_value = number

for trans in transformations:
    tmp_return_value = trans(tmp_return_value)
    print("Wartosc zmiennej dla liczby {} po operacji {} to {}".format(number, trans.__name__,tmp_return_value))#.__name__ wyświetla nazwe funkcji