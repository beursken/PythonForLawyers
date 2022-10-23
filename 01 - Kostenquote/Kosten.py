# Programm 01: Kostenquote nach §§ 91, 92 ZPO im Zweipersonenverhältnis
# (C) 13.04.2021, Michael Beurskens

# Im Folgenden werden einige Variablen definiert, die wir später brauchen. Dies geschieht durch Angabe des Namens, 
# gefolgt von einem Doppelpunkt mit dem Typ und einem Gleichheitszeichen mit dem Wert

streitwert: float = 0
erfolg: float = 0
unterliegen: float = 0
kostenKlaeger: float = 0
kostenBeklagter: float = 0
# Noch ein Kommentar


# Mit der Funktion print() kann man Texte ausgeben. Diese stehen in Anführungszeichen.
print("Dieses Programm berechnet die Kostenquote nach §§ 91, 92 ZPO im Zweipersonenverhältnis")

# Mit der Funktion input() kann man Texte, die über die Tastatur eingegeben werden, in eine Variable speichern. Dazu schreibt man einfach Variablenname : str = input().
eingabeStreitwert: str = input("Wie hoch ist der Streitwert (in Euro)? ")
eingabeErfolg: str = input(
    "In welchem Umfang war die Klage erfolgreich (in Euro)? ")

# Man kann Werte umwandeln (etwa einen Text in eine Zahl), indem man den gewünschten Typ vor eine Variable setzt und diese in Klammern dahinterschreibt, also z.B. int(jahr), str(zahl)
streitwert = float(eingabeStreitwert)
erfolg = float(eingabeErfolg)
unterliegen = streitwert-erfolg
kostenKlaeger = round((streitwert-erfolg)/streitwert*100, 2)
kostenBeklagter = 100-kostenKlaeger

# Wenn man \n im Rahmen eines print()-Befehls eingibt, wird eine leere Zeile ("Absatz") ausgegeben
print("\n")
print("-----------------------------------------------------------------------")

# Hier folgt jetzt eine etwas kompliziertere Ausgabe. Dabei ist folgendes zu beachten:
# 1. Wenn eine Zeile zu lang wird, kann man diese mit einem Backslash (Alt Gr+ ß) in der nächsten Zeile fortsetzen.
# 2. Wenn man ein Prozentzeichen in einem Text angibt, wird dieses durch Wert ersetzt, die man nach dem Text auflistet.
# 3. Wenn man hinter dem Prozentzeichen %f angibt, weiß der Computer, dass eine Gleitkommazahl gewünscht ist.
# 4. Wenn man hinter dem Prozentzeichen %.2f angibt, weiß der Computer, dass hinter dem Punkt (Komma) nur zwei Ziffern stehen sollen (der Rest fällt ohne Rundung weg)
# 5. Wenn es in einem Text mehrere Lücken gibt, werden die einzufügenden Werte in einer Klammer hinter dem Text angegeben
print("Die Kosten des Rechtsstreits trägt der Kläger zu %.2f / %.2f \
und der Beklagte zu %.2f / %.2f." % (unterliegen, streitwert, erfolg, streitwert))
print("\n")
print("- oder (alternativer Tenor) -")
print("\n")
print("Die Kosten des Rechtsstreits trägt der Kläger zu %.2f Prozent \
und der Beklagte zu %.2f Prozent." % (kostenKlaeger, kostenBeklagter))
print("-----------------------------------------------------------------------")
