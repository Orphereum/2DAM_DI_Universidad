# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UniversidadPage.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_UniversidadPage(object):
    def setupUi(self, UniversidadPage):
        if not UniversidadPage.objectName():
            UniversidadPage.setObjectName(u"UniversidadPage")
        UniversidadPage.resize(850, 650)
        UniversidadPage.setStyleSheet(u"\n"
"QWidget#UniversidadPage {\n"
"  background-color: #23222a;\n"
"}\n"
"QLineEdit {\n"
"  font: 300 12pt \"Poppins\";\n"
"  padding: 5px;\n"
"  border: 1px solid #3d3d4d;\n"
"  border-radius: 4px;\n"
"  background-color: #2c2b36;\n"
"  color: #ffffff;\n"
"}\n"
"QLabel {\n"
"  font: 600 14pt \"Poppins\";\n"
"  color: #ffffff;\n"
"}\n"
"QPushButton {\n"
"  font: 600 11pt \"Poppins\";\n"
"  padding: 8px 15px;\n"
"  border-radius: 5px;\n"
"}\n"
"QTableWidget {\n"
"  background-color: #2c2b36;\n"
"  color: #ffffff;\n"
"  gridline-color: #3d3d4d;\n"
"  border: 1px solid #3d3d4d;\n"
"  border-radius: 6px;\n"
"}\n"
"   ")
        self.mainVerticalLayout = QVBoxLayout(UniversidadPage)
        self.mainVerticalLayout.setSpacing(20)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.mainVerticalLayout.setContentsMargins(25, 25, 25, 25)
        self.labelTitulo = QLabel(UniversidadPage)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(22)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainVerticalLayout.addWidget(self.labelTitulo)

        self.formLayout = QHBoxLayout()
        self.formLayout.setSpacing(15)
        self.formLayout.setObjectName(u"formLayout")
        self.labelNombre = QLabel(UniversidadPage)
        self.labelNombre.setObjectName(u"labelNombre")
        self.labelNombre.setMinimumSize(QSize(80, 0))

        self.formLayout.addWidget(self.labelNombre)

        self.inputNombre = QLineEdit(UniversidadPage)
        self.inputNombre.setObjectName(u"inputNombre")
        self.inputNombre.setMinimumSize(QSize(0, 40))
        self.inputNombre.setMaximumSize(QSize(16777215, 40))

        self.formLayout.addWidget(self.inputNombre)


        self.mainVerticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(10)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnCrear = QPushButton(UniversidadPage)
        self.btnCrear.setObjectName(u"btnCrear")

        self.buttonLayout.addWidget(self.btnCrear)

        self.btnEditar = QPushButton(UniversidadPage)
        self.btnEditar.setObjectName(u"btnEditar")

        self.buttonLayout.addWidget(self.btnEditar)

        self.btnGuardar = QPushButton(UniversidadPage)
        self.btnGuardar.setObjectName(u"btnGuardar")

        self.buttonLayout.addWidget(self.btnGuardar)

        self.btnEliminar = QPushButton(UniversidadPage)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.buttonLayout.addWidget(self.btnEliminar)

        self.btnLimpiar = QPushButton(UniversidadPage)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.buttonLayout.addWidget(self.btnLimpiar)

        self.btnReporte = QPushButton(UniversidadPage)
        self.btnReporte.setObjectName(u"btnReporte")

        self.buttonLayout.addWidget(self.btnReporte)


        self.mainVerticalLayout.addLayout(self.buttonLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.mainVerticalLayout.addItem(self.verticalSpacer)

        self.tablaUniversidades = QTableWidget(UniversidadPage)
        if (self.tablaUniversidades.columnCount() < 2):
            self.tablaUniversidades.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaUniversidades.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaUniversidades.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tablaUniversidades.setObjectName(u"tablaUniversidades")
        self.tablaUniversidades.setMinimumSize(QSize(0, 300))
        self.tablaUniversidades.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaUniversidades.setColumnCount(2)
        self.tablaUniversidades.horizontalHeader().setStretchLastSection(True)

        self.mainVerticalLayout.addWidget(self.tablaUniversidades)


        self.retranslateUi(UniversidadPage)

        QMetaObject.connectSlotsByName(UniversidadPage)
    # setupUi

    def retranslateUi(self, UniversidadPage):
        UniversidadPage.setWindowTitle(QCoreApplication.translate("UniversidadPage", u"Universidad", None))
        self.labelTitulo.setText(QCoreApplication.translate("UniversidadPage", u"Gesti\u00f3n de Universidades", None))
        self.labelNombre.setText(QCoreApplication.translate("UniversidadPage", u"Nombre:", None))
        self.btnCrear.setText(QCoreApplication.translate("UniversidadPage", u"Crear", None))
        self.btnEditar.setText(QCoreApplication.translate("UniversidadPage", u"Editar", None))
        self.btnGuardar.setText(QCoreApplication.translate("UniversidadPage", u"Guardar", None))
        self.btnEliminar.setText(QCoreApplication.translate("UniversidadPage", u"Eliminar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("UniversidadPage", u"Limpiar", None))
        self.btnReporte.setText(QCoreApplication.translate("UniversidadPage", u"Generar Reporte", None))
        ___qtablewidgetitem = self.tablaUniversidades.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("UniversidadPage", u"ID", None));
        ___qtablewidgetitem1 = self.tablaUniversidades.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("UniversidadPage", u"Nombre", None));
    # retranslateUi

