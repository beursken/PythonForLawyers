# Programm: Berechnung der Gesamtnotenstufe und Punktzahl nach § 17 Abs. 1 JAPO
# (C), 26.04.2012, Valerie Pichlmayr

# Funktion:
def GesamtNotenstufe(Note: float) -> str:
    if Note >= 14.00:
        return "sehr gut (%.2f Punkte)" % Note
    elif Note >= 11.50:
        return "gut (%.2f Punkte)" % Note
    elif Note >= 9.00:
        return "vollbefriedigend (%.2f Punkte)" % Note
    elif Note >= 6.50:
        return "befriedigend (%.2f Punkte)" % Note
    elif Note >= 4.00:
        return "ausreichend (%.2f Punkte)" % Note
    elif Note >= 1.50:
        return "mangelhaft (%.2f Punkte)" % Note
    else:
        return f"ungenügend ({Note:.2f} Punkte)"


def Einzelnotenstufe(Note: float) -> str:
    if Note >= 16:
        return "sehr gut (%.2f Punkte)" % Note
    elif Note >= 13:
        return "gut (%.2f Punkte)" % Note
    elif Note >= 10:
        return "vollbefriedigend (%.2f Punkte)" % Note
    elif Note >= 7:
        return "befriedigend (%.2f Punkte)" % Note
    elif Note >= 4:
        return "ausreichend (%.2f Punkte)" % Note
    elif Note >= 1:
        return "mangelhaft (%.2f Punkte)" % Note
    else:
        return "ungenügend (%.2f Punkte)" % Note


def ErlasseneKlausuren() -> int:
    while True:
        eingabe: str = input(
            "Wie viele Klausuren wurden Ihnen erlassen (0 bis 2) ")
        try:
            zahl: int = int(eingabe)
            if(zahl >= 0) and (zahl <= 2):
                return zahl
            else:
                print(
                    "Die Zahl der erlassenen Klausuren darf nur zwischen 0 und 2 liegen.")
        except:
            print("Bitte geben Sie ausschließlich Zahlen (zwischen 0 und 2) ein.")


def NotenEingabeGanz(text: str) -> int:
    while True:
        eingabe: str = input(text)
        try:
            zahl: int = int(eingabe)
            if(zahl >= 0) and (zahl <= 18):
                return zahl
            else:
                print("Noten dürfen nur zwischen 0 und 18 liegen.")
        except:
            print("Bitte geben Sie ausschließlich Zahlen (zwischen 0 und 18) ein.")


def NotenEingabeKomma(text: str) -> float:
    while True:
        eingabe: str = input(text)
        eingabe = eingabe.replace(",", ".")
        try:
            zahl: float = float(eingabe)
            if(zahl >= 0) and (zahl <= 18):
                if zahl % 0.5 == 0:
                    return zahl
                else:
                    print("Die Note darf nur um 0.5 zwischen zwei Stufen liegen.")
            else:
                print("Noten dürfen nur zwischen 0 und 18 liegen.")
        except:
            print("Bitte geben Sie ausschließlich Zahlen (zwischen 0 und 18) ein.")


print("Dieses Programm berechnet Ihre Gesamtnote für das Erste Staatsexamen (bestehend aus EJS und JUP)\n\n\n")
print("\n")
print("--- EJS: Klausurnoten ---")
print("\n")


klausurzaehler: int = 1
erlassenenKlausuren: int = ErlasseneKlausuren()
summeKlausuren: float = 0
anzahlUnter40: int = 0

maximalErgebnis: float = (6-erlassenenKlausuren)*18
gesamtNoteStaatlich: float = 0

# Klausuren

while(klausurzaehler < 7-erlassenenKlausuren):
    klausurNote: float = NotenEingabeKomma(
        f"Geben Sie die Note der {klausurzaehler}. Klausur ein: ")

    print(
        f"Sie haben in der {klausurzaehler}. Klausur die Note {Einzelnotenstufe(klausurNote)} erzielt.")

    klausurzaehler += 1
    summeKlausuren += klausurNote

    maximalErgebnis -= 18
    maximalErgebnis += klausurNote

    if(klausurNote < 4.0):
        anzahlUnter40 += 1  # <=> anzahlUnter40=anzahlUnter40+1
    print(
        f"Sie können nach dieser Klausur noch maximal {maximalErgebnis/(6-erlassenenKlausuren)} Punkte erzielen.")

    if(anzahlUnter40 > 3):
        print("Sie können ohnehin nicht mehr bestehen, da Sie mehr als 3 Klausuren nicht bestanden haben.")
        break

    if(maximalErgebnis/(6-erlassenenKlausuren) < 3.8):
        print(
            "Sie können nicht mehr als 3.8 Punkte erreichen und sind damit durchgefallen.")
        break


durchschnittsnoteKlausuren: float = summeKlausuren/(6-erlassenenKlausuren)

print(
    f"Die Gesamtnote der Klausuren ist {GesamtNotenstufe(durchschnittsnoteKlausuren)}.")


print("\n")
print("--- EJS: mündliche Prüfung ---")
print("\n")

# Mündliche Prüfung
if durchschnittsnoteKlausuren < 3.8 \
        or ((erlassenenKlausuren != 2) and anzahlUnter40 > 3) \
        or ((erlassenenKlausuren == 2) and anzahlUnter40 > 2):
    print("Sie wurden nicht zur mündlichen Prüfung zugelassen. Sie haben damit die EJS nicht bestanden.")
else:
    print("Sie wurden zur mündlichen Prüfung zugelassen.")
    summeMuendlich: int = NotenEingabeGanz(
        "Welche Note haben Sie in der mündlichen Prüfung im Zivilrecht erreicht? ")
    summeMuendlich += NotenEingabeGanz(
        "Welche Note haben Sie in der mündlichen Prüfung im Strafrecht erreicht? ")
    summeMuendlich += NotenEingabeGanz(
        "Welche Note haben Sie in der mündlichen Prüfung im Öffentlichen Recht erreicht? ")
    durchschnittsnoteMuendlich: float = summeMuendlich/3
    print(
        f"Die Gesamtnote der mündlichen Prüfung ist {GesamtNotenstufe(durchschnittsnoteMuendlich)}.")
    gesamtNoteStaatlich = (
        durchschnittsnoteKlausuren*3+durchschnittsnoteMuendlich)/4
    print(
        f"Die Gesamtnote der staatlichen Prüfung ist {GesamtNotenstufe(gesamtNoteStaatlich)}.")


print("\n")
print("--- JUP ---")
print("\n")

# Universitätsprüfung

schwerpunktKlausur: float = NotenEingabeKomma(
    "Welche Note haben Sie in der Schwerpunktklausur erzielt? ")
schwerpunktSeminarMuendlich: int = NotenEingabeGanz(
    "Welche mündliche Note haben Sie im Seminar erzielt? ")
schwerpunktSeminarArbeit: float = NotenEingabeKomma(
    "Welche Note haben Sie in der Seminararbeit erzielt? ")

print(
    f"Die Gesamtnote für die Teilleistung 1 beträgt {GesamtNotenstufe( (schwerpunktSeminarArbeit*2/3 + schwerpunktSeminarMuendlich/3))}")

gesamtNoteSchwerpunkt: float =\
    schwerpunktKlausur*0.4 + \
    (schwerpunktSeminarArbeit*2/3 + schwerpunktSeminarMuendlich/3)*0.6

print(
    f"Die Gesamtnote im Schwerpunktbereich beträgt {GesamtNotenstufe(gesamtNoteSchwerpunkt)}")

if(gesamtNoteSchwerpunkt < 4.0):
    print("Damit haben Sie die Juristische Universitätsprüfung nicht bestanden.")


print("\n")
print("--- Gesamtnote ---")
print("\n")

if(gesamtNoteStaatlich > 4.0 and gesamtNoteSchwerpunkt > 4.0):
    print(
        f"Die Gesamtnote der Ersten Juristischen Prüfung (staatlicher Teil und Universitätsteil) beträgt {GesamtNotenstufe(gesamtNoteSchwerpunkt*0.3+gesamtNoteStaatlich*0.7)}")
else:
    print("Sie haben die Prüfung bislang noch nicht bestanden.")
