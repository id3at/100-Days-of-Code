'''Day 9 - 100 Days of Code - The Complete Python Pro Bootcamp for 2021'''

osoby_licytujace = {}


def dodaj_osobe():

    imie = input("podaj imie")
    cena = int(input('Podaj cene'))
    osoby_licytujace[imie] = cena

# def najwyzsza_cena():
#     liczba_pomocnicza = 0
#     osoba = ''
#     for t in osoby_licytujace:
#         if liczba_pomocnicza < osoby_licytujace[t]:
#             liczba_pomocnicza = osoby_licytujace[t]
#             osoba = t
#     print(f'Wygrał {osoba} z kwotą równą {liczba_pomocnicza}')

def najwyzsza_cena2():

    revers_osob_licytujacych = {k: v for v, k in osoby_licytujace.items()}
    print(f'Wygrał {revers_osob_licytujacych[max(revers_osob_licytujacych)]} z kwotą równą {max(revers_osob_licytujacych)}')


on_off = True
while on_off:
    odp = input("Chcesz dodać osobe?")
    if odp == 'y':
        dodaj_osobe()
    elif odp == 'n':
        najwyzsza_cena2()
        on_off = False
        
