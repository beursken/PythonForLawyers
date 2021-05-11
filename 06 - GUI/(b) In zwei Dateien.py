# GUI-Test: Beispiel für eine grafische Benutzeroberfläche
# (C) 22.04.2021, Michael Beurskens

import sys   # Systemfunktionen: Erforderlich um Befehlszeilenparameter auszulesen und einen Rückgabewert zu liefern

from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox # Wichtige Funktionen für die grafische Benutzeroberfläche
from FensterDatei import Ui_Dialog # Selbst gestaltetete Oberfläche (generiert von QT Designer) - anders als bei "fenster.py" wurde diese hier in einer eigenen Datei ("Ui_GUI.py") gespeichert, so dass hier nur die eigenen Befehle stehen




# Funktionen, die auf Änderungen in der Oberfläche reagieren

def check():
    """Prüft, ob die Eingabe gültig ist"""
    if(ui.spinBox.value() > 0):              # Positiver Wert eingegeben
        ui.pushButton.setEnabled(True)       # Knopf wird aktiviert
    else:                                    # sonst (negativer Wert)
        ui.pushButton.setEnabled(False)     # Knopf wird deaktiviert


def update():
    """Aktualisiert die Liste und setzt das Eingabefeld zurück"""
    ui.textBrowser.insertPlainText(
        str(ui.spinBox.value())+"\n")   # Neue Zeile in die Textanzeige einfügen
    # Wert auf Null zurücksetzen
    ui.spinBox.setValue(0)
    ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
        (True))    # Ok-Knopf aktivieren


# Das eigentliche Programm beginnt hier

# Diese Zeile stellt sicher, dass die folgenden Befehle nur ausgeführt werden, wenn dieses Programm direkt gestartet (und nicht nur importiert) wird
if __name__ == '__main__':

    # Initialisiert die grafische Oberfläche und gibt ihr die zusätzlichen Argumente, die beim Start angegeben wurden
    app: QApplication = QApplication(sys.argv)
    w: QDialog = QDialog()   # Öffnet ein neues Fenster
    # Generiert die Inhalte des Fensters anhand der Vorgaben, die mit QT Designer erstellt wurden
    ui: Ui_Dialog = Ui_Dialog()
    ui.setupUi(w)  # Fügt die einzelnen Elemente zum Fenster hinzu

    # Funktionen des Programms
    ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
        (False))  # OK-Knopf deaktivieren
    # Bei Änderungen des Eingabefelds Knopf aktivieren oder deaktivieren
    ui.spinBox.valueChanged.connect(check)
    # Bei Anklicken des Knopfes Inhalt des Eingabefelds an Liste anhängen und OK-Knopf aktivieren
    ui.pushButton.clicked.connect(update)

    # Rückgabewert bei Schließen des Fensters durch Klick auf "OK" ausgeben
    w.accepted.connect(lambda: print("Ok"))
    # Rückgabewert bei Schließen des Fensters durch Klick auf "Abbrechen" ausgeben
    w.rejected.connect(lambda: print("Abbruch"))

    w.show()  # Fenster anzeigen

    # Beim Schließen des Fensters das Programm beenden und als Rückgabewert die Reaktion der grafischen Oberfläche weiterreichen
    sys.exit(app.exec_())
