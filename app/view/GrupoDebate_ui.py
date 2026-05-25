# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GrupoDebate.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_GrupoDebate_page(object):
    def setupUi(self, GrupoDebate_page):
        if not GrupoDebate_page.objectName():
            GrupoDebate_page.setObjectName(u"GrupoDebate_page")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GrupoDebate_page.sizePolicy().hasHeightForWidth())
        GrupoDebate_page.setSizePolicy(sizePolicy)
        self.mainLayout = QVBoxLayout(GrupoDebate_page)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.topBar = QHBoxLayout()
        self.topBar.setObjectName(u"topBar")
        self.pageTitle = QLabel(GrupoDebate_page)
        self.pageTitle.setObjectName(u"pageTitle")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(24)
        font.setBold(True)
        self.pageTitle.setFont(font)
        self.pageTitle.setStyleSheet(u"color:white;")

        self.topBar.addWidget(self.pageTitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.topBar.addItem(self.horizontalSpacer)


        self.mainLayout.addLayout(self.topBar)

        self.contentLayout = QHBoxLayout()
        self.contentLayout.setSpacing(18)
        self.contentLayout.setObjectName(u"contentLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(12)
        self.labelNombre = QLabel(GrupoDebate_page)
        self.labelNombre.setObjectName(u"labelNombre")
        font1 = QFont()
        font1.setPointSize(14)
        self.labelNombre.setFont(font1)
        self.labelNombre.setStyleSheet(u"color:white;")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelNombre)

        self.inputNombre = QLineEdit(GrupoDebate_page)
        self.inputNombre.setObjectName(u"inputNombre")
        self.inputNombre.setStyleSheet(u"color:white;")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.inputNombre)

        self.labelTema = QLabel(GrupoDebate_page)
        self.labelTema.setObjectName(u"labelTema")
        self.labelTema.setFont(font1)
        self.labelTema.setStyleSheet(u"color:white;")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelTema)

        self.inputTemaPrincipal = QLineEdit(GrupoDebate_page)
        self.inputTemaPrincipal.setObjectName(u"inputTemaPrincipal")
        self.inputTemaPrincipal.setStyleSheet(u"color:white;")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.inputTemaPrincipal)

        self.labelDescripcion = QLabel(GrupoDebate_page)
        self.labelDescripcion.setObjectName(u"labelDescripcion")
        self.labelDescripcion.setFont(font1)
        self.labelDescripcion.setStyleSheet(u"color:white;")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelDescripcion)

        self.inputDescripcion = QLineEdit(GrupoDebate_page)
        self.inputDescripcion.setObjectName(u"inputDescripcion")
        self.inputDescripcion.setStyleSheet(u"color:white;")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.inputDescripcion)

        self.labelFechaInicio = QLabel(GrupoDebate_page)
        self.labelFechaInicio.setObjectName(u"labelFechaInicio")
        self.labelFechaInicio.setFont(font1)
        self.labelFechaInicio.setStyleSheet(u"color:white;")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.labelFechaInicio)

        self.inputFechaInicio = QLineEdit(GrupoDebate_page)
        self.inputFechaInicio.setObjectName(u"inputFechaInicio")
        self.inputFechaInicio.setStyleSheet(u"color:white;")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.inputFechaInicio)

        self.labelEstado = QLabel(GrupoDebate_page)
        self.labelEstado.setObjectName(u"labelEstado")
        self.labelEstado.setFont(font1)
        self.labelEstado.setStyleSheet(u"color:white;")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.labelEstado)

        self.inputEstado = QLineEdit(GrupoDebate_page)
        self.inputEstado.setObjectName(u"inputEstado")
        self.inputEstado.setStyleSheet(u"color:white;")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.inputEstado)


        self.contentLayout.addLayout(self.formLayout)

        self.buttonsLayout = QVBoxLayout()
        self.buttonsLayout.setSpacing(10)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.btn_editar = QPushButton(GrupoDebate_page)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setFont(font1)

        self.buttonsLayout.addWidget(self.btn_editar)

        self.btn_guardar = QPushButton(GrupoDebate_page)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setFont(font1)

        self.buttonsLayout.addWidget(self.btn_guardar)

        self.btn_eliminar = QPushButton(GrupoDebate_page)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setFont(font1)

        self.buttonsLayout.addWidget(self.btn_eliminar)

        self.btn_limpiar = QPushButton(GrupoDebate_page)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setFont(font1)

        self.buttonsLayout.addWidget(self.btn_limpiar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.buttonsLayout.addItem(self.verticalSpacer)


        self.contentLayout.addLayout(self.buttonsLayout)


        self.mainLayout.addLayout(self.contentLayout)

        self.tabla_grupos = QTableWidget(GrupoDebate_page)
        if (self.tabla_grupos.columnCount() < 6):
            self.tabla_grupos.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_grupos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_grupos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_grupos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_grupos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_grupos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_grupos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabla_grupos.setObjectName(u"tabla_grupos")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.tabla_grupos.sizePolicy().hasHeightForWidth())
        self.tabla_grupos.setSizePolicy(sizePolicy1)

        self.mainLayout.addWidget(self.tabla_grupos)


        self.retranslateUi(GrupoDebate_page)

        QMetaObject.connectSlotsByName(GrupoDebate_page)
    # setupUi

    def retranslateUi(self, GrupoDebate_page):
        GrupoDebate_page.setWindowTitle(QCoreApplication.translate("GrupoDebate_page", u"Grupo Debate", None))
        self.pageTitle.setText(QCoreApplication.translate("GrupoDebate_page", u"Grupos de Debate", None))
        self.labelNombre.setText(QCoreApplication.translate("GrupoDebate_page", u"Nombre:", None))
        self.labelTema.setText(QCoreApplication.translate("GrupoDebate_page", u"Tema principal:", None))
        self.labelDescripcion.setText(QCoreApplication.translate("GrupoDebate_page", u"Descripci\u00f3n:", None))
        self.labelFechaInicio.setText(QCoreApplication.translate("GrupoDebate_page", u"Fecha inicio:", None))
        self.labelEstado.setText(QCoreApplication.translate("GrupoDebate_page", u"Estado:", None))
        self.btn_editar.setText(QCoreApplication.translate("GrupoDebate_page", u"Editar", None))
        self.btn_guardar.setText(QCoreApplication.translate("GrupoDebate_page", u"Guardar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("GrupoDebate_page", u"Eliminar", None))
        self.btn_limpiar.setText(QCoreApplication.translate("GrupoDebate_page", u"Limpiar", None))
        ___qtablewidgetitem = self.tabla_grupos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("GrupoDebate_page", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_grupos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("GrupoDebate_page", u"Nombre", None));
        ___qtablewidgetitem2 = self.tabla_grupos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("GrupoDebate_page", u"Tema principal", None));
        ___qtablewidgetitem3 = self.tabla_grupos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("GrupoDebate_page", u"Descripci\u00f3n", None));
        ___qtablewidgetitem4 = self.tabla_grupos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("GrupoDebate_page", u"Fecha inicio", None));
        ___qtablewidgetitem5 = self.tabla_grupos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("GrupoDebate_page", u"Estado", None));
    # retranslateUi

