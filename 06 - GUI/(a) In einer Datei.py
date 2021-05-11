# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designeravlkQV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################



# Die folgenden Zeilen laden bestimmte (notwendige) Klassen, um grafische Oberflächen anzuzeigen
# Sie müssen diese nicht selber schreiben, da sie von QT-Designer automatisch erstellt werdne
from PyQt5.QtCore import * # Alle Klassen aus QtCore importieren, so dass man sie benutzen kann
from PyQt5.QtGui import *  # Alle Klassen aus QtGui importieren, so dass man sie benutzen kann
from PyQt5.QtWidgets import * # Alle Klassen aus QtWidgets importieren, so dass man sie benutzen kann
import sys


# Diesen Teil des Programms erstellt QT-Designer automatisch; am Besten hier nichts ändern!
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(668, 595)
        Dialog.setAutoFillBackground(True)
        self.knopf = QPushButton(Dialog)
        self.knopf.setObjectName(u"knopf")
        self.knopf.setGeometry(QRect(410, 130, 75, 23))
        self.knopf.setAutoDefault(True)
        self.knopf.setFlat(False)
        self.eingabeExamensnote = QLineEdit(Dialog)
        self.eingabeExamensnote.setObjectName(u"eingabeExamensnote")
        self.eingabeExamensnote.setGeometry(QRect(30, 130, 381, 20))
        self.ausgabefeld = QTextBrowser(Dialog)
        self.ausgabefeld.setObjectName(u"ausgabefeld")
        self.ausgabefeld.setGeometry(QRect(30, 160, 461, 281))
        self.ausgabefeld.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ausgabefeld.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.knopf.setText(QCoreApplication.translate("Dialog", u"Anzeigen", None))
        self.eingabeExamensnote.setText("")
        self.eingabeExamensnote.setPlaceholderText(QCoreApplication.translate("Dialog", u"Examensnote eingeben", None))
    # retranslateUi


def knopfGedrueckt():
    fenster.ausgabefeld.insertPlainText(fenster.eingabeExamensnote.text())




# Das ist das eigentliche Programm. Die folgenden Befehle müssen Sie *immer* bei grafischen Anwendungen ausführen. Nur der Name des Fensters ist ggf. ein anderer (hier heißt es Ui_Dialog, den Namen können Sie aber in QT-Designer anpassen)
# Die eigentlichen Knöpfe etc. positionieren Sie mit QT Designer. Dadurch ändert sich nur der Teil oben, nicht aber die folgenden vier Zeilen. Merken Sie sich also diese Zeilen!

app :QApplication = QApplication(sys.argv) # Anwendung initialisieren (für Sie unsichtbar - alle Parameter von Python weiterleiten)
x:QDialog=QDialog() # Fenster erstellen - QDialog ist eine Klasse von QT; wie diese funktioniert kann Ihnen egal sein. Kurz gesagt erstellt diese Zeile eine leere Seite, in die man Inhalte (die Sie in QT-Designer definiert haben) laden kann
fenster: Ui_Dialog = Ui_Dialog() # konkretes Objekt mit dem oben definierten Fensterinhalt erstellen
fenster.setupUi(x) # Fensterinhalt in das Fenster einfügen - das heißt, der gesamte Programmcode von oben (den QT-Designer erstellt hat) wird ausgeführt. Dadurch werden z.B. Eingabefelder, Knöpfe etc. eingefügt


# An dieser Stelle kommt der eigentliche Funktionsteil des Programms. Hier programmieren Sie sog. "Ereignisse" (Events), d.h. was passiert, wenn der Nutzer etwas macht
fenster.knopf.clicked.connect(knopfGedrueckt) # Dies verknüpft (connect) das Ereignis "clicked" (angeklickt) des Objekts "knopf" im Objekt "fenster" (siehe oben im von QT-Designer erstellten Programmcode: self.knopf = QPushButton(Dialog)) mit einer Funktion "knopfGedrueckt", die Sie oben mit def erstellt haben
#fenster.eingabeExamensnote.textChanged.connect(knopfGedrueckt) # Diese Zeile verknüpft (connect) das Ereignis "textChanged" des Objekts "eingabeEamensnote" im Objekt "fenster" (siehe oben  im von QT-Designer erstellten Programmcode: self.eingabeExamensnote = QLineEdit(Dialog)) mit einer Funktion "knopfGedrueckt", die Sie oben mit def erstellt haben


x.show() # Fenster anzeigen (dies erfolgt immer als vorletzter Schritt - vergessen Sie diesen Befehl, ist ihr Programm "unsichtbar" und damit nutzlos)
sys.exit(app.exec()) # Programm bis zum bitteren Ende ausführen (und am Ende den Rückgabewert von QT zurückliefern)