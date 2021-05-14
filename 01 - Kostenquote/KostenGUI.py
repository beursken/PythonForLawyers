# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'designeravlkQV.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


# Die folgenden Zeilen laden bestimmte (notwendige) Klassen, um grafische Oberflächen anzuzeigen
# Sie müssen diese nicht selber schreiben, da sie von QT-Designer automatisch erstellt werdne

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import locale


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1107, 640)
        self.action_Beenden = QAction(MainWindow)
        self.action_Beenden.setObjectName(u"action_Beenden")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.erklaerung = QLabel(self.centralwidget)
        self.erklaerung.setObjectName(u"erklaerung")
        self.erklaerung.setTextFormat(Qt.PlainText)
        self.erklaerung.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.erklaerung)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.antrag = QComboBox(self.centralwidget)
        self.antrag.setObjectName(u"antrag")
        self.antrag.setEditable(True)

        self.horizontalLayout.addWidget(self.antrag)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.erfolg = QComboBox(self.centralwidget)
        self.erfolg.setObjectName(u"erfolg")
        self.erfolg.setEditable(True)

        self.horizontalLayout.addWidget(self.erfolg)

        self.berechnen = QPushButton(self.centralwidget)
        self.berechnen.setObjectName(u"berechnen")
        self.berechnen.setAutoDefault(True)
        self.berechnen.setEnabled(False)

        self.horizontalLayout.addWidget(self.berechnen)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.fehlermeldung = QLabel(self.centralwidget)
        self.fehlermeldung.setObjectName(u"fehlermeldung")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fehlermeldung.setFont(font)
        self.fehlermeldung.setStyleSheet(u"color:rgb(170, 0, 0)")
        self.fehlermeldung.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.fehlermeldung)

        self.ergebnis = QTextBrowser(self.centralwidget)
        self.ergebnis.setObjectName(u"ergebnis")
        self.verticalLayout.addWidget(self.ergebnis)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1107, 21))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menuDatei.addAction(self.action_Beenden)

        self.retranslateUi(MainWindow)

        self.berechnen.setDefault(True)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Kostenrechner", None))
        self.action_Beenden.setText(
            QCoreApplication.translate("MainWindow", u"&Beenden", None))
        self.erklaerung.setText(QCoreApplication.translate(
            "MainWindow", u"Dieses Programm berechnet die Kostenquote für eine Klage eines Klägers gegen einen Beklagten (ohne Widerklage oder Streitgenossenschaft).", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Beantragter Betrag:", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Zugesprochener Betrag:", None))
        self.berechnen.setText(QCoreApplication.translate(
            "MainWindow", u"Kostenquote berechnen", None))
        self.fehlermeldung.setText("")
        self.menuDatei.setTitle(QCoreApplication.translate(
            "MainWindow", u"&Datei", None))
    # retranslateUi


# Ab hier beginnt das eigentliche Programm


# Hilfsfunktion: Größten gemeinsamen Teiler berechnen

def ggt(wert1: int, wert2: int) -> int:
    '''Euklidischer Algorithmus (https://de.wikipedia.org/wiki/Euklidischer_Algorithmus) zur Berechnung des größten gemeinsamen Teilers'''
    # Muss man nicht auswendig können, sondern kann man bei Bedarf nachschlagen!
    while wert2 != 0:
        temp: int = wert1 % wert2
        wert1 = wert2
        wert2 = temp
    return wert1

# Prüffunktionen zur Validierung der Eingabe

def pruefeEuro(betrag: str, feld: str) -> bool:
    '''Prüfen, ob ein Textwert einen gültigen Euro-Betrag darstellt; ggf. Fehlermeldung mit Angabe des betroffenen Feldes'''
    try:
        betragZahl: float = float(betrag.replace(",", "."))
        if(betragZahl < 0):
            fenster.fehlermeldung.setText(
                f"Bitte eine positive Zahl im Feld {feld} eingeben (Euro-Beträge können nicht negativ sein).")
            return False
        # Wenn bei Runden eine Nachkommastelle wegfällt, hat die Zahl offenbar mehr als zwei Nachkommastellen
        elif (round(betragZahl, 2) != betragZahl):
            fenster.fehlermeldung.setText(
                f"Bitte maximal zwei Nachkommastellen  im Feld {feld} eingeben (ein Euro hat 100 Cent).")
            return False
        else:
            return True
    except:
        fenster.fehlermeldung.setText(
            f"Bitte einen Eurobetrag  im Feld {feld} eingeben.")
        return False


def erfolgKleinerAntrag() -> bool:
    '''Prüfen, ob Erfolg kleiner als der Antrag ist'''
    streitwert = float(fenster.antrag.currentText().replace(",", "."))
    erfolg = float(fenster.erfolg.currentText().replace(",", "."))
    if(erfolg > streitwert):
        fenster.fehlermeldung.setText(
            f"Der Erfolg muss kleiner oder gleich dem Antrag sein.")
        return False
    return True



# Reaktionen auf Ereignisse (d.h. Änderungen in der Benutzeroberfläche wie Knöpfe, die angeklickt werden oder Felder, die ausgefüllt werden)

def changed():
    '''Bei Eingabe: Prüfen, ob Eingabe in beiden Eingabefelder gültig ist, so dass der Berechnen-Knopf aktiviert werden kann'''
    fenster.fehlermeldung.setText("")  # Text im Feld Fehlermeldung löschen
    fenster.berechnen.setEnabled(False)  # Berechnen-Knopf deaktivieren
    if pruefeEuro(fenster.antrag.currentText(), "Antrag") and pruefeEuro(fenster.erfolg.currentText(), "Erfolg") and erfolgKleinerAntrag():
        # Berechnen-Knopf aktivieren, wenn alles in Ordnung ist
        fenster.berechnen.setEnabled(True)


def knopfGedrueckt():
    '''Berechnung durchführen und Ergebnis anzeigen'''
    streitwert: float = float(fenster.antrag.currentText().replace(",", "."))
    erfolg: float = float(fenster.erfolg.currentText().replace(",", "."))
    unterliegen: float = streitwert-erfolg
    kostenKlaeger: float = round((streitwert-erfolg)/streitwert*100, 2)
    kostenBeklagter: float = 100-kostenKlaeger



    # Das folgende ist neu: Die Brüche werden jetzt gekürzt und vor allem als ganze Zahlen ausgewertet (d.h. nicht mehr 32,12/400,74)
    kostenKlaegerNenner: int = int(
        streitwert*100/ggt(int(unterliegen*100), int(streitwert*100))) # Um schöne Brüche auszugeben, kürzen wir automatisch
    kostenKlaegerZaehler: int = int(
        unterliegen*100/ggt(int(unterliegen*100), int(streitwert*100))) # Um schöne Brüche auszugeben, kürzen wir automatisch
    kostenBeklagterZaehler: int = int(
        erfolg*100/ggt(int(erfolg*100), int(streitwert*100))) # Um schöne Brüche auszugeben, kürzen wir automatisch
    kostenBeklagterNenner: int = int(
        streitwert*100/ggt(int(erfolg*100), int(streitwert*100)))  # Um schöne Brüche auszugeben, kürzen wir automatisch
    
    
    
    
    fenster.ergebnis.append("<h3>Streitwertberechnung</h3>") # Hier wird der Text als HTML eingefügt - das erlaubt Formatierungen (z.B. im konkreten Fall als h3 = Überschrift 3)

    fenster.ergebnis.append( 
        f"<p><i>Kläger hat <b>{locale.currency(streitwert)}</b> beantragt, ihm wurden <b>{locale.currency(erfolg)}</b> zugesprochen.</i></p><br/><br/>")
#Die beiden Geldbeträge werden automatisch von Python richtig (Kommazahl, Euro) formatiert, wenn man die entsprechenden Zahlen an die Funktion locale.currency übergibt - diese wandelt also jede Zahl in einen String um, der diese als Euro-Betrag ausgibt

    if kostenKlaeger < 10:    # Bei weniger als 10% der Kosten wenden die Gerichte in der Praxis § 92 Abs. 2 Nr. 2 ZPO an und legen die Kosten einer Partei allein auf
        fenster.ergebnis.append(
            "<p style='font-family:courier'>Die Kosten des Verfahrens trägt der Beklagte.</p>")
        if kostenKlaeger > 0:  # Klarstellender Hinweis ist nur relevant, falls der Kläger überhaupt irgendwelche Kosten tragen würde
            fenster.ergebnis.append(
                f"<br/><p style=\"color:silver\"><i>(beachten Sie <b class=\"color:black\">§ 92 Abs. 2 Nr. 2 ZPO</b> - hier müsste der Kläger sonst (nur) <b class=\"color:black\">{locale.format_string('%.2g',kostenKlaeger)}%</b> der Kosten tragen).</i></p>")
    elif kostenBeklagter < 10: # Bei weniger als 10% der Kosten wenden die Gerichte in der Praxis § 92 Abs. 2 Nr. 2 ZPO an und legen die Kosten einer Partei allein auf
        fenster.ergebnis.append(
            "<p  style='font-family:courier'>Die Kosten des Verfahrens trägt der Kläger.</p>")
        if kostenBeklagter > 0: # Klarstellender Hinweis ist nur relevant, falls der Beklagte überhaupt irgendwelche Kosten tragen würde
            fenster.ergebnis.append(
                f"<br/><p style=\"color:silver\"><i>(beachten Sie <b class=\"color:black\">§ 92 Abs. 2 Nr. 2 ZPO</b> - hier müsste der Beklagte sonst (nur) <b  class=\"color:black\">{locale.format_string('%.2g',kostenBeklagter)}%</b> der Kosten tragen).</i></p>")
    else:
        fenster.ergebnis.append(
            f"<p style='font-family:courier'>Die Kosten des Rechtsstreits trägt der Kläger zu <b>{kostenKlaegerZaehler}</b> / <b>{kostenKlaegerNenner}</b> und der Beklagte zu <b>{kostenBeklagterZaehler}</b> / <b>{kostenBeklagterNenner}</b>.</p>")
        fenster.ergebnis.append(
            "<br/><br/><p style=\"color:silver\">- oder (alternativer Tenor) -</p><br/><br/>")
        fenster.ergebnis.append(
            f"<p style='font-family:courier'>Die Kosten des Rechtsstreits trägt der Kläger zu <b>{locale.format_string('%.2g',kostenKlaeger)}%</b> und der Beklagte zu <b>{locale.format_string('%.2g',kostenBeklagter)}%</b> Prozent.</p>")
    fenster.ergebnis.append("<hr/><br/><br/>")

    # Fügt die Eingabe für den Antrag in die Archivliste des Eingabefeldes ein (falls man denselben Betrag noch einmal benötigt)
    fenster.antrag.addItem(fenster.antrag.currentText())
    # Fügt die Eingabe für den Erfolg in die Archivliste  des Eingabefeldes ein (falls man denselben Betrag noch einmal benötigt)
    fenster.erfolg.addItem(fenster.erfolg.currentText())
    # Löscht den bisherigen Text im Eingabefeld für den Antrag
    fenster.antrag.setCurrentText("")
    # Löscht den bisherigen Text im Eingabefeld für den Erfolg
    fenster.erfolg.setCurrentText("")
    # Bewirkt, dass das Eingabefeld für den Antrag wieder aktiv wird (d.h., dass Sie dort als nächstes Text eingeben sollen)
    fenster.antrag.setFocus()


# Das ist das eigentliche Programm. Die folgenden Befehle müssen Sie *immer* bei grafischen Anwendungen ausführen. Nur der Name des Fensters ist ggf. ein anderer (hier heißt es Ui_Dialog, den Namen können Sie aber in QT-Designer anpassen)
# Die eigentlichen Knöpfe etc. positionieren Sie mit QT Designer. Dadurch ändert sich nur der Teil oben, nicht aber die folgenden vier Zeilen. Merken Sie sich also diese Zeilen!


locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8') # Deutsche Formatierung für Währungen und Kommazahlen


# Anwendung initialisieren (für Sie unsichtbar - alle Parameter von Python weiterleiten)
app: QApplication = QApplication(sys.argv)
x: QMainWindow = QMainWindow()  # Fenster erstellen - QMainWindow ist eine Klasse von QT; wie diese funktioniert kann Ihnen egal sein. Kurz gesagt erstellt diese Zeile eine leere Seite, in die man Inhalte (die Sie in QT-Designer definiert haben) laden kann
# konkretes Objekt mit dem oben definierten Fensterinhalt erstellen
fenster: Ui_MainWindow = Ui_MainWindow()
fenster.setupUi(x)  # Fensterinhalt in das Fenster einfügen - das heißt, der gesamte Programmcode von oben (den QT-Designer erstellt hat) wird ausgeführt. Dadurch werden z.B. Eingabefelder, Knöpfe etc. eingefügt

# Die folgenden beiden Funktionen dienen der Überprüfung der Eingabe, während Tasten im Feld gedrückt werden
# Dies verknüpft (connect) das Ereignis "editTextChanged" (Text geändert) des Objekts "antrag" im Objekt "fenster" (siehe oben im von QT-Designer erstellten Programmcode: self.knopf = QPushButton(Dialog)) mit einer Funktion "changed", die Sie oben mit def erstellt haben
fenster.antrag.editTextChanged.connect(changed)
# Dies verknüpft (connect) das Ereignis "editTextChanged" (Text geändert) des Objekts "erfolg" im Objekt "fenster" (siehe oben im von QT-Designer erstellten Programmcode: self.knopf = QPushButton(Dialog)) mit einer Funktion "changed", die Sie oben mit def erstellt haben
fenster.erfolg.editTextChanged.connect(changed)

# Die folgende Zeile dient dem Beenden des Programms, wenn der entsprechende Menüeintrag gewählt wurde
fenster.action_Beenden.triggered.connect(quit)

# An dieser Stelle kommt der eigentliche Funktionsteil des Programms. Hier programmieren Sie sog. "Ereignisse" (Events), d.h. was passiert, wenn der Nutzer etwas macht
# Dies verknüpft (connect) das Ereignis "clicked" (angeklickt) des Objekts "berechnen" im Objekt "fenster" (siehe oben im von QT-Designer erstellten Programmcode: self.knopf = QPushButton(Dialog)) mit einer Funktion "knopfGedrueckt", die Sie oben mit def erstellt haben
fenster.berechnen.clicked.connect(knopfGedrueckt)


x.show()  # Fenster anzeigen (dies erfolgt immer als vorletzter Schritt - vergessen Sie diesen Befehl, ist ihr Programm "unsichtbar" und damit nutzlos)
# Programm bis zum bitteren Ende ausführen (und am Ende den Rückgabewert von QT zurückliefern)
sys.exit(app.exec())
