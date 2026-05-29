# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FacultadPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_FacultadPage(object):
    def setupUi(self, FacultadPage):
        if not FacultadPage.objectName():
            FacultadPage.setObjectName(u"FacultadPage")
        FacultadPage.resize(880, 614)
        self.verticalLayoutWidget = QWidget(FacultadPage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 851, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblFacultad = QLabel(self.verticalLayoutWidget)
        self.lblFacultad.setObjectName(u"lblFacultad")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFacultad.sizePolicy().hasHeightForWidth())
        self.lblFacultad.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(30)
        self.lblFacultad.setFont(font)
        self.lblFacultad.setTextFormat(Qt.TextFormat.MarkdownText)
        self.lblFacultad.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.lblFacultad)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblNombre = QLabel(self.verticalLayoutWidget)
        self.lblNombre.setObjectName(u"lblNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.leNombre = QLineEdit(self.verticalLayoutWidget)
        self.leNombre.setObjectName(u"leNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leNombre)

        self.lblTelefono = QLabel(self.verticalLayoutWidget)
        self.lblTelefono.setObjectName(u"lblTelefono")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblTelefono)

        self.leTelefono = QLineEdit(self.verticalLayoutWidget)
        self.leTelefono.setObjectName(u"leTelefono")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.leTelefono)

        self.lblEmail = QLabel(self.verticalLayoutWidget)
        self.lblEmail.setObjectName(u"lblEmail")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblEmail)

        self.leEmail = QLineEdit(self.verticalLayoutWidget)
        self.leEmail.setObjectName(u"leEmail")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.leEmail)

        self.lblUniversidad = QLabel(self.verticalLayoutWidget)
        self.lblUniversidad.setObjectName(u"lblUniversidad")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblUniversidad)

        self.cbUniversidad = QComboBox(self.verticalLayoutWidget)
        self.cbUniversidad.setObjectName(u"cbUniversidad")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cbUniversidad)

        self.lblProfesor = QLabel(self.verticalLayoutWidget)
        self.lblProfesor.setObjectName(u"lblProfesor")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblProfesor)

        self.cbProfesor = QComboBox(self.verticalLayoutWidget)
        self.cbProfesor.setObjectName(u"cbProfesor")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cbProfesor)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.tableFacultades = QTableWidget(self.verticalLayoutWidget)
        self.tableFacultades.setObjectName(u"tableFacultades")

        self.gridLayout.addWidget(self.tableFacultades, 0, 1, 1, 1)

        self.buttonRow1 = QHBoxLayout()
        self.buttonRow1.setObjectName(u"buttonRow1")
        self.btnGuardar = QPushButton(self.verticalLayoutWidget)
        self.btnGuardar.setObjectName(u"btnGuardar")

        self.buttonRow1.addWidget(self.btnGuardar)

        self.btnEliminar = QPushButton(self.verticalLayoutWidget)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.buttonRow1.addWidget(self.btnEliminar)


        self.gridLayout.addLayout(self.buttonRow1, 1, 0, 1, 1)

        self.buttonRow2 = QHBoxLayout()
        self.buttonRow2.setObjectName(u"buttonRow2")
        self.btnEditar = QPushButton(self.verticalLayoutWidget)
        self.btnEditar.setObjectName(u"btnEditar")

        self.buttonRow2.addWidget(self.btnEditar)

        self.btnInforme = QPushButton(self.verticalLayoutWidget)
        self.btnInforme.setObjectName(u"btnInforme")

        self.buttonRow2.addWidget(self.btnInforme)


        self.gridLayout.addLayout(self.buttonRow2, 1, 1, 1, 1)

        self.btnRefrescar = QPushButton(self.verticalLayoutWidget)
        self.btnRefrescar.setObjectName(u"btnRefrescar")

        self.gridLayout.addWidget(self.btnRefrescar, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(FacultadPage)

        QMetaObject.connectSlotsByName(FacultadPage)
    # setupUi

    def retranslateUi(self, FacultadPage):
        FacultadPage.setWindowTitle(QCoreApplication.translate("FacultadPage", u"Form", None))
        self.lblFacultad.setText(QCoreApplication.translate("FacultadPage", u"Facultad", None))
        self.lblNombre.setText(QCoreApplication.translate("FacultadPage", u"Nombre:", None))
        self.lblTelefono.setText(QCoreApplication.translate("FacultadPage", u"Tel\u00e9fono:", None))
        self.lblEmail.setText(QCoreApplication.translate("FacultadPage", u"Email:", None))
        self.lblUniversidad.setText(QCoreApplication.translate("FacultadPage", u"Universidad:", None))
        self.lblProfesor.setText(QCoreApplication.translate("FacultadPage", u"Prof. Decano:", None))
        self.btnGuardar.setText(QCoreApplication.translate("FacultadPage", u"Guardar", None))
        self.btnEliminar.setText(QCoreApplication.translate("FacultadPage", u"Eliminar", None))
        self.btnEditar.setText(QCoreApplication.translate("FacultadPage", u"Editar", None))
        self.btnInforme.setText(QCoreApplication.translate("FacultadPage", u"Informe PDF", None))
        self.btnRefrescar.setText(QCoreApplication.translate("FacultadPage", u"Refrescar Tabla", None))
    # retranslateUi

