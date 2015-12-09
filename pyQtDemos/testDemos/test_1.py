#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time 

'''
class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)
        self.connect(dial, SIGNAL("valueChanged(int)"),spinbox.setValue)
        self.connect(spinbox, SIGNAL("valueChanged(int)"),dial.setValue)
        self.setWindowTitle("Signals and Slots")
'''



class form(QDialog):
    def __init__(self, parent=None):
        super(form, self).__init__(parent)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        buttonBox.button(QDialogButtonBox.Ok).setDefault(True)
        self.layout = QHBoxLayout()
        self.layout.addWidget(buttonBox)
        self.setLayout(self.layout)
        
        
        

        

if __name__ == '__main__':

    import sys
    import time 
    app = QApplication(sys.argv)
    f = form()
    f.show()
    app.exec_()
