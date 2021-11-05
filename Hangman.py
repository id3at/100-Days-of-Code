""""Day 7 - 100 Days of Code - The Complete Python Pro Bootcamp for 2021"""

import random
import art


wisielec = "wisielec"

wisielecGry = ["_","_","_","_","_","_","_","_",]
indexwisielca = 0

listaSlow = ['dobro', 'markiz', 'słowa', 'zbrodnia', 'radość']

losoweSlowo = random.choice(listaSlow)
zakryteLosSlo = ["_" for _ in losoweSlowo]
print(art.logo)
print(zakryteLosSlo)

while losoweSlowo != "".join(zakryteLosSlo):
    literaUsera = input("Podaj literę: ")
    if literaUsera in losoweSlowo:
        for index,litera in enumerate(losoweSlowo):
           if literaUsera == litera:
                zakryteLosSlo[index] = litera    
        print(zakryteLosSlo)
        if losoweSlowo == "".join(zakryteLosSlo):
            print(f"Zgadłeś: Wylosowane słowo to '{''.join(zakryteLosSlo).upper()}'")
    else:
        wisielecGry[indexwisielca] = wisielec[indexwisielca]
        indexwisielca += 1
        print("".join(wisielecGry))
        if wisielec == ''.join(wisielecGry):
            print('Nie Zgadłeś!!')
            break
