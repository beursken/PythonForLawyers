# Programm 03: Blutalkoholkonzentration nach der Widmark-Formel
# (C) 20.04.2021, Michael Beurskens

alkoholDichte: float = 0.8
print("Dieses Programm berechnet die Alkoholkonzentration im Blut nach der sog. Widmark-Formel.")
print("\n")
volumenText: str = input("Wie viel Milliliter haben Sie getrunken? ")
alkoholText: str = input("Wie viel Alkohol enthielt das Getränk in Prozent? ")
gewichtText: str = input("Wie viel wiegen Sie in Kilogramm? ")
resorptionText: str = input("Geben Sie jetzt den sog. Verteilungsfaktor ein - \
dieser beträgt für Männer 0.7, für Frauen 0.6 oder für Kinder 0.8: ")

volumen: float = float(volumenText)
alkohol: float = float(alkoholText)/100
gewicht: float = float(gewichtText)
resorption: float = float(resorptionText)
alkoholMasse: float = volumen*alkohol*alkoholDichte
blutalkohol: float = alkoholMasse/(gewicht*resorption)
print("\n")
print("---------------------------------------------------")
print("Masse aufgenommenen Alkohols = Getränkemenge in Milliliter * Alkoholvolum in Prozent * Dichte von Alkohol")
print("<=> %.2f g = %.2f ml * %.2f %% * %.2f g/ml" %
      (alkoholMasse, volumen, alkohol*100, alkoholDichte))
print("\n")
print("Promille im Körper = Masse aufgenommenen Alkohols / (Gewicht * Verteilungsfaktor)")
print("<=> %.2f ‰ = %.2f g / (%.2f kg * %.2f)" %
      (blutalkohol, alkoholMasse, gewicht, resorption))
print("---------------------------------------------------")
