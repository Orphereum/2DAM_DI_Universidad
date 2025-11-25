# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DepartamentoPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_Departamento(object):
    def setupUi(self, DepartamentoPage):
        if not DepartamentoPage.objectName():
            DepartamentoPage.setObjectName(u"DepartamentoPage")
        DepartamentoPage.resize(879, 621)
        self.horizontalLayoutWidget = QWidget(DepartamentoPage)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 19, 861, 331))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tablaFacultades = QTableView(self.horizontalLayoutWidget)
        self.tablaFacultades.setObjectName(u"tablaFacultades")

        self.horizontalLayout.addWidget(self.tablaFacultades)

        self.tablaDepartamentos = QTableView(self.horizontalLayoutWidget)
        self.tablaDepartamentos.setObjectName(u"tablaDepartamentos")

        self.horizontalLayout.addWidget(self.tablaDepartamentos)

        self.horizontalLayoutWidget_2 = QWidget(DepartamentoPage)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(450, 360, 421, 41))
        self.horizontalBotones = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalBotones.setObjectName(u"horizontalBotones")
        self.horizontalBotones.setContentsMargins(0, 0, 0, 0)
        self.btnAgregar = QPushButton(self.horizontalLayoutWidget_2)
        self.btnAgregar.setObjectName(u"btnAgregar")

        self.horizontalBotones.addWidget(self.btnAgregar)

        self.btnEliminar = QPushButton(self.horizontalLayoutWidget_2)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.horizontalBotones.addWidget(self.btnEliminar)

        self.btnEditar = QPushButton(self.horizontalLayoutWidget_2)
        self.btnEditar.setObjectName(u"btnEditar")

        self.horizontalBotones.addWidget(self.btnEditar)

        self.btnActualizar = QPushButton(self.horizontalLayoutWidget_2)
        self.btnActualizar.setObjectName(u"btnActualizar")

        self.horizontalBotones.addWidget(self.btnActualizar)

        self.lblFacultades = QLabel(DepartamentoPage)
        self.lblFacultades.setObjectName(u"lblFacultades")
        self.lblFacultades.setGeometry(QRect(170, 0, 61, 21))
        self.lblDepartamento = QLabel(DepartamentoPage)
        self.lblDepartamento.setObjectName(u"lblDepartamento")
        self.lblDepartamento.setGeometry(QRect(620, 0, 81, 20))
        self.formLayoutWidget = QWidget(DepartamentoPage)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 360, 431, 251))
        self.formularioInformacion = QFormLayout(self.formLayoutWidget)
        self.formularioInformacion.setObjectName(u"formularioInformacion")
        self.formularioInformacion.setContentsMargins(0, 0, 0, 0)
        self.lblNombre = QLabel(self.formLayoutWidget)
        self.lblNombre.setObjectName(u"lblNombre")

        self.formularioInformacion.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.LineEditDepartamento = QLineEdit(self.formLayoutWidget)
        self.LineEditDepartamento.setObjectName(u"LineEditDepartamento")

        self.formularioInformacion.setWidget(0, QFormLayout.ItemRole.FieldRole, self.LineEditDepartamento)

        self.lblFacultad = QLabel(self.formLayoutWidget)
        self.lblFacultad.setObjectName(u"lblFacultad")

        self.formularioInformacion.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblFacultad)

        self.comboBoxFacultad = QComboBox(self.formLayoutWidget)
        self.comboBoxFacultad.addItem("")
        self.comboBoxFacultad.addItem("")
        self.comboBoxFacultad.addItem("")
        self.comboBoxFacultad.addItem("")
        self.comboBoxFacultad.addItem("")
        self.comboBoxFacultad.setObjectName(u"comboBoxFacultad")

        self.formularioInformacion.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBoxFacultad)


        self.retranslateUi(DepartamentoPage)

        QMetaObject.connectSlotsByName(DepartamentoPage)
    # setupUi

    def retranslateUi(self, DepartamentoPage):
        DepartamentoPage.setWindowTitle(QCoreApplication.translate("Departamento", u"Form", None))
        self.btnAgregar.setText(QCoreApplication.translate("Departamento", u"Agregar", None))
        self.btnEliminar.setText(QCoreApplication.translate("Departamento", u"Eliminar", None))
        self.btnEditar.setText(QCoreApplication.translate("Departamento", u"Editar", None))
        self.btnActualizar.setText(QCoreApplication.translate("Departamento", u"Actualizar", None))
        self.lblFacultades.setText(QCoreApplication.translate("Departamento", u"Facultades", None))
        self.lblDepartamento.setText(QCoreApplication.translate("Departamento", u"Departamentos", None))
        self.lblNombre.setText(QCoreApplication.translate("Departamento", u"Nombre: ", None))
        self.LineEditDepartamento.setInputMask("")
        self.LineEditDepartamento.setText("")
        self.LineEditDepartamento.setPlaceholderText(QCoreApplication.translate("Departamento", u"Nombre Departamento", None))
        self.lblFacultad.setText(QCoreApplication.translate("Departamento", u"Facultad", None))
        self.comboBoxFacultad.setItemText(0, QCoreApplication.translate("Departamento", u"Facultad_1", None))
        self.comboBoxFacultad.setItemText(1, QCoreApplication.translate("Departamento", u"Facultad_2", None))
        self.comboBoxFacultad.setItemText(2, QCoreApplication.translate("Departamento", u"Facultad_3", None))
        self.comboBoxFacultad.setItemText(3, QCoreApplication.translate("Departamento", u"Facultad_4", None))
        self.comboBoxFacultad.setItemText(4, QCoreApplication.translate("Departamento", u"Facultad_5", None))

    # retranslateUi

