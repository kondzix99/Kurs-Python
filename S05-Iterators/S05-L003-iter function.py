import csv

with open(r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs-Python\Kurs Python Pliki\S05-L003-Zadanie.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))
    while True:
        try:
            data = next(csvreader)
            print(data)
        except StopIteration:
            break
    print('All data was processed')