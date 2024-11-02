def BuyMe(prefix, what):
    print(prefix, what)

BuyMe('Please buy me','a new car')
BuyMe(prefix='Please buy me', what='a car')
BuyMe(what='a car', prefix='cos tam')

def show_progress(how_many=1,character='*', ):
    print(how_many*character)


show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, '-')
show_progress(15, '+')