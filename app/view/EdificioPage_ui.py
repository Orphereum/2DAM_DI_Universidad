# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EdificioPage.ui'
##
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget,
)


class Ui_EdificioPage(object):
    def setupUi(self, EdificioPage):
        if not EdificioPage.objectName():
            EdificioPage.setObjectName(u"EdificioPage")
        EdificioPage.resize(820, 580)

        # ── Formulario (nombre + facultad) ────────────────────────────────────
        self.widget = QWidget(EdificioPage)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 90, 301, 75))

        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)

        font_form = QFont()
        font_form.setPointSize(15)

        self.lblNombre = QLabel(self.widget)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setFont(font_form)
        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.leNombre = QLineEdit(self.widget)
        self.leNombre.setObjectName(u"leNombre")
        self.leNombre.setFont(font_form)
        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leNombre)

        self.lblFacultad = QLabel(self.widget)
        self.lblFacultad.setObjectName(u"lblFacultad")
        self.lblFacultad.setFont(font_form)
        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblFacultad)

        self.cbFacultad = QComboBox(self.widget)
        self.cbFacultad.setObjectName(u"cbFacultad")
        self.cbFacultad.setFont(font_form)
        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cbFacultad)

        # ── Título ────────────────────────────────────────────────────────────
        self.lblTitulo = QLabel(EdificioPage)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setGeometry(QRect(30, 20, 121, 61))
        font_titulo = QFont()
        font_titulo.setPointSize(22)
        font_titulo.setBold(True)
        self.lblTitulo.setFont(font_titulo)

        # ── Tabla ─────────────────────────────────────────────────────────────
        self.widget1 = QWidget(EdificioPage)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(90, 190, 661, 341))

        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        font_tabla = QFont()
        font_tabla.setPointSize(13)

        self.tableEdificios = QTableWidget(self.widget1)
        self.tableEdificios.setObjectName(u"tableEdificios")
        self.tableEdificios.setFont(font_tabla)
        self.verticalLayout.addWidget(self.tableEdificios)

        # ── Botones CRUD + Informe ─────────────────────────────────────────────
        self.widget2 = QWidget(EdificioPage)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(480, 90, 282, 90))   # ligeramente más alto

        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        # Fila 1: Añadir | Eliminar
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.btnAnadir = QPushButton(self.widget2)
        self.btnAnadir.setObjectName(u"btnAnadir")
        self.btnAnadir.setMaximumSize(QSize(200, 16777215))
        self.btnAnadir.setFont(font_tabla)
        self.horizontalLayout.addWidget(self.btnAnadir)

        self.btnEliminar = QPushButton(self.widget2)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setMaximumSize(QSize(200, 16777215))
        self.btnEliminar.setFont(font_tabla)
        self.horizontalLayout.addWidget(self.btnEliminar)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        # Fila 2: Editar | Refrescar
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.btnEditar = QPushButton(self.widget2)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setMaximumSize(QSize(200, 16777215))
        self.btnEditar.setFont(font_tabla)
        self.horizontalLayout_2.addWidget(self.btnEditar)

        self.btnRefrescar = QPushButton(self.widget2)
        self.btnRefrescar.setObjectName(u"btnRefrescar")
        self.btnRefrescar.setMaximumSize(QSize(200, 16777215))
        self.btnRefrescar.setFont(font_tabla)
        self.horizontalLayout_2.addWidget(self.btnRefrescar)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        # Fila 3: Generar Informe (ocupa todo el ancho)
        self.btnGenerarInforme = QPushButton(self.widget2)
        self.btnGenerarInforme.setObjectName(u"btnGenerarInforme")
        self.btnGenerarInforme.setFont(font_tabla)
        self.verticalLayout_2.addWidget(self.btnGenerarInforme)

        self.retranslateUi(EdificioPage)
        QMetaObject.connectSlotsByName(EdificioPage)

    def retranslateUi(self, EdificioPage):
        EdificioPage.setWindowTitle(
            QCoreApplication.translate("EdificioPage", u"Form", None)
        )
        self.lblNombre.setText(
            QCoreApplication.translate("EdificioPage", u"Nombre:", None)
        )
        self.lblFacultad.setText(
            QCoreApplication.translate("EdificioPage", u"Facultad: ", None)
        )
        self.lblTitulo.setText(
            QCoreApplication.translate("EdificioPage", u"Edificios", None)
        )
        self.btnAnadir.setText(
            QCoreApplication.translate("EdificioPage", u"Añadir", None)
        )
        self.btnEliminar.setText(
            QCoreApplication.translate("EdificioPage", u"Eliminar", None)
        )
        self.btnEditar.setText(
            QCoreApplication.translate("EdificioPage", u"Editar", None)
        )
        self.btnRefrescar.setText(
            QCoreApplication.translate("EdificioPage", u"Refrescar Tabla", None)
        )
        self.btnGenerarInforme.setText(
            QCoreApplication.translate("EdificioPage", u"Generar Informe PDF", None)
        )