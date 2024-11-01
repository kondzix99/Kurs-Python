# workDays = [19,21, 22, 21, 20, 22]
# months = ['I','II','III','IV','V','VI']
#
# monthDays = dict(zip(months, workDays))
# print(monthDays)
#
# for key in monthDays:
#     print('Key is', key, 'value is', monthDays[key])
#
# for value in monthDays.values():
#     print('the value is', value)

#ZADANIE
banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

dict_denominations = dict(zip(banknotes_coins, [0]*len(banknotes_coins)))

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for key in dict_denominations:
    print('Denominate: {0:6.2f}  - amount\t {1:5}'.format(key, dict_denominations[key]))
