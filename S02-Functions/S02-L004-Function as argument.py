def Bake(what):
    print('Baking {}'.format(what))

def Add(what):
    print('Adding {}'.format(what))

def Mix(what):
    print('Mixing {}'.format(what))

def Cook(activity, obj):
    activity(obj)

cookbook = [(Add, 'milk'),(Add, 'eggs')]

#funkcja jako argument funkcji
Cook(Bake, 'brownies')

for activity, obj in cookbook:
    Cook(activity, obj)

#ZADANIE
def double(x):
    return 2 * x

def square(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2

#pierwszy argument to funckja, którą będzie liczyć
#drugi argument to liczby, które będą obliczane
def generate_values(function, numbers):

    result = []

    for i in numbers:
        result.append(function(i))

    return result

x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))