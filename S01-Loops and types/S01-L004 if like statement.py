import os

# path = r'C:\Users\konra\OneDrive\Dokumenty\mydata.txt'
#
# #os.remove(path)
#
# '''
# if os.path.isfile(path):
#     print('File %s exists' % path)
# else:
#     print('Creating a file %s' % path)
#     open(path, 'x'). close()
#     print('File %s created' % path)
# '''
#
# #funkcja open otwiera plik i od razu go zamyka
# result = os.path.isfile(path) or open(path, 'x').close()
# print(result)

#ZADANIE
path = r'C:\Users\konra\OneDrive\Dokumenty\zadanie.txt'

def counted_words(path):
    with open(path,'r') as f: #tylko wczytuje plik
        word = f.read()
        counts = len(word.split(" "))
        print("Spliited word with space: ", word)
    return counts

if os.path.isfile(path):
    print('File %s exists' % path)
    print('Counted words: {}'.format(counted_words(path)))

os.path.isfile(path) and print("There are {} words in the file {}".format(counted_words(path), path))