# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EdificioPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_EdificioPage(object):
    def setupUi(self, EdificioPage):
        if not EdificioPage.objectName():
            EdificioPage.setObjectName(u"EdificioPage")
        EdificioPage.resize(838, 550)
        self.layoutWidget = QWidget(EdificioPage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 90, 661, 91))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblNombre = QLabel(self.layoutWidget)
        self.lblNombre.setObjectName(u"lblNombre")
        font = QFont()
        font.setPointSize(15)
        self.lblNombre.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.leNombre = QLineEdit(self.layoutWidget)
        self.leNombre.setObjectName(u"leNombre")
        self.leNombre.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leNombre)

        self.lblFacultad = QLabel(self.layoutWidget)
        self.lblFacultad.setObjectName(u"lblFacultad")
        self.lblFacultad.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblFacultad)

        self.cbFacultad = QComboBox(self.layoutWidget)
        self.cbFacultad.setObjectName(u"cbFacultad")
        self.cbFacultad.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cbFacultad)

        self.lblTitulo = QLabel(EdificioPage)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setGeometry(QRect(90, 30, 211, 61))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        self.lblTitulo.setFont(font1)
        self.layoutWidget1 = QWidget(EdificioPage)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(90, 190, 661, 341))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableEdificios = QTableWidget(self.layoutWidget1)
        self.tableEdificios.setObjectName(u"tableEdificios")
        font2 = QFont()
        font2.setPointSize(13)
        self.tableEdificios.setFont(font2)

        self.verticalLayout.addWidget(self.tableEdificios)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAnadir = QPushButton(self.layoutWidget1)
        self.btnAnadir.setObjectName(u"btnAnadir")
        self.btnAnadir.setMinimumSize(QSize(0, 35))
        self.btnAnadir.setMaximumSize(QSize(191, 16777215))
        self.btnAnadir.setFont(font2)

        self.horizontalLayout.addWidget(self.btnAnadir)

        self.btnEliminar = QPushButton(self.layoutWidget1)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setMinimumSize(QSize(0, 35))
        self.btnEliminar.setMaximumSize(QSize(191, 16777215))
        self.btnEliminar.setFont(font2)

        self.horizontalLayout.addWidget(self.btnEliminar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnEditar = QPushButton(self.layoutWidget1)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setMinimumSize(QSize(0, 35))
        self.btnEditar.setMaximumSize(QSize(191, 16777215))
        self.btnEditar.setFont(font2)

        self.horizontalLayout_2.addWidget(self.btnEditar)

        self.btnRefrescar = QPushButton(self.layoutWidget1)
        self.btnRefrescar.setObjectName(u"btnRefrescar")
        self.btnRefrescar.setMinimumSize(QSize(0, 35))
        self.btnRefrescar.setMaximumSize(QSize(191, 16777215))
        self.btnRefrescar.setFont(font2)

        self.horizontalLayout_2.addWidget(self.btnRefrescar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.btnGenerarInforme = QPushButton(EdificioPage)
        self.btnGenerarInforme.setObjectName(u"btnGenerarInforme")
        self.btnGenerarInforme.setGeometry(QRect(550, 40, 191, 41))
        self.btnGenerarInforme.setMinimumSize(QSize(0, 35))
        self.btnGenerarInforme.setMaximumSize(QSize(191, 16777215))
        self.btnGenerarInforme.setFont(font2)

        self.retranslateUi(EdificioPage)

        QMetaObject.connectSlotsByName(EdificioPage)
    # setupUi

    def retranslateUi(self, EdificioPage):
        EdificioPage.setWindowTitle(QCoreApplication.translate("EdificioPage", u"Form", None))
        self.lblNombre.setText(QCoreApplication.translate("EdificioPage", u"Nombre:", None))
        self.lblFacultad.setText(QCoreApplication.translate("EdificioPage", u"Facultad: ", None))
        self.lblTitulo.setText(QCoreApplication.translate("EdificioPage", u"Edificios", None))
        self.btnAnadir.setText(QCoreApplication.translate("EdificioPage", u"A\u00f1adir", None))
        self.btnEliminar.setText(QCoreApplication.translate("EdificioPage", u"Eliminar", None))
        self.btnEditar.setText(QCoreApplication.translate("EdificioPage", u"Editar", None))
        self.btnRefrescar.setText(QCoreApplication.translate("EdificioPage", u"Refrescar Tabla", None))
        self.btnGenerarInforme.setText(QCoreApplication.translate("EdificioPage", u"Generar Informe PDF", None))
    # retranslateUi

