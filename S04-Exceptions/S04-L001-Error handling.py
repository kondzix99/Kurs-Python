import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'https://www.onet.pl/'
dir = r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path) == True:
        print("REMOVING")
        os.remove(tmpfile_path)

    #zapisywanie url do pliku
    save_url_to_file(url, tmpfile_path)
    #kopiowanie pliku z tmpfile_path do file_path
    shutil.copy(tmpfile_path, file_path)

except Exception as e:
    print("ERROR "+ "Details: {}".format(e))

else:
    print("COMPLETED SUCCESFULLY")

finally:
    if os.path.exists(tmpfile_path) == True:
        print("REMOVING FINALLY")
        os.remove(tmpfile_path)
    print("THE END")

