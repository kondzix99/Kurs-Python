# for i in range(10,0,-1):
#     print(i)
#
# list = list(range(10))
# print('List: ', list, type(list), id(list))
#
# list2 = list[:]
# print('List2: ', list2, type(list2), id(list2))
#
# #odwrócenie listy
# print(list[-1::-1])

#ZADANIE

colors = ["red", "orange", "green", "violet", "blue", "yellow"]
new_colors = colors.copy()

def return_colors(list_colors, n):
    new_colors = list_colors[:n]
    return new_colors

for i in range(1,len(colors)+1):
    print(return_colors(colors, i))

text = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."

a = text. find("(")
b = text. find(")")
print("TEKST W NAWIASIE: ", text[a+1:b])

#lub sposob z odpowiedzi, w sumie to samo tylko z użyciem index
print(text[text.index('(')+1:text.index(')')])