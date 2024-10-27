number = 10
print('Variable number', number, id(number))
number += 2
print('Variable number', number, id(number))

text = 'africa'
print('variable text ', text, id(text))
text += ' is hot'
print('variable text ', text, id(text))

#mutable-zmienny, immutable-niezmienny

list = [1,2,3]
print('Variable list', list, id(list))
list.append(4)
print('Variable list', list, id(list))

list2=list
list2.append(5)
print('Variable list', list, id(list))
print('Variable list', list2, id(list2))

list3 = list.copy()
print('Variable list', list, id(list))
print('Variable list3', list3, id(list3))
list3.append(6)
print('Variable list', list, id(list))
print('Variable list3', list3, id(list3))

#ZADANIE
days = ['mon','tue','wed','thu','fri','sat','sun']
workdays = days[:-2]
print('days: ', days, id(days))
print('workdays: ', workdays, id(workdays))
