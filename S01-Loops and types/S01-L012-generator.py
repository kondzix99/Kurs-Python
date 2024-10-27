listA = list(range(6))
listB = list(range(6))

product = []

for a in listA:
    for b in listB:
        product.append((a,b))

gen = ((a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)# wyświetla nieparzyste z a i parzyste z b
print(gen)

#zwraca następną wartość z generatora
print(next(gen))
print(next(gen))
print('-'*30)
for x in gen:
    print(x)
print('-'*30)
for x in gen:
    print(x)

gen = ((a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)# wyświetla nieparzyste z a i parzyste z b

while True:
    try:
        print(next(gen))
    except StopIteration:
        print('all values have been generated')
        break