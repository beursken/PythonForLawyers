# Example for designing a graphical User Interface using QT-Designer and PyQT5

This folder requires installation of 
* PYQT5 (pip3 install pyqt5)
* PYQT5-tools (pip3 install pyqt5-tools)

It is recommended to use the PyQT Integration Extension by Feng Zhou (https://marketplace.visualstudio.com/items?itemName=zhoufeng.pyqt-integration) and setup paths in @ext:zhoufeng.pyqt-integration (Settings / Extensions / PYQT-Integration) - this allows for direct compilation of QT-Designer-files in Visual Studio (and one click editing of UI-files in Designer). It is also possible to Copy & Paste Code from Designer itself (but unnecessarily cumbersome).

This directory includes two versions of the example (with identical code and functionality, but a different split among files to illustrate imports):
* (a) In einer Datei.py (UI and code in a single file)
* (b) In zwei Dateien.py (UI in a separate file, FensterDatei.py)

The program itself does nothing exciting (It copies text from the input field to the textlister at the bottom). It is meant to illustrate how to transfer text-based tools to GUI (which is the homework for the following week)