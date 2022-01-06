print("Witaj tajemniczy podróżniku, dziś będziemy nadawać paczki, podaj liczbę elementów do wysłania")
max_liczba_elementów = int(input())
element = 0
paczka = 0
wyslane_paczki = 0
wyslane_kilogramy = 0
max_liczba_pustych_kg = 0
najpustsza_paczka = 0
while max_liczba_elementów > 0:
    print("Podaj wagę elementu")
    waga_elementu = float(input())
    if waga_elementu > 10 or waga_elementu == 0 or waga_elementu < 1:
        break
    elif paczka + waga_elementu > 20:
        print("Waga paczki to ", paczka, "Paczka została wysłana")
        ilosc_pustki_w_paczce = 20 - paczka
        paczka = 0 + waga_elementu
        wyslane_paczki = wyslane_paczki + 1
        if ilosc_pustki_w_paczce > max_liczba_pustych_kg:
            max_liczba_pustych_kg = ilosc_pustki_w_paczce
            najpustsza_paczka = wyslane_paczki
    else:
        paczka = paczka + waga_elementu
        max_liczba_elementów = max_liczba_elementów - 1
        wyslane_kilogramy = wyslane_kilogramy + waga_elementu
        print("pozostało ", (max_liczba_elementów), "do wysłania")
        print("Waga paczki to ", (paczka))
else:
    print("Ilosc wyslanych paczek to ", (wyslane_paczki))
    print("Ilość wysłanych kilogramów to ", (wyslane_kilogramy))
    print("Suma pustych kilogramów to ", wyslane_paczki * 20 - wyslane_kilogramy)
    print("Najwięcej pustych kg miała paczka nr ", najpustsza_paczka, "byo to ", max_liczba_pustych_kg, "kg" )
