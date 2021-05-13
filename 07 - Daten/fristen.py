# Fristenrechner 1.0 - Berechnung von Fristen nach §§ 187 ff. BGB
# (C) 11.05.2021, Michael Beurskens

from datetime import date,timedelta,datetime # Funktionen für den Umgang mit Daten


wochentage:list[str]=["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"] # Für die deutsche Darstellung des Namens des Tages

def inputDate(text:str)->date:
    '''Datum abfragen (bis gültige Eingabe erfolgt)'''
    while True:   # Endlosschleife
        value:str=input(text).replace(" ","").replace("-",".").replace("/",".").replace(",","") # Text einlesen; dabei alle Striche, Punkte und Leerzeichen entfernen
        try:
            enteredDate:date=datetime.strptime(value, '%d.%m.%Y')    # Umwandlungsfunktion: Formatiertes Datum. Was die %-Angaben bedeuten sieht man unter https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes (hier: Tag.Monat.Jahr (4-stellig))
            return enteredDate
        except:
            print("Bitte geben Sie ein gültiges Datum mit vierstelligem Jahr (01.01.2020) ein.") # Fehlermeldung bei ungültiger Eingabe

def inputContinue()->bool:
    '''Programm beenden, wenn J, Ja, j, jau, etc. eingegeben wird'''
    value:str=input("Drücken Sie jetzt ""J"", um das Programm zu beenden: ")
    if len(value)>0 and value.lower()[0]=='j':  # Eingabe in Kleinbuchstaben umwandeln und nur ersten Buchstaben auf "j" prüfen
        return True
    else:
        return False

def inputNumber(text:str)->int:
    '''Eingabe von natürlichen Zahlen (ohne Komma, größer Null)'''
    while True: # Endlosschleife
        value:str=input(text) # Text eingeben mit Ausgabe des als Parameter übergebenen Erklärungstextes
        try:
            number:int=int(value) # Text in Zahl umwandeln
            if number<1: # Fehlermeldung bei negativen Zahlen
                print("Bitte geben Sie einen positiven Wert ein.")
            elif value.count(",")>0 or value.count(".")>0: # Fehlermeldung bei Kommazahlen (wobei das Programm nicht bis hier kommen sollte)
                print("Bitte geben Sie eine Zahl oder Komma ein.")
            else:
                return number # Zahl als Ergebnis zurückliefern
        except:
            print("Bitte geben Sie eine positive Zahl ein.") # Fehlermeldung bei unzulässigen Eingaben

print("\n\nDieses Programm berechnet Wochenfristen nach §§ 187 Abs. 1, 188 BGB.")
print("---------\n\n")


while True:
    start:date=inputDate("Bitte geben Sie das Datum an, in dem das Ereignis eingetreten ist: ")  # Eingabe eines gültigen Startdatums
    frist:int=inputNumber("Bitte geben Sie die Zahl der Wochen ein, welche die Frist dauert: ")  # Eingabe einer gültigen Frist

    beginn:date=start+timedelta(days=1)      # Fristbeginn: Einen Tag nach dem Ereignis (also: Addiere eine "Delta" von einem Tag -> timedelta(days=1))
    ziel:date=start+timedelta(weeks=frist)   # Fristende: x Wochen nach dem Ereignis - nicht etwa nach dem Beginn (also: addiere ein "Delta" von eingegeben Wochen -> timedelta(weeks=frist))

    print(f"Fristbeginn: {wochentage[beginn.weekday()]}, {beginn.strftime('%d.%m.%Y')}, 00:00 Uhr")  # Ausgabe des Ergebnisses - zur Klarstellung mit Uhrzeit; wichtig hier: strftime zur Formatierung. Was die %-Angaben bedeuten sieht man unter https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes (hier: Tag.Monat.Jahr (4-stellig))
    print(f"Fristende: {wochentage[ziel.weekday()]}, {ziel.strftime('%d.%m.%Y')} 24:00 Uhr") # Ausgabe des Ergebnisses - zur Klarstellung mit Uhrzeit; wichtig hier: strftime zur Formatierung. Was die %-Angaben bedeuten sieht man unter https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes (hier: Tag.Monat.Jahr (4-stellig))
    if(inputContinue()): # Prüfen, ob das Programm beendet werden soll
        break
    else:
        print("---------") # Zweite Runde mit Trennlinie vorbereiten
        print("\n")
