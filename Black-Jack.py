import random

karty = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4


def usuwanieKart(kartydousuniecia):
    for t in kartydousuniecia:
        karty.remove(int(t))


odp_KontynuacjaGry = 'y'

while odp_KontynuacjaGry == 'y' and karty:
    print(karty)
    karty_gracza = list(random.choices(karty, k=2))
    usuwanieKart(karty_gracza)
    karty_krupiera = list(random.choices(karty, k=2))
    usuwanieKart(karty_krupiera)

    print(f'Karty Gracza: {karty_gracza}')

    petla_wygranej = True
    petla_krupiera = True

    while (dobieranie := input("Dobieranie 'y' lub 'n'")) == 'y':

        if dobieranie == 'y' and karty:
            if len(karty) <= 5:
              
                break

            karta_dobrana = list(random.choices(karty, k=1))
            karty_gracza.append(karta_dobrana[0])
            print(f'Karty Gracza: {karty_gracza}')

            usuwanieKart(karta_dobrana)
            if sum(karty_gracza) > 21:
                print(
                    f'Wygrały karty krupiera {karty_krupiera} Gracz pobrał za duzo kart: {karty_gracza}')

                petla_wygranej = False
                petla_krupiera = False
                break

    while petla_krupiera:
        if len(karty) <= 5:
              
                break

        if sum(karty_krupiera) > 21:
            petla_wygranej = False
            petla_krupiera = False
            print(
                f'Gracz wygrał {karty_gracza} Kurier pobrał za duzo kart: {karty_krupiera}')
        elif sum(karty_krupiera) >= 17:

            petla_krupiera = False
        else:
            karta_dobrana = list(random.choices(karty, k=1))
            karty_krupiera.append(karta_dobrana[0])
            usuwanieKart(karta_dobrana)

    while petla_wygranej:
        if len(karty) == 0 or len(karty) <= 5:
          
            break
        if len(karty_gracza) == 2 and sum(karty_gracza) == 2 and sum(karty_gracza) > sum(karty_krupiera):
            print(f'Gracz wygrał BlacjJack{karty_gracza} z kartami {karty_krupiera}')

        elif sum(karty_gracza) > sum(karty_krupiera):
            print(f'Gracz wygrał {karty_gracza} z kartami {karty_krupiera}')
            petla_wygranej = False
        elif sum(karty_gracza) == sum(karty_krupiera):
            print(
                f'Remis karty gracza {karty_gracza} vs karty krupiera {karty_krupiera}')
            petla_wygranej = False
        else:
            print(
                f'Wygrały karty krupiera {karty_krupiera} z kartami gracza {karty_gracza} ')
            petla_wygranej = False

    odp_KontynuacjaGry = input("Kontynuować grę")

    if len(karty) == 0 or len(karty) <= 5:
        print("Koniec Tali")
        break
