from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

rapor = CoffeeMaker()
men = Menu()
monyy = MoneyMachine()



warunek_petli = True
while warunek_petli:

        wejscie_użytkownika = input(f'Wybierz: {men.get_items()}Koniec/raport: ') 
        if wejscie_użytkownika == 'Koniec':
            warunek_petli = False
        elif wejscie_użytkownika == 'raport':
            rapor.report()
        else:
            if men.find_drink(wejscie_użytkownika):
                if rapor.is_resource_sufficient(men.find_drink(wejscie_użytkownika)):
                    if monyy.make_payment(men.find_drink(wejscie_użytkownika).cost):    
                        rapor.make_coffee(men.find_drink(wejscie_użytkownika))
