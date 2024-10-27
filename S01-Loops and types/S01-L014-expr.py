import os.path

var_x = 10

source = '''
new_var = 1
for i in range(var_x):
    print('-'*i)
    new_var += i
'''

result = exec(source)
print(result)

print(var_x)
print(new_var)

#source = input("Enter your expressions: ")
#print(eval(source))

files_to_process = [
    r"C:\Users\konra\PycharmProjects\Sekcja2\.venv\Lessons\S01-L014 zadanie part1.py",
    r"C:\Users\konra\PycharmProjects\Sekcja2\.venv\Lessons\S01-L014 zadanie part2.py",
    ]

for file_path in files_to_process:
    #wczytanie pliku
    with open(file_path, 'r') as f:
        print("File name: {}".format(os.path.basename(file_path)))
        source = f.read()
        exec(source)