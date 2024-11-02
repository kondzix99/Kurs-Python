def double(x):
    return x*2

x=10
x = double(x)
print(x)

x = 10
f = lambda x: x*2
print(f(x))

def power(x,y):
    return x**y

x = 5
y = 3
print(power(x,y))

f = lambda x,y: x ** y
print(f(x,y))

list_numbers = [1,2,3,4,11,14,15,20,21]

#sprawdza czy liczba jest nieparzysta
def is_odd(x):
    return x % 2 !=0

print(is_odd(7), is_odd(4))

#dla każdego elementu listy stosowana jest funkcja is_odd
filtered_list = list(filter(is_odd, list_numbers))
print(filtered_list)

filtered_list = list(filter(lambda x: x % 2 != 0, list_numbers))
print(filtered_list)

print(list(filter(lambda x: x % 2 != 0, list_numbers)))

def generate_multiply_function(n):
    return lambda x: n*x

mul_2 = generate_multiply_function(2) #13*2
mul_3 = generate_multiply_function(3) #8*3

print(mul_2(13),mul_3(8))


def mk_thg(a, b, c):
    if c > 0:
        return lambda a, b: a + b
    else:
        return lambda a, b: -a - b


p = mk_thg(1, 2, 1)

print(p(3,4))