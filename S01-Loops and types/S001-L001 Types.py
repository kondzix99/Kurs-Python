myvar = 'Hello Pycharm!'
myvar2 = myvar + '!!'
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print('Is the value the same?', myvar == myvar2)
print('Are the variables the same?', myvar is myvar2)
print(id(myvar), id(myvar2))
myvar2 = myvar2[:-2]
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print('Is the value the same?', myvar == myvar2)
print('Are the variables the same?', myvar is myvar2)
print(id(myvar), id(myvar2))

#LAB1
a=b=c=10
print(a,b,c,id(a),id(b),id(c))
a=20
print(a,b,c,id(a),id(b),id(c))

a = b = c = [1,2,3]
print(a,b,c,id(a),id(b),id(c))
a.append(4)
print(a,b,c,id(a),id(b),id(c))

x=10
y=10
print(f'x = {id(x)}, y = {id(y)}')

y =- 1234567890
y =+ 1234567890
print(f'x = {id(x)}, y = {id(y)}')