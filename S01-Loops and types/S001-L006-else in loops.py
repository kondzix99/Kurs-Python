import os
import urllib.request

data_dir = r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs Python'

pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'onet', 'url': 'https://www.onet.pl/' },

    { 'name': 'nasze',       'url': 'https://www.nasze.fm/'} ]

path = []

for page in pages:
    try:
        file_name = "{}.html".format(page["name"])
        #path = os.path.join(data_dir, file_name) -> robi to samo co linijka 19
        path = data_dir + "\\" + page["name"] + ".html"

        print("Processing ... {}".format(page["url"], file_name))
        urllib.request.urlretrieve(page["url"], path)
        print("wczytane")

    except:
        print("BŁAD WCZYTYWANIA STRONY ... {}". format(page["url"], file_name))
        print("STOP")
        break

else:
    print("KONIEC PETLI - UDALO SIE WCZYTAC")