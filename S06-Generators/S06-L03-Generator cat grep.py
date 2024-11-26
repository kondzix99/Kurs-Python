'''
Generator grep działa w sposób leniwy, co oznacza, że przetwarza dane tylko wtedy, gdy są potrzebne.
Dzięki temu jest wydajniejszy pamięciowo w porównaniu do standardowych metod filtracji, które tworzą nową listę.

Funkcja grep jako generator w Pythonie to potężne narzędzie do efektywnej filtracji dużych zbiorów danych.
Dzięki yield pozwala przetwarzać dane w sposób leniwy i elastyczny, oszczędzając pamięć i zwiększając wydajność.
'''

import os
import requests

def gen_get_files(dir):
    for d in os.listdir(dir):
        yield os.path.join(dir,d)

def gen_get_file_lines(filename):
    with open(filename,'r') as text:
        for line in text.readlines():
            yield line.strip()

def check_webpage(url):
    try:
        if requests.get(url).status_code == 200:
            return True
    except:
        return False

for file in gen_get_files(r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\links_to_check'):
    for line in gen_get_file_lines(file):
        print("Plik {} o adresie www {} - {}".format(file, line, check_webpage(line)))




