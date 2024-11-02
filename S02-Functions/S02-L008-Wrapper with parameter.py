import os
import functools
from datetime import datetime as dt

def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wraper(path):
            file = open(log_file_path, "a")
            file.write('Wykonywana czynność "{}" '.format(logged_action))
            file.write('Operacja wykonywana na pliku {}'.format(path))
            file.write('Data i godzina: {}'.format(dt.now().strftime("%Y-%m-%d %H:%M:%S")))
            return func
        return the_real_wraper
    return wrapper_with_log_to_known_file


@wrapper_with_log_file( "FILE_CREATE", r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs Python\file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")

@wrapper_with_log_file("FILE_DELETE",r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs Python\file_delete.txt' )
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs Python\dummy_file.txt')
delete_file(r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs Python\dummy_file.txt')
create_file(r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs Python\dummy_file.txt')
delete_file(r'C:\Users\konra\OneDrive\Dokumenty\Konrad Pliki\Kurs Python\dummy_file.txt')

#komentarz