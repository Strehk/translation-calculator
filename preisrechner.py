from math import floor
import os
import re
import time

def get_grundlage():
    with open("grundlage.txt", "r") as f:
        lines = f.readlines()
        n = int(re.search("\d\d", lines[0]).group(0))
        p = float(re.search("(\d+)([.]\d\d)", lines[1]).group(0))
        z = float(re.search("(\d+)([.]\d\d)", lines[2]).group(0))
        s = int(re.search("\d\d", lines[3]).group(0))
    
    return n, p, z, s


NORMZEILE, PREIS_PRO_ZEILE, ZUSCHLAG, NORMSEITE = get_grundlage()


def align_right(text, length):
    return str(text).rjust(length)

def zuschlag_berechnen(preis):
    zuschlag = input("Handelt es sich um eine Eilübersetzung? (j/n) ")
    
    if zuschlag == "j":
        preis_mit_zuschlag = preis + ZUSCHLAG
    else:
        preis_mit_zuschlag = preis

    return preis_mit_zuschlag

def rabatt_berechnen(preis):
    rabatt_check = input("Soll es einen Rabatt geben? (j/n) ")
    if rabatt_check == "j":
        while True:
            try:
                rabatt_input = input("Gib den Rabatt ein (in %): ")
                if rabatt_input.isdigit():
                    rabatt = float(rabatt_input) / 100
                    preis_mit_rabatt = preis * (1 - rabatt)
                    return rabatt, preis_mit_rabatt
                else:
                    raise ValueError("Bitte geben Sie eine Zahl ein.")
            except ValueError as e:
                print(e)
                continue
    else:
        return 0, preis


def preis_berechnen(zeichen):
    zeichen = int(zeichen)
    normzeilen = round(zeichen / NORMZEILE, 2)
    preis = round(normzeilen * PREIS_PRO_ZEILE, 2)
    rabatt, preis_mit_rabatt = rabatt_berechnen(preis)
    preis_mit_zuschlag = zuschlag_berechnen(preis_mit_rabatt)
    return zeichen, normzeilen, preis, rabatt, preis_mit_rabatt, preis_mit_zuschlag


def print_preis(zeichen, normzeilen, preis, rabatt, preis_mit_rabatt, preis_mit_zuschlag):
    prints = []
    
    prints.append("\n")
    prints.append("Berechnungsgrundlage:\n")
    prints.append(f"Zeichen:         {zeichen} übersetzte Zeichen (mit Leerzeichen)")
    prints.append(f"Normzeile:       {NORMZEILE} Zeichen")
    prints.append(f"Basispreis:      {PREIS_PRO_ZEILE:.2f} € pro Normzeile")
    if rabatt != 0:
        prints.append(f"Rabatt:          {rabatt * 100:.2f} %")
    if preis_mit_zuschlag != preis_mit_rabatt:
        prints.append(f"Zuschlag:        {ZUSCHLAG:.2f} € (Eilzuschlag)")
    
    prints.append("\n----------------------------------------------------\n")

    prints.append(f"  {align_right(zeichen, 7)}    Zeichen")
    prints.append(f"/ {align_right(NORMZEILE, 7)}    Zeichen pro Normzeile")
    prints.append("  ------- --")
    prints.append(f"  {align_right(f'{normzeilen:.2f}', 10)} Normzeilen")
    prints.append(f"  {align_right(f'(≙  {(normzeilen / NORMSEITE):.2f}', 10)} Normseiten)")
    
    prints.append("\n----------------------------------------------------\n")

    prints.append(f"  {align_right(f'{normzeilen:.2f}', 10)}   Normzeilen")
    prints.append(f"* {align_right(f'{PREIS_PRO_ZEILE:.2f}', 10)} € Preis pro Normzeile")
    prints.append("  ------- --")
    prints.append(f"  {align_right(f'{preis:.2f}', 10)} € Preis")
    if preis_mit_zuschlag != preis_mit_rabatt or rabatt != 0:
        if rabatt != 0:
            prints.append(f"- {align_right(f'{(preis - preis_mit_rabatt):.2f}', 10)} € Rabatt")
        if preis_mit_zuschlag != preis_mit_rabatt:
            prints.append(f"+ {align_right(f'{ZUSCHLAG:.2f}', 10)} € Eilzuschlag")
        prints.append("  ------- --")
        prints.append(f"  {align_right(f'{preis_mit_zuschlag:.2f}', 10)} € Preis mit {'Zuschlag und Rabatt' if preis_mit_zuschlag != preis_mit_rabatt and rabatt != 0 else ('Rabatt' if rabatt != 0 else 'Zuschlag')}")
    
    
    prints.append("\n----------------------------------------------------\n")

    prints.append(f"Der endgültige Preis für {normzeilen} Normzeilen ({zeichen} Zeichen{'' if preis_mit_rabatt == preis_mit_zuschlag else f', {ZUSCHLAG:.2f}€ Eilzuschlag'}{'' if rabatt == 0 else f', {round(rabatt * 100)}% Rabatt'}) ist: {preis_mit_zuschlag:.2f} €\n\n\n")

    for item in prints:
        print(item)
        time.sleep(0.2)

    time.sleep(4)

    _ = input("Drücken Sie Enter um das Programm neu zu starten...")
    print("\n\n\n")


def main():
    os.system("clear")
    while True:
        try:
            zeichen = input("Gib die Anzahl der Zeichen (mit Leerzeichen) ein: ")
            
            if zeichen.isdigit():
                zeichen, normzeilen, preis, rabatt, preis_mit_rabatt, preis_mit_zuschlag = preis_berechnen(zeichen)
                print_preis(zeichen, normzeilen, preis, rabatt, preis_mit_rabatt, preis_mit_zuschlag)

            else:
                raise ValueError("Bitte geben Sie eine Zahl ein.")

        except ValueError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()