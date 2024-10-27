from enum import unique

#użycie generatorów plus zliczenie ile wartości jest generowanych przez generator

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

gen1= ((a,b) for a in ports for b in ports)
i = 0
for x in gen1:
    print(x)
    i+=1

j = 0
gen2 = ((a,b) for a in ports for b in ports if a!=b)
for y in gen2:
    print(y)
    j+=1

k = 0
gen3 = ((a,b) for a in ports for b in ports if a<b)
for z in gen3:
    print(z)
    k += 1

print("Dlugosc wszystkich polaczen: {}".format(i))
print("Dlugosc wszystkich  polaczen bez tych samych miast: {}".format(j))
print("Dlugosc wszystkich  polaczen tylko unikatowe: {}".format(k))