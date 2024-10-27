import math, time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range (10000):
    argument_list.append(i/10)


for formula in formulas_list:
    results_list = []
    start = time.time()
    print("Obecnie liczy sie formula {}".format(formula))
    for x in argument_list:
        results_list.append(eval(formula))
    print("Maksimum to {}, a minimum to  {}".format(max(results_list),min(results_list)))
    stop = time.time()
    czas_przed = stop - start
    print("Czas trwania obliczen przed optymalizacja: {}".format(stop - start))
#print(results_list)

#po optymalizacji kodu z użyciem compile
start = time.time()

for formula in formulas_list:
    results_list = []
    start = time.time()
    compiled_formula = compile(source=formula, filename='internal variable source', mode='eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print("Maksimum to {}, a minimum to  {}".format(max(results_list),min(results_list)))
    stop = time.time()
    czas_po = stop-start
    print("Czas trwania obliczen po optymalizacji: {}".format(stop-start))