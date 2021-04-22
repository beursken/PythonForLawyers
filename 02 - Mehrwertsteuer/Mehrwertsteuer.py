# Programm 01: Kostenquote nach §§ 91, 92 ZPO im Zweipersonenverhältnis
# (C) 13.04.2021, Michael Beurskens


print("Dieses Programm berechnet Preise mit und ohne Umsatzsteuer (Brutto und Nettopreise)")
betragText: str = input("Betrag (in Euro): ")
steuersatzText: str = input("Steuersatz (in Prozent): ")

betrag: float = round(float(betragText), 2)
steuersatz: float = round(float(steuersatzText), 2)
brutto: float = round(betrag*(100 + steuersatz)/100, 2)
netto: float = round(betrag / ((100 + steuersatz)/100), 2)
steuerBrutto: float = round(brutto-betrag, 2)
steuerNetto: float = round(betrag-netto, 2)
print("\n")
print("-----------------------------------------------------------------------")

print(f"{betrag:,.2f} € netto + {steuersatz}% \
Umsatzsteuer ({steuerBrutto:,.2f} €) = {brutto:,.2f} € brutto.")
print(f"{betrag:,.2f} € brutto = {netto:,.2f} € netto + {steuersatz}% \
Umsatzsteuer ({steuerNetto:,.2f} €).")
print("-----------------------------------------------------------------------")
