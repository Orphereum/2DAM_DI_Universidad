# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Departamento.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QSizePolicy,
    QTableView, QWidget)

class Ui_Departamento(object):
    def setupUi(self, Departamento):
        if not Departamento.objectName():
            Departamento.setObjectName(u"Departamento")
        Departamento.resize(881, 621)
        self.horizontalLayoutWidget = QWidget(Departamento)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(19, 19, 851, 331))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.horizontalLayoutWidget)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout.addWidget(self.tableView)

        self.tableView_2 = QTableView(self.horizontalLayoutWidget)
        self.tableView_2.setObjectName(u"tableView_2")

        self.horizontalLayout.addWidget(self.tableView_2)


        self.retranslateUi(Departamento)

        QMetaObject.connectSlotsByName(Departamento)
    # setupUi

    def retranslateUi(self, Departamento):
        Departamento.setWindowTitle(QCoreApplication.translate("Departamento", u"Form", None))
    # retranslateUi

