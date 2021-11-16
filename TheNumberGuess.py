import random


wylosowana_liczba = random.randint(1, 100)
print("Wlosowano liczb z zakresu od 1 do 100. Sprubuj ją zgadnąć")
level_gry = input(
    'Wybierz level gry. Wpisz - "hard": Masz 5 szans,  lub "easy": masz 10 szans')
liczba_typowan = []


if level_gry == 'hard':
    level_gry = 5
else:
    level_gry = 10


while level_gry != len(liczba_typowan):
    try:
        typowana_liczba = int(input("Zgadnij liczbę?: "))
        liczba_typowan.append(typowana_liczba)
        if wylosowana_liczba > typowana_liczba:
            print("Liczba jest za mała.")
        elif wylosowana_liczba < typowana_liczba:
            print("Liczba jest za duża.")
        else:
            print(
                f'Zgadłeś liczbę  Liczba wylosowana to "{wylosowana_liczba}"')
            break
    except:
        print('Typowana liczba musi byc liczbą całkowitą')


else:
    print(
        f'Nie zgadłeś. Straciłeś wszystkie szanse. Liczba wylosowana to "{wylosowana_liczba}"')
