
class HtmlCM:

    def __init__(self):
        pass

    def __enter__(self):
        '''
        ENTER
        Wywoływana automatycznie na początku bloku with.
        Zwykle służy do przygotowania zasobów, które będą używane w bloku (np. otwarcie pliku, zarezerwowanie zasobów, połączenie z bazą danych).
        Może zwracać wartość, która jest przypisana do zmiennej po słowie kluczowym as (np. with context_manager() as variable)
        '''
        print("<TABLE>")
        print(" <TR>")
        print("  <TH>Number</TH><TH>Description</TH>")
        print(" </TR>")
        return self

    #type, value, traceback
    def __exit__(self, exc_type, exc_val, exc_tb):
        '''
        Wywoływana automatycznie na końcu bloku with, niezależnie od tego, czy kod zakończył się sukcesem, czy wystąpił wyjątek.
        Służy do czyszczenia zasobów lub innych czynności porządkowych (np. zamykanie pliku, zwalnianie pamięci).
        Przyjmuje trzy argumenty:
        exc_type: Typ wyjątku, jeśli wystąpił (np. ValueError), w przeciwnym razie None.
        exc_val: Wartość wyjątku, jeśli wystąpił (np. instancja błędu), w przeciwnym razie None.
        exc_tb: Ślad stosu (traceback) dla wyjątku, jeśli wystąpił, w przeciwnym razie None.
        Jeśli __exit__ zwróci True, wyjątek zostanie "przełknięty", tj. program będzie kontynuował działanie, jakby wyjątku nie było.
        '''
        print("</TABLE>")

with HtmlCM() as html:
    print(" <TR>")
    print("     <TD>1</TD><TD>Say hello!</TD>")
    print(" </TR>")
    print(" <TR>")
    print("     <TD>2</TD><TD>Say good bye!</TD>")
    print(" </TR>")

#help(html.__exit__)