isOK = 'True'
print('Variable isOK', isOK, type(isOK))
if isOK:
    print('TRUE\n')

#ZADANIE
def DisplayOptions(options):
    for i in range(len(options)):
        print(f'{i+1} = {options[i]}')

    choice = input('Select option above or press enter to exit: ')
    return choice

options = ['load data', 'export data', 'analyze & predict']
choice = 'x'


while(choice):

    choice = DisplayOptions(options)

    if choice:
        try:
            choice_num = int(choice) - 1
            if (choice_num >= 0 and choice_num< len(options)):
                # indeksowanie 0,1,2 a 1,2,3 dlatego te plus 1
                print("Dokonano wyboru: ", choice_num+1, options[choice_num])
            else:
                print("Dokonano nieprawidłowego wyboru")

        except:
            print("Wprowadzona wartość musi być liczbą")

    else:
        print("ZAKOŃCZENIE DZIAŁANIA PROGRAMU")