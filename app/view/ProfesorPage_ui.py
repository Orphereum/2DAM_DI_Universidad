# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProfesorPage.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from app.resources import resources_rc

class Ui_ProfesorPage(object):
    def setupUi(self, ProfesorPage):
        if not ProfesorPage.objectName():
            ProfesorPage.setObjectName(u"ProfesorPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProfesorPage.sizePolicy().hasHeightForWidth())
        ProfesorPage.setSizePolicy(sizePolicy)
        ProfesorPage.setStyleSheet(u"color:black")
        self.mainLayout = QVBoxLayout(ProfesorPage)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName(u"mainLayout")
        self.topBar = QHBoxLayout()
        self.topBar.setSpacing(12)
        self.topBar.setObjectName(u"topBar")
        self.pageTitle = QLabel(ProfesorPage)
        self.pageTitle.setObjectName(u"pageTitle")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(26)
        font.setBold(True)
        self.pageTitle.setFont(font)
        self.pageTitle.setStyleSheet(u"color:white")
        self.pageTitle.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.topBar.addWidget(self.pageTitle)

        self.topSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.topBar.addItem(self.topSpacer)

        self.searchLayout = QHBoxLayout()
        self.searchLayout.setSpacing(8)
        self.searchLayout.setObjectName(u"searchLayout")
        self.lnBusqueda = QLineEdit(ProfesorPage)
        self.lnBusqueda.setObjectName(u"lnBusqueda")

        self.searchLayout.addWidget(self.lnBusqueda)

        self.btnBusqueda = QPushButton(ProfesorPage)
        self.btnBusqueda.setObjectName(u"btnBusqueda")
        font1 = QFont()
        font1.setPointSize(12)
        self.btnBusqueda.setFont(font1)
        self.btnBusqueda.setStyleSheet(u"color:white")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icono_buscar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBusqueda.setIcon(icon)
        self.btnBusqueda.setIconSize(QSize(19, 19))

        self.searchLayout.addWidget(self.btnBusqueda)


        self.topBar.addLayout(self.searchLayout)

        self.pushButton = QPushButton(ProfesorPage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"color:white")

        self.topBar.addWidget(self.pushButton)


        self.mainLayout.addLayout(self.topBar)

        self.midLayout = QHBoxLayout()
        self.midLayout.setSpacing(16)
        self.midLayout.setObjectName(u"midLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(10)
        self.lblNombre = QLabel(ProfesorPage)
        self.lblNombre.setObjectName(u"lblNombre")
        font2 = QFont()
        font2.setPointSize(16)
        self.lblNombre.setFont(font2)
        self.lblNombre.setStyleSheet(u"color:white")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txtNombre = QLineEdit(ProfesorPage)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setStyleSheet(u"color:white")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.lblCorreo = QLabel(ProfesorPage)
        self.lblCorreo.setObjectName(u"lblCorreo")
        self.lblCorreo.setFont(font2)
        self.lblCorreo.setStyleSheet(u"color:white")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblCorreo)

        self.txtCorreo = QLineEdit(ProfesorPage)
        self.txtCorreo.setObjectName(u"txtCorreo")
        self.txtCorreo.setStyleSheet(u"color:white")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtCorreo)

        self.lblTlf = QLabel(ProfesorPage)
        self.lblTlf.setObjectName(u"lblTlf")
        self.lblTlf.setFont(font2)
        self.lblTlf.setStyleSheet(u"color:white")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblTlf)

        self.txtTlf = QLineEdit(ProfesorPage)
        self.txtTlf.setObjectName(u"txtTlf")
        self.txtTlf.setStyleSheet(u"color:white")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtTlf)

        self.label = QLabel(ProfesorPage)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color:white")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label)

        self.txtTitulo = QLineEdit(ProfesorPage)
        self.txtTitulo.setObjectName(u"txtTitulo")
        self.txtTitulo.setStyleSheet(u"color:white")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtTitulo)

        self.lblDpto = QLabel(ProfesorPage)
        self.lblDpto.setObjectName(u"lblDpto")
        self.lblDpto.setFont(font2)
        self.lblDpto.setStyleSheet(u"color:white")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblDpto)

        self.cbDpto = QComboBox(ProfesorPage)
        self.cbDpto.addItem("")
        self.cbDpto.addItem("")
        self.cbDpto.setObjectName(u"cbDpto")
        self.cbDpto.setStyleSheet(u"color:white")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cbDpto)

        self.lblJefeDpto = QLabel(ProfesorPage)
        self.lblJefeDpto.setObjectName(u"lblJefeDpto")
        self.lblJefeDpto.setFont(font2)
        self.lblJefeDpto.setStyleSheet(u"color:white")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblJefeDpto)

        self.checkJefe = QCheckBox(ProfesorPage)
        self.checkJefe.setObjectName(u"checkJefe")
        self.checkJefe.setFont(font1)
        self.checkJefe.setStyleSheet(u"color:white")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.checkJefe)


        self.midLayout.addLayout(self.formLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnActualizar = QPushButton(ProfesorPage)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setFont(font2)
        self.btnActualizar.setStyleSheet(u"color:white")

        self.verticalLayout.addWidget(self.btnActualizar)

        self.btbGuardar = QPushButton(ProfesorPage)
        self.btbGuardar.setObjectName(u"btbGuardar")
        self.btbGuardar.setFont(font2)
        self.btbGuardar.setStyleSheet(u"color:white")

        self.verticalLayout.addWidget(self.btbGuardar)

        self.btnEliminar = QPushButton(ProfesorPage)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setFont(font2)
        self.btnEliminar.setStyleSheet(u"color:white")

        self.verticalLayout.addWidget(self.btnEliminar)

        self.btnLimpiar = QPushButton(ProfesorPage)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setFont(font2)
        self.btnLimpiar.setStyleSheet(u"color:white")

        self.verticalLayout.addWidget(self.btnLimpiar)

        self.buttonsSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.buttonsSpacer)


        self.midLayout.addLayout(self.verticalLayout)


        self.mainLayout.addLayout(self.midLayout)

        self.tblProfesores = QTableWidget(ProfesorPage)
        self.tblProfesores.setObjectName(u"tblProfesores")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.tblProfesores.sizePolicy().hasHeightForWidth())
        self.tblProfesores.setSizePolicy(sizePolicy1)

        self.mainLayout.addWidget(self.tblProfesores)


        self.retranslateUi(ProfesorPage)

        QMetaObject.connectSlotsByName(ProfesorPage)
    # setupUi

    def retranslateUi(self, ProfesorPage):
        ProfesorPage.setWindowTitle(QCoreApplication.translate("ProfesorPage", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("ProfesorPage", u"Profesores", None))
        self.lnBusqueda.setPlaceholderText(QCoreApplication.translate("ProfesorPage", u"Buscar...", None))
        self.btnBusqueda.setText("")
        self.pushButton.setText(QCoreApplication.translate("ProfesorPage", u"Exportar a PDF", None))
        self.lblNombre.setText(QCoreApplication.translate("ProfesorPage", u"Nombre:", None))
        self.lblCorreo.setText(QCoreApplication.translate("ProfesorPage", u"Correo:", None))
        self.lblTlf.setText(QCoreApplication.translate("ProfesorPage", u"Tel\u00e9fono:", None))
        self.label.setText(QCoreApplication.translate("ProfesorPage", u"T\u00edtulo:", None))
        self.lblDpto.setText(QCoreApplication.translate("ProfesorPage", u"Departamento:", None))
        self.cbDpto.setItemText(0, QCoreApplication.translate("ProfesorPage", u"Ciencias", None))
        self.cbDpto.setItemText(1, QCoreApplication.translate("ProfesorPage", u"Ingenieria", None))

        self.lblJefeDpto.setText(QCoreApplication.translate("ProfesorPage", u"Jefe de departamento:", None))
        self.checkJefe.setText(QCoreApplication.translate("ProfesorPage", u"Es jefe de departamento", None))
        self.btnActualizar.setText(QCoreApplication.translate("ProfesorPage", u"Editar", None))
        self.btbGuardar.setText(QCoreApplication.translate("ProfesorPage", u"Guardar", None))
        self.btnEliminar.setText(QCoreApplication.translate("ProfesorPage", u"Eliminar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("ProfesorPage", u"Limpiar", None))
    # retranslateUi

