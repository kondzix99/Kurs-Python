from datetime import datetime

def CreateFunction(kind = '+'):
    source = '''
def f(*args):
    result = 0
    for a in args:
        result {}= a
    return result
'''.format(kind)
    # nie jest okreslone srodowisko, zeby zwrocic wyniki uzyto globals
    exec(source, globals())
    return f

f_add = CreateFunction('+')
print(f_add(1,2,3,4))
f_subs = CreateFunction('-')
print(f_subs(10,20,30))

#ZADANIE
def calculate(span):
    if span == 'm':
        i = 60
    elif span == 'h':
        i = 3600
    elif span == 'd':
        i = 86400

    def time_span_m(start, end):
        duration = end - start
        duration_in_s = duration.total_seconds()
        return divmod(duration_in_s , i)[0]

    return time_span_m


start = datetime(2024, 1, 1, 0, 0, 0)
end = datetime.now()

f_minutes = calculate('m')
f_hours = calculate('h')
f_days = calculate('d')

print("Od poczatku 2024 minelo {} minut:".format(f_minutes(start, end)))
print("Od poczatku 2024 minelo {} godzin:".format(f_hours(start, end)))
print("Od poczatku 2024 minelo {} dni:".format(f_days(start, end)))