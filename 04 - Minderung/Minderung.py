# Minderung im Kaufrecht
# (C) 20.04.2021 Michael Beurskens

def GeldBetrag(text: str) -> float:
    "Wandelt Text-Eingaben in gültige Geldbeträge mit zwei Nachkommastellen um; Erklärung für den Nutzer durch Parameter text"
    while True:
        wert = input(text)
        # Wenn die Zahl mit Komma statt mit Punkt eingegeben wurde
        wert = wert.replace(",", ".")
        try:
            eingabe = float(wert)
            if(eingabe < 0):
                print(
                    "Bitte eine positive Zahl eingeben (Zahlungen können nicht negativ sein).")
            else:
                # Wenn bei Runden eine Nachkommastelle wegfällt, hat die Zahl offenbar mehr als zwei Nachkommastellen
                if(round(eingabe, 2) != eingabe):
                    print(
                        "Bitte maximal zwei Nachkommastellen eingeben (ein Euro hat maximal 100 Cent).")
                else:
                    break
        except:
            print(
                "Bitte geben Sie eine Ganzzahl (100...) oder eine Kommazahl (20.40) ein.")
    return eingabe


while True:
    # Kaufpreis muss > 0 sein
    while True:  # Kaufpreis muss größer Null sein
        print("-------------------------------------------------------------------------------------------------------------")
        print("Um die Minderung nach § 441 Abs. 3 S. 1 BGB zu berechnen brauchen wir drei Angaben: Den vereinbarten Kaufpreis, den wahren Wert des Kaufgegenstands mit Mangel und den hypothetischen Wert ohne Mangel.")
        print("\n")
        Kaufpreis: float = GeldBetrag("Geben Sie den Kaufpreis in Euro ein: ")
        if(Kaufpreis == 0):
            print("Der Kaufpreis muss größer Null sein (sonst liegt eine Schenkung vor).")
        else:
            break

    # Keine zusätzliche Bedingung für wahren Wert (es reicht ein beliebiger Geldbetrag)
    WahrerWert: float = GeldBetrag(
        "Geben Sie den wahren Wert (mit Mangel) in Euro ein: ")

    # Wahrer Wert muss größer oder gleich dem hypothetischen Wert sein (keine "Herabsetzung" bei Wertsteigerung
    while True:
        HypoWert: float = GeldBetrag(
            "Geben Sie den hypothetischen Wert (ohne Mangel) in Euro ein: ")
        if(HypoWert < WahrerWert):
            print(
                "Der hypothetische Wert (ohne Mangel) muss größer als der wahre Wert (mit Mangel) sein.")
        else:
            break

    print("\n")
    print("Geminderter Kaufpreis (%.2f Euro) = Vereinbarter Kaufpreis (%.2f Euro) * Wahrer Wert mit Mangel (%.2f Euro) / Hypothetischer Wert ohne Mangel (%.2f Euro)" %
          (round(Kaufpreis*WahrerWert/HypoWert, 2), Kaufpreis, WahrerWert, HypoWert))
    print("Der zurückzuzahlende Minderungsbetrag ist %.2f Euro." %
          (Kaufpreis-(round(Kaufpreis*WahrerWert/HypoWert, 2))))
    print("\n")
    if(input("Wollen Sie noch einen weiteren Minderungsbetrag berechnen (J für Ja)? ").lower()[:1] != "j"):
        break
