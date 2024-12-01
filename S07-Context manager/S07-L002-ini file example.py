import os
import zipfile
import requests

class FileFromWeb:
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.tmp_file,'wb') as file:
            file.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
path = r"C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\euroxref.zip"

with FileFromWeb(url, path) as f:
    with zipfile.ZipFile(f.tmp_file,'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir(r"C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki")
        z.extract(a_file,'.',None)