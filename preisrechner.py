from math import floor
import os
import time


NORMZEILE = 55
PREIS_PRO_ZEILE = 1.00
ZUSCHLAG = 15

def align_right(text, length):
    return str(text).rjust(length)

def zuschlag_berechnen(preis):
    zuschlag = input("Handelt es sich um eine Eilübersetzung? (j/n) ")
    
    if zuschlag == "j":
        preis_mit_zuschlag = preis + ZUSCHLAG
    else:
        preis_mit_zuschlag = preis

    return preis_mit_zuschlag


def preis_berechnen(zeichen):
    zeichen = int(zeichen)
    normzeilen = round(zeichen / NORMZEILE, 2)
    preis = round(normzeilen * PREIS_PRO_ZEILE, 2)
    preis_mit_zuschlag = zuschlag_berechnen(preis)
    return zeichen, normzeilen, preis, preis_mit_zuschlag


def print_preis(zeichen, normzeilen, preis, preis_mit_zuschlag):
    prints = []
    
    prints.append("\n")
    prints.append("Berechnungsgrundlage:")
    prints.append(f"Zeichen:         {zeichen} Zeichen pro Zeile")
    prints.append(f"Normzeile:       {NORMZEILE} Zeichen")
    prints.append(f"Preis pro Zeile: {PREIS_PRO_ZEILE:.2f} €")
    if preis_mit_zuschlag != preis:
        prints.append(f"Zuschlag:        {ZUSCHLAG:.2f} €")
    
    prints.append("\n----------------------------------------------------\n")

    prints.append(f"  {align_right(zeichen, 7)}    Zeichen)")
    prints.append(f"/ {align_right(NORMZEILE, 7)}    Zeichen pro Normzeile")
    prints.append("  ------- --")
    prints.append(f"= {align_right(f'{normzeilen:.2f}', 10)} Normzeilen")
    
    prints.append("\n----------------------------------------------------\n")

    prints.append(f"  {align_right(f'{normzeilen:.2f}', 10)} Normzeilen")
    prints.append(f"* {align_right(f'{PREIS_PRO_ZEILE:.2f}', 10)} €")
    prints.append("  ------- --")
    prints.append(f"= {align_right(f'{preis:.2f}', 10)} € Preis")
    if preis_mit_zuschlag != preis:
        prints.append(f"+ {align_right(f'{ZUSCHLAG:.2f}', 10)} € Zuschlag")
        prints.append("  ------- --")
        prints.append(f"= {align_right(f'{preis_mit_zuschlag:.2f}', 10)} € Preis mit Zuschlag")
    
    prints.append("\n----------------------------------------------------\n")

    prints.append(f"Der endgültige Preis für {normzeilen} Normzeilen ({zeichen} Zeichen{'' if preis == preis_mit_zuschlag else f', {ZUSCHLAG}€ Zuschlag'}) ist: {preis_mit_zuschlag:.2f} €\n\n\n")

    for item in prints:
        print(item)
        time.sleep(0.5)

    time.sleep(4)

    _ = input("Drücken Sie Enter um das Programm neu zu starten...")
    print("\n\n\n")


def main():
    os.system("clear")
    while True:
        try:
            zeichen = input("Gib die Anzahl der Zeichen (mit Leerzeichen) ein: ")
            

            if zeichen.isdigit():
                zeichen, normzeilen, preis, preis_mit_zuschlag = preis_berechnen(zeichen)
                print_preis(zeichen, normzeilen, preis, preis_mit_zuschlag)

            else:
                raise ValueError("Bitte geben Sie eine Zahl ein.")

        except ValueError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()