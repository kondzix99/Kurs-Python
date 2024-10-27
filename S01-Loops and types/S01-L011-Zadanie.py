from enum import unique

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections = [(a,b) for a in ports for b in ports]
print(connections)

connections_b = [(a,b) for a in ports for b in ports if a!=b]
print(connections_b)

connections_c = [(a,b) for a in ports for b in ports if a<b]
print(connections_c)

print("Dlugosc wszystkich polaczen: {}".format(len(connections)))
print("Dlugosc wszystkich  polaczen bez tych samych miast: {}".format(len(connections_b)))
print("Dlugosc wszystkich  polaczen tylko unikatowe: {}".format(len(connections_c)))

# 3. Wyeliminuj zdublowane połączenia (A -> B i B -> A traktujemy jako jedno)
unique_connections = []
for a, b in connections_b:
    if (b, a) not in unique_connections:
        unique_connections.append((a, b))

print(unique_connections)
print(len(unique_connections))
