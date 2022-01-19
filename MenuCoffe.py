
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

GROSZE = 0.50
ZLOTOWKA = 1
DWAZLOTE = 2
PIECZLOTYCH = 5

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




def suma():
    return (GROSZE * ilosc_piecdz) + (ZLOTOWKA * ilosc_zlotowek) + (DWAZLOTE * ilosc_dwazlote) + (PIECZLOTYCH * ilosc_piecio)


def raport():
    raport = f"""
Water: {resources['water']} ml,
Milk: {resources['milk']}ml,
Coffee: {resources['coffee']}ml.
"""
    print(raport)

def odejmowanie(wejscie):

    if wejscie == 'raport':
        raport()
    elif wejscie == 'espresso':
        if resources['water'] >= MENU[wejscie]['ingredients']['water'] and resources['coffee'] >= MENU[wejscie]['ingredients']['coffee']:
            resources['water'] = resources['water'] - MENU[wejscie]['ingredients']['water']
            resources['coffee'] = resources['coffee'] - MENU[wejscie]['ingredients']['coffee']
        else: 
            print("Brak składników")
    else:
        if resources['water'] >= MENU[wejscie]['ingredients']['water'] and resources['coffee'] >= MENU[wejscie]['ingredients']['coffee'] and resources['milk'] >= MENU[wejscie]['ingredients']['milk']:
            resources['water'] = resources['water'] - MENU[wejscie]['ingredients']['water']
            resources['milk'] = resources['milk'] - MENU[wejscie]['ingredients']['milk']
            resources['coffee'] = resources['coffee'] - MENU[wejscie]['ingredients']['coffee']
        else:
            print("Brak składników")





warunek_petli = True
while warunek_petli:

        wejscie_użytkownika = input('Wybierz: espresso/latte/cappuccino/Koniec/raport: ') 
        if wejscie_użytkownika == 'Koniec':
            warunek_petli = False
        elif wejscie_użytkownika == 'raport':
            raport()
        else:
            ilosc_piecdz = int(input("Ile 50 groszówek: "))
            ilosc_zlotowek = int(input("Ile złotówek: "))
            ilosc_dwazlote = int(input("Ile dwuzlotówek: "))
            ilosc_piecio = int(input("Ile piecio złotówek: "))
            kasa = suma()
            cena = MENU[wejscie_użytkownika]['cost']
            if kasa >= cena:
                odejmowanie(wejscie_użytkownika)
                reszta = kasa - cena
                print(f"Twoja reszta {reszta}")
                raport()
            else:
                print('Za mało środków')
                print(f'Twoja gotówka to {kasa}, koszt {wejscie_użytkownika}, to {cena}')



    



