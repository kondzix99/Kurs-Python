#eval innymi słowy, interpretuje i uruchamia kod zapisany w formie tekstowej.

# var_x = 10
# password = 'hufjejf'
#
# source = 'var_x + 1'
#
# #globals = globals().copy()
# #del globals['password']
# globals = {}
#
# result = eval(source, globals)
# print(result)

#kalkulator oparty na funkcji eval
import math

argument_list = []


for i in range(0,100):
    argument_list.append(i/10)
print(argument_list)

formula = input("Wprowadz wzor matematyczny ze zmienna x: ")

for x in argument_list:
    print('Wynik działania {} z {} to {}'. format(formula, x, eval(formula)))