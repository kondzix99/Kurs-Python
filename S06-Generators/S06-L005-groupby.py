import itertools as it
import os
'''
ten plik sprawdza ile plików i katalagów znajduje się w określonym katalagu
wykorzystujemy tutaj groupby z modułu intertools

'''
p = r"C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki"

def scan_tree(path):
    with os.scandir(path) as file:
        for f in file:
            if f.is_dir() == True:
                yield f
                scan_tree(f)
            else:
                yield f


listing = scan_tree(p)
for l in listing:
        print('DIR ' if l.is_dir() else 'FILE', l.path)

listing = scan_tree(p)
print("-"*30)
listing = sorted(listing, key=lambda x: x.is_dir())
for is_dir, elements in it.groupby(listing, key = lambda x: x.is_dir()):
    print('DIR' if is_dir else 'FILE',len(list(elements)))


print("-"*30)
#ponizej przyklad z chat GPT
# Przykładowa lista
dane = [('A', 10), ('A', 20), ('B', 30), ('B', 40), ('A', 50)]

# Grupowanie po pierwszym elemencie
for klucz, grupa in it.groupby(sorted(dane, key=lambda x: x[0]), key=lambda x: x[0]):
    print(f"{klucz}: {[item[1] for item in grupa]}")