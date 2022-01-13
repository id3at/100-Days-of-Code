from gamedata import data


#Losowanie dwóch liczb
import random

lista_liczb_danych = list(range(0, len(data)-1))

losowe_liczby = random.sample(lista_liczb_danych, k=2)



#wypisanie dwóch wyników

pierwszy_los = [data[t] for t in losowe_liczby]

osoba_1 = pierwszy_los[0]
osoba_2 = pierwszy_los[1]

punkty = 0

gra = True
while gra:
    

    #poprabie od użytkownika decyzji które wieksze
    print(f"Co ma wieksza liczbe oglądających A: {osoba_1['name']} vs B: {osoba_2['name']}")
    decyzja_uzyt = input("Wybierz 'A' lub 'B'")

    #Zakonczenie gry lub dodanie punktu jesli zgadl
    
    if decyzja_uzyt == "A":
        if osoba_1['follower_count'] > osoba_2['follower_count']:
            punkty += 1
            print(punkty)
            losowa_liczba = random.sample(lista_liczb_danych, k=1)
            osoba_2 = data[losowa_liczba[0]]
        else:
            print("Koniec gry")
            print(punkty)
            gra = False
    if decyzja_uzyt == "B":
        if osoba_2['follower_count'] > osoba_1['follower_count']:
            punkty += 1
            print(punkty)
            losowa_liczba = random.sample(lista_liczb_danych, k=1)
            osoba_1 = data[losowa_liczba[0]]

        else:
            print("Koniec gry")
            print(punkty)
            gra = False
        

    #Wylosowanie kolejnej liczb


