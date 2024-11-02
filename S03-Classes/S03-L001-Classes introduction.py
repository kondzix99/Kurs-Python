cake01 = {
'taste': 'vanilia',
'glaze': 'chocolade',
'text': 'Happy Brithday',
'weight': 0.7,
}

cake02 = {
'taste': 'tee',
'glaze': 'lemon',
'text': 'Happy Python Coding',
'weight': 1.3,
}

#print(cake01.values())

def show_cake_info(Acake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        Acake['taste'], Acake['glaze'], Acake['text'], Acake['weight']))

#lista tortow
cakes = [cake01, cake02]
#lista tortow i przechodząc przez nią wyświetl informacje zwracane przez funkcje show_cake_info
for cake in cakes:
    show_cake_info(cake)


