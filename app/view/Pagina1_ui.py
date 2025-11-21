# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pagina1.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Pagina1(object):
    def setupUi(self, Pagina1):
        if not Pagina1.objectName():
            Pagina1.setObjectName(u"Pagina1")
        Pagina1.resize(881, 621)
        self.label = QLabel(Pagina1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 200, 121, 31))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)

        self.retranslateUi(Pagina1)

        QMetaObject.connectSlotsByName(Pagina1)
    # setupUi

    def retranslateUi(self, Pagina1):
        Pagina1.setWindowTitle(QCoreApplication.translate("Pagina1", u"Form", None))
        self.label.setText(QCoreApplication.translate("Pagina1", u"Ejemplo pagina 1", None))
    # retranslateUi

