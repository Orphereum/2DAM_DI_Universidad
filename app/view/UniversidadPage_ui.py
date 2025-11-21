# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UniversidadPage.ui'
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

class Ui_UniversidadPage(object):
    def setupUi(self, UniversidadPage):
        if not UniversidadPage.objectName():
            UniversidadPage.setObjectName(u"UniversidadPage")
        UniversidadPage.resize(881, 621)
        self.label = QLabel(UniversidadPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 100, 161, 61))

        self.retranslateUi(UniversidadPage)

        QMetaObject.connectSlotsByName(UniversidadPage)
    # setupUi

    def retranslateUi(self, UniversidadPage):
        UniversidadPage.setWindowTitle(QCoreApplication.translate("UniversidadPage", u"Form", None))
        self.label.setText(QCoreApplication.translate("UniversidadPage", u"Ventana universidad", None))
    # retranslateUi

