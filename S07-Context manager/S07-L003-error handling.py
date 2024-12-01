import os
import zipfile
import requests

'''
obsluga bledow za pomoca context managera
'''
class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        # download
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == KeyError:
            print("Nie znaleziono katalogu do wypakowania - blad {}".format(exc_type))
            return True
        elif exc_type == FileNotFoundError:
            print("Nie znaleziono pliku - blad {}".format(exc_type))
            return True
        else:
            return False


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', r"C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\euroxref.zip") as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        # zmiana katalogu na nieistniejący"
        os.chdir('c:/temp')
        z.extract(a_file, '.', None)

