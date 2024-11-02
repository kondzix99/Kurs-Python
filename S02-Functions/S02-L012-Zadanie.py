text_list = ['x','xxx','xxxxx','xxxxxxx','']

napis = "ZF byl spoko"
#wyrazenie lambda
f = lambda x: len(x)

print(f(napis))

#wyrazenie lamda dla listy
print(list(map(f, text_list)))

#wyrazenie lambda dla listy ale definiowana dynamicznie
print(list(map(lambda a: len(a), text_list)))
