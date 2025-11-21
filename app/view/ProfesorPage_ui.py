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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_ProfesorPage(object):
    def setupUi(self, ProfesorPage):
        if not ProfesorPage.objectName():
            ProfesorPage.setObjectName(u"ProfesorPage")
        ProfesorPage.resize(881, 621)
        ProfesorPage.setStyleSheet(u"color:black")
        self.pageTitle = QLabel(ProfesorPage)
        self.pageTitle.setObjectName(u"pageTitle")
        self.pageTitle.setGeometry(QRect(10, 10, 201, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(26)
        font.setBold(True)
        self.pageTitle.setFont(font)
        self.pageTitle.setStyleSheet(u"color:white")
        self.pageTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayoutWidget = QWidget(ProfesorPage)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 70, 501, 211))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblNombre = QLabel(self.formLayoutWidget)
        self.lblNombre.setObjectName(u"lblNombre")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        self.lblNombre.setFont(font1)
        self.lblNombre.setStyleSheet(u"color:white")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txtNombre = QLineEdit(self.formLayoutWidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setStyleSheet(u"color:white")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.lblCorreo = QLabel(self.formLayoutWidget)
        self.lblCorreo.setObjectName(u"lblCorreo")
        self.lblCorreo.setFont(font1)
        self.lblCorreo.setStyleSheet(u"color:white")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblCorreo)

        self.txtCorreo = QLineEdit(self.formLayoutWidget)
        self.txtCorreo.setObjectName(u"txtCorreo")
        self.txtCorreo.setStyleSheet(u"color:white")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtCorreo)

        self.lblTlf = QLabel(self.formLayoutWidget)
        self.lblTlf.setObjectName(u"lblTlf")
        font2 = QFont()
        font2.setPointSize(16)
        self.lblTlf.setFont(font2)
        self.lblTlf.setStyleSheet(u"color:white")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblTlf)

        self.txtTlf = QLineEdit(self.formLayoutWidget)
        self.txtTlf.setObjectName(u"txtTlf")
        self.txtTlf.setStyleSheet(u"color:white")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtTlf)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color:white")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label)

        self.txtTitulo = QLineEdit(self.formLayoutWidget)
        self.txtTitulo.setObjectName(u"txtTitulo")
        self.txtTitulo.setStyleSheet(u"color:white")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtTitulo)

        self.lblDpto = QLabel(self.formLayoutWidget)
        self.lblDpto.setObjectName(u"lblDpto")
        self.lblDpto.setFont(font2)
        self.lblDpto.setStyleSheet(u"color:white")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblDpto)

        self.cbDpto = QComboBox(self.formLayoutWidget)
        self.cbDpto.addItem("")
        self.cbDpto.addItem("")
        self.cbDpto.setObjectName(u"cbDpto")
        self.cbDpto.setStyleSheet(u"color:white")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cbDpto)

        self.lblJefeDpto = QLabel(self.formLayoutWidget)
        self.lblJefeDpto.setObjectName(u"lblJefeDpto")
        self.lblJefeDpto.setFont(font2)
        self.lblJefeDpto.setStyleSheet(u"color:white")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblJefeDpto)

        self.checkJefe = QCheckBox(self.formLayoutWidget)
        self.checkJefe.setObjectName(u"checkJefe")
        font3 = QFont()
        font3.setPointSize(12)
        self.checkJefe.setFont(font3)
        self.checkJefe.setStyleSheet(u"color:white")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.checkJefe)

        self.verticalLayoutWidget = QWidget(ProfesorPage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(530, 70, 331, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnActualizar = QPushButton(self.verticalLayoutWidget)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setFont(font2)
        self.btnActualizar.setStyleSheet(u"color:white")

        self.verticalLayout.addWidget(self.btnActualizar)

        self.btbGuardar = QPushButton(self.verticalLayoutWidget)
        self.btbGuardar.setObjectName(u"btbGuardar")
        self.btbGuardar.setFont(font2)
        self.btbGuardar.setStyleSheet(u"color:white")

        self.verticalLayout.addWidget(self.btbGuardar)

        self.btnEliminar = QPushButton(self.verticalLayoutWidget)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setFont(font2)
        self.btnEliminar.setStyleSheet(u"color:white")

        self.verticalLayout.addWidget(self.btnEliminar)

        self.btnLimpiar = QPushButton(self.verticalLayoutWidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setFont(font2)
        self.btnLimpiar.setStyleSheet(u"color:white")

        self.verticalLayout.addWidget(self.btnLimpiar)

        self.tblProfesores = QTableWidget(ProfesorPage)
        self.tblProfesores.setObjectName(u"tblProfesores")
        self.tblProfesores.setGeometry(QRect(10, 300, 861, 321))

        self.retranslateUi(ProfesorPage)

        QMetaObject.connectSlotsByName(ProfesorPage)
    # setupUi

    def retranslateUi(self, ProfesorPage):
        ProfesorPage.setWindowTitle(QCoreApplication.translate("ProfesorPage", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("ProfesorPage", u"Profesores", None))
        self.lblNombre.setText(QCoreApplication.translate("ProfesorPage", u"Nombre:", None))
        self.lblCorreo.setText(QCoreApplication.translate("ProfesorPage", u"Correo:", None))
        self.lblTlf.setText(QCoreApplication.translate("ProfesorPage", u"Tel\u00e9fono: ", None))
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

