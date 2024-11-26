import os

try:
    os.mkdir(r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\links_to_check')
except:
    pass

with open(r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\links_to_check\pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open(r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\links_to_check\com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')