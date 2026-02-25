# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProyectoPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Proyecto_page(object):
    def setupUi(self, Proyecto_page):
        if not Proyecto_page.objectName():
            Proyecto_page.setObjectName(u"Proyecto_page")
        Proyecto_page.resize(868, 599)
        Proyecto_page.setStyleSheet(u"QLineEdit {\n"
"	font: 300 12pt \"Poppins\";\n"
"}\n"
"QPlainTextEdit {\n"
"	font: 300 12pt \"Poppins\";\n"
"}\n"
"QLabel {\n"
"	\n"
"	font: 600 16pt \"Poppins\";\n"
"}\n"
"QPushButton {\n"
"	font: 600 14pt \"Poppins\";\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(Proyecto_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pageTitle = QLabel(Proyecto_page)
        self.pageTitle.setObjectName(u"pageTitle")
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.pageTitle.setFont(font)
        self.pageTitle.setStyleSheet(u"font: 700 24pt \"Poppins\";")
        self.pageTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.pageTitle)

        self.widget = QWidget(Proyecto_page)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"	border: 0.5px solid gray;\n"
"	border-radius: 5px\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox_gruposInv = QComboBox(self.groupBox)
        self.comboBox_gruposInv.setObjectName(u"comboBox_gruposInv")

        self.verticalLayout_3.addWidget(self.comboBox_gruposInv)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_2.addWidget(self.comboBox_2)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMaximumSize(QSize(16777215, 25))
        self.pushButton.setStyleSheet(u"color:white")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.groupBox_3)


        self.verticalLayout_5.addWidget(self.widget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, -1, 10, -1)
        self.lblNombre = QLabel(Proyecto_page)
        self.lblNombre.setObjectName(u"lblNombre")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(16)
        font1.setWeight(QFont.DemiBold)
        font1.setItalic(False)
        self.lblNombre.setFont(font1)
        self.lblNombre.setStyleSheet(u"color:white")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.nombre_txt = QLineEdit(Proyecto_page)
        self.nombre_txt.setObjectName(u"nombre_txt")
        self.nombre_txt.setMaximumSize(QSize(16777215, 35))
        self.nombre_txt.setStyleSheet(u"color:white")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nombre_txt)

        self.lblCorreo = QLabel(Proyecto_page)
        self.lblCorreo.setObjectName(u"lblCorreo")
        self.lblCorreo.setFont(font1)
        self.lblCorreo.setStyleSheet(u"color:white")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblCorreo)

        self.descripcion_txt = QPlainTextEdit(Proyecto_page)
        self.descripcion_txt.setObjectName(u"descripcion_txt")
        self.descripcion_txt.setMaximumSize(QSize(16777215, 100))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.descripcion_txt)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.btn_editar = QPushButton(Proyecto_page)
        self.btn_editar.setObjectName(u"btn_editar")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(14)
        font2.setWeight(QFont.DemiBold)
        font2.setItalic(False)
        self.btn_editar.setFont(font2)
        self.btn_editar.setStyleSheet(u"color:white")

        self.verticalLayout_4.addWidget(self.btn_editar)

        self.btn_guardar = QPushButton(Proyecto_page)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setFont(font2)
        self.btn_guardar.setStyleSheet(u"color:white")

        self.verticalLayout_4.addWidget(self.btn_guardar)

        self.btn_eliminar = QPushButton(Proyecto_page)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setFont(font2)
        self.btn_eliminar.setStyleSheet(u"color:white")

        self.verticalLayout_4.addWidget(self.btn_eliminar)

        self.btn_limpiar = QPushButton(Proyecto_page)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setFont(font2)
        self.btn_limpiar.setStyleSheet(u"color:white")

        self.verticalLayout_4.addWidget(self.btn_limpiar)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tabla_proyectos = QTableWidget(Proyecto_page)
        if (self.tabla_proyectos.columnCount() < 3):
            self.tabla_proyectos.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_proyectos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabla_proyectos.setObjectName(u"tabla_proyectos")
        self.tabla_proyectos.horizontalHeader().setStretchLastSection(True)
        self.tabla_proyectos.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_3.addWidget(self.tabla_proyectos)

        self.tabla_subvenciones = QTableWidget(Proyecto_page)
        if (self.tabla_subvenciones.columnCount() < 2):
            self.tabla_subvenciones.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_subvenciones.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_subvenciones.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        self.tabla_subvenciones.setObjectName(u"tabla_subvenciones")
        self.tabla_subvenciones.horizontalHeader().setStretchLastSection(True)
        self.tabla_subvenciones.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_3.addWidget(self.tabla_subvenciones)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 2)
        self.verticalLayout_5.setStretch(3, 3)

        self.retranslateUi(Proyecto_page)

        QMetaObject.connectSlotsByName(Proyecto_page)
    # setupUi

    def retranslateUi(self, Proyecto_page):
        Proyecto_page.setWindowTitle(QCoreApplication.translate("Proyecto_page", u"Form", None))
        self.pageTitle.setText(QCoreApplication.translate("Proyecto_page", u"Proyectosv2", None))
        self.groupBox.setTitle(QCoreApplication.translate("Proyecto_page", u"Grupos de Investigaci\u00f3n", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Proyecto_page", u"Subvenciones", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Proyecto_page", u"Informes", None))
        self.pushButton.setText(QCoreApplication.translate("Proyecto_page", u"Guardar datos", None))
        self.lblNombre.setText(QCoreApplication.translate("Proyecto_page", u"Nombre:", None))
        self.lblCorreo.setText(QCoreApplication.translate("Proyecto_page", u"Descripci\u00f3n", None))
        self.btn_editar.setText(QCoreApplication.translate("Proyecto_page", u"Editar", None))
        self.btn_guardar.setText(QCoreApplication.translate("Proyecto_page", u"Guardar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Proyecto_page", u"Eliminar", None))
        self.btn_limpiar.setText(QCoreApplication.translate("Proyecto_page", u"Limpiar", None))
        ___qtablewidgetitem = self.tabla_proyectos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Proyecto_page", u"Id proyecto", None));
        ___qtablewidgetitem1 = self.tabla_proyectos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Proyecto_page", u"Nombre", None));
        ___qtablewidgetitem2 = self.tabla_proyectos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Proyecto_page", u"Descripci\u00f3n", None));
        ___qtablewidgetitem3 = self.tabla_subvenciones.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Proyecto_page", u"Subvenci\u00f3n", None));
        ___qtablewidgetitem4 = self.tabla_subvenciones.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Proyecto_page", u"Importe asignado", None));
    # retranslateUi

