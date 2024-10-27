dayType = 3

weekend = 1
workday = 2
holiday = 3

if dayType == 1:
    pass
elif dayType ==2:
    pass
else:
   pass #to polecenie nic nie robi

dayDescription = 'weekend' if dayType == 1 else 'workday' if dayType == 2 else 'holiday'
print(dayDescription)

print('weekend') if dayType == 1 else print('workday') if dayType == 2 else print('holiday')

#ZADANIE
price = 123
bonus = 23
bonus_granted = True

price -= bonus if bonus_granted else price
print(price)

rating = 5
print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')

#zwraca numer dnia tygodnia
import datetime as dt
today_weekday = dt.date.today().strftime("%A")
print(today_weekday)