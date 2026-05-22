# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClasesPage.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(883, 631)
        self.lblTitulo = QLabel(Form)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setGeometry(QRect(20, 20, 271, 41))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.tblClases = QTableWidget(Form)
        if (self.tblClases.columnCount() < 4):
            self.tblClases.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblClases.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblClases.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblClases.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblClases.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblClases.setObjectName(u"tblClases")
        self.tblClases.setGeometry(QRect(30, 150, 831, 371))
        self.tblClases.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 110, 336, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnCrear = QPushButton(self.widget)
        self.btnCrear.setObjectName(u"btnCrear")

        self.horizontalLayout.addWidget(self.btnCrear)

        self.btnEditar = QPushButton(self.widget)
        self.btnEditar.setObjectName(u"btnEditar")

        self.horizontalLayout.addWidget(self.btnEditar)

        self.btnBorrar = QPushButton(self.widget)
        self.btnBorrar.setObjectName(u"btnBorrar")

        self.horizontalLayout.addWidget(self.btnBorrar)

        self.btnRefrescar = QPushButton(self.widget)
        self.btnRefrescar.setObjectName(u"btnRefrescar")

        self.horizontalLayout.addWidget(self.btnRefrescar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblTitulo.setText(QCoreApplication.translate("Form", u"Gestion de Clases", None))
        ___qtablewidgetitem = self.tblClases.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tblClases.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem2 = self.tblClases.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Capacidad", None));
        ___qtablewidgetitem3 = self.tblClases.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Edificio", None));
        self.btnCrear.setText(QCoreApplication.translate("Form", u"Crear", None))
        self.btnEditar.setText(QCoreApplication.translate("Form", u"Editar", None))
        self.btnBorrar.setText(QCoreApplication.translate("Form", u"Borrar", None))
        self.btnRefrescar.setText(QCoreApplication.translate("Form", u"Refrescar", None))
    # retranslateUi

