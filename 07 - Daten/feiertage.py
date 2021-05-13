# Feiertagschecker - Prüfung, ob ein bestimmtes Datum in einem bestimmten Bundesland ein Feiertag ist
# Hierzu wird (a) auf eine Webseite zugegriffen und (b) eine XML-Datei ausgewertet
# Die Schnittstelle ist unter https://www.spiketime.de/blog/spiketime-feiertag-api-feiertage-nach-bundeslandern/ dokumentiert
# (C) 11.05.2021, Michael Beurskens

from datetime import date,timedelta,datetime # Funktionen für den Umgang mit Daten (siehe auch fristen.py)
from urllib.request import urlopen, Request # Um Daten aus dem Internet abzurufen
import xml.etree.ElementTree as ET # Funktionen zur Verarbeitung von XML-Daten


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


def getBundesLand()->str:
    '''Eingabe eines Bundeslandes und Prüfung, ob dies gültig ist'''
    url=urlopen(
            Request("https://www.spiketime.de/feiertagapi/bundeslaender",
            headers={"Accept": "application/xml"})        
        , data=None)
    
    # Lade eine Datei aus dem Internet ("urlopen") - dabei wichtig die Angaben hinter Request: Zunächst die Adresse ("url") und dann die akzeptierten Datenformate (hier nur: "XML")
    # Diese Vorgaben kann man eigentlich immer nutzen, wenn es um strukturierte Daten geht
    # Schließlich: Keine Parameter übermitteln.

    namespaces={'ft': 'http://schemas.datacontract.org/2004/07/FeiertagAPI'} # Verwendete Namespaces (Beschreibungen) in der XML-Datei (siehe erste Zeile unte https://www.spiketime.de/feiertagapi/bundeslaender : xmlns="http://schemas.datacontract.org/2004/07/FeiertagAPI")

    document:ET.ElementTree = ET.parse(url) # Geladene Seite in interne Datenstrukturen vom Typ ElementTree umwandeln 
    laender:ET.Element = document.getroot() # Ersten Knoten der Datei ("<ArrayOfBundesland xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/FeiertagAPI">" und alle Unterknoten öffnen)

    while True: # Endlosschleife
        value:str=input("Bitte geben Sie die Abkürzung des betroffenen Bundeslandes  ein: ").lower().replace(" ","")        # In Kleinbuchstaben umwandeln und Leerzeichen entfernen
        for land in laender:            # Prüfe alle Unterpunkte des Ersten Knotens (also <Bundesland>... siehe https://www.spiketime.de/feiertagapi/bundeslaender)
            if land.find("ft:Name",namespaces).text.lower()==value or land.find("ft:Abkuerzung",namespaces).text.lower()==value: # Jeweils den Text der Unter-Unterknoten <Abkuerzung> und <Name> mit der Eingabe vergleichen
                return str(land.find("ft:Abkuerzung",namespaces).text) # Wenn Treffer: Abkürzung als Ergebnis liefern (man kann also den vollen Namen oder eine Abkürzung eingeben; Groß- und Kleinschreibung sind egal)
        print("Dieses Bundesland ist unbekannt. Zulässige Eingabewerte sind:") # Sinnvolle Fehlermeldung mit Hinweis auf zulässige Eingaben
        for land in laender:
            print(f"{land.find('ft:Name',namespaces).text} ({land.find('ft:Abkuerzung',namespaces).text})") # Formatierte Liste: Für jedes Bundesland Name und dahinter in Klammern die Abkürzung
    return value

def getBundeslandLang(bundesLandKurz:str)->str:
    '''Abkürzung eines Bundeslandes in vollen Namen konvertieren über Zugriff auf Webservice'''
    url=urlopen(
            Request("https://www.spiketime.de/feiertagapi/bundeslaender",
            headers={"Accept": "application/xml"})        
        , data=None) # 
    
    # Wie oben: Lade aus dem Internet (urlopen) mit den VOrgaben unter Request (Adresse=URL und Header für gewünschten Inhaltstyp) und ohne zu übermittelnde Daten
    
    
    namespaces={'ft': 'http://schemas.datacontract.org/2004/07/FeiertagAPI'} # Wie oben: Verwendete Typbezeichnungen (siehe erste Zeile der Datei hinter xmlns)
    
    document:ET.ElementTree = ET.parse(url) # Abgerufene Datei in von Python verarbeitungsfähiges Objekt umwandeln (siehe oben)
    laender:ET.Element = document.getroot() # Ersten Knoten (hier: <ArrayofBundesland> aufrufen)


    for land in laender:            # Der Reihe nach alle Unterknoten öffnen
        if land.find("ft:Abkuerzung",namespaces).text==bundesLandKurz: # Den Unter-Unterknoten Abkürzung mit dem Parameter vergleichen (dieser ist schon richtig geschrieben, da wir bei Eingabe validiert haben)
            return str(land.find("ft:Name",namespaces).text) # Den langen Namen als Ergebnis zurückgeben
    return ""

def checkFeiertag(datum:date, bundesland:str, bundeslandLang:str)->str:
    '''Funktion, um zu prüfen, ob ein Tag ein Feiertag ist'''
    result:str=f"Der {datum.strftime('%d.%m.%Y')} ist in {bundeslandLang} kein Feiertag." # Standardtext (die meisten Tage sind keine Feiertage)
    url:urllib._UrlopenRet=urlopen(
        Request(f"https://www.spiketime.de/feiertagapi/feiertage/{bundesland}/{datum.year}",
        headers={"Accept": "application/xml"}), 
        data=None)
    # Zum dritten (und letzten) Mal: Abruf einer Datei aus dem Internet, aber diesmal von einer anderen Adresse. Die Adresse wird zusammengesetzt aus Bundesland und Jahr des zu prüfenden Datums.
    
    namespaces={'ft': 'http://schemas.datacontract.org/2004/07/FeiertagAPI'}
    # Auch diese Datei hat den gleichen Namespace, siehe auch dort die erste Zeile
    document:ET.ElementTree = ET.parse(url) # Wie oben: Gelesene Datei in interne Datenstruktur umwandeln
    feiertage:ET.Element = document.getroot() # Wie oben: Ersten Knoten aufrufen (hier: <ArrayofFeiertagDatum>, siehe https://www.spiketime.de/feiertagapi/feiertage/SN/2014)

    for feiertag in feiertage:        # Wie oben: Jeden Unterknoten (hier: <FeiertagDatum>) der Reihe nach durchlaufen
            feiertagDatum:date=datetime.strptime(feiertag.find('ft:Datum',namespaces).text[0:10],'%Y-%m-%d') # Die Daten in der XML-Datei haben ein anderes Format. Daher: 1. Die Uhrzeiten wegschneiden (nur die ersten zehn Zeichen nutzen - aus 2014-01-01T00:00:00 wird also 2014-01-01 und dann konvertieren mit der Formatvorgabe Jahr(vierstellig)-Monat-Date)
            if feiertagDatum==datum: # Zu suchendes Datum mit Datum aus der Feiertagsliste vergleichen
                return (f"Am {feiertagDatum.strftime('%d.%m.%Y')} ist in {bundeslandLang} ein Feiertag ({feiertag.find('ft:Feiertag/ft:Name',namespaces).text}).") # Wenn gefunden: Hinweis mit Namen des Feiertags zurückgeben. Die Datei hat den Namen in einem Unter-Unterknoten von <FeiertagDatum> versteckt  - sie steht nämlich unter <FeiertagDatum><Feiertag><Name> - den Unterpfad kann man mit dem / abrufen
                break
            if feiertagDatum>datum: # Da die Daten in der Datei chronologisch sortiert sind, kann abgebrochen werden, sobald das erste Datum nach der Eingabe liegt
                break 
    return result


print("\n\n Dieses Programm bestimmt, ob an einem bestimmten Tag in einem bestimmten Bundesland ein Feiertag war.")
print("Dazu wird auf die SpikeTime-Feiertag-API zurückgegriffen (https://www.spiketime.de/blog/spiketime-feiertag-api-feiertage-nach-bundeslandern/).")
print("-----\n\n")
while True:
    bundesland:str=getBundesLand() # Eingabefunktion für Bundesland aufrufen (siehe oben)
    datum:date=inputDate("Bitte geben Sie ein Datum ein: ") # Eingabefunktion für Datum aufrufen (siehe oben)
    print(checkFeiertag(datum,bundesland,getBundeslandLang(bundesland))) # Prüf- und Ergebnisfunktion aufrufen
    if(inputContinue()): # Prüfen, ob das Programm beendet werden soll
        break
    else:
        print("---------") # Zweite Runde mit Trennlinie vorbereiten
        print("\n")
