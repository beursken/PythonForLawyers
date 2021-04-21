# Programm 01: Kostenquote nach §§ 91, 92 ZPO im Zweipersonenverhältnis
# (C) 13.04.2021, Michael Beurskens

streitwert:float = 0
erfolg:float = 0
unterliegen:float = 0
kostenKlaeger:float = 0
kostenBeklagter:float = 0

print("Dieses Programm berechnet die Kostenquote nach §§ 91, 92 ZPO im Zweipersonenverhältnis")
eingabeStreitwert:str=input("Wie hoch ist der Streitwert (in Euro)? ")
eingabeErfolg:str=input("In welchem Umfang war die Klage erfolgreich (in Euro)? ")

streitwert = float(eingabeStreitwert)
erfolg = float(eingabeErfolg)
unterliegen = streitwert-erfolg
kostenKlaeger=round((streitwert-erfolg)/streitwert*100,2)
kostenBeklagter=100-kostenKlaeger
print("\n")
print("-----------------------------------------------------------------------")
print("Die Kosten des Rechtsstreits trägt der Kläger zu %.2f / %.2f \
und der Beklagte zu %.2f / %.2f." % (unterliegen,streitwert,erfolg,streitwert))
print("\n")
print("- oder (alternativer Tenor) -")
print("\n")
print("Die Kosten des Rechtsstreits trägt der Kläger zu %.2f Prozent \
und der Beklagte zu %.2f Prozent." %(kostenKlaeger,kostenBeklagter))

print("-----------------------------------------------------------------------")