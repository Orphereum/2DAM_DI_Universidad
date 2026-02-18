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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_UniversidadPage(object):
    def setupUi(self, UniversidadPage):
        if not UniversidadPage.objectName():
            UniversidadPage.setObjectName(u"UniversidadPage")
        UniversidadPage.resize(800, 600)
        self.verticalLayout = QVBoxLayout(UniversidadPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitulo = QLabel(UniversidadPage)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitulo)

        self.formLayout = QHBoxLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelNombre = QLabel(UniversidadPage)
        self.labelNombre.setObjectName(u"labelNombre")

        self.formLayout.addWidget(self.labelNombre)

        self.inputNombre = QLineEdit(UniversidadPage)
        self.inputNombre.setObjectName(u"inputNombre")

        self.formLayout.addWidget(self.inputNombre)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnCrear = QPushButton(UniversidadPage)
        self.btnCrear.setObjectName(u"btnCrear")

        self.buttonLayout.addWidget(self.btnCrear)

        self.btnEditar = QPushButton(UniversidadPage)
        self.btnEditar.setObjectName(u"btnEditar")

        self.buttonLayout.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(UniversidadPage)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.buttonLayout.addWidget(self.btnEliminar)

        self.btnLimpiar = QPushButton(UniversidadPage)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.buttonLayout.addWidget(self.btnLimpiar)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.tablaUniversidades = QTableWidget(UniversidadPage)
        if (self.tablaUniversidades.columnCount() < 2):
            self.tablaUniversidades.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaUniversidades.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaUniversidades.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tablaUniversidades.setObjectName(u"tablaUniversidades")
        self.tablaUniversidades.setColumnCount(2)

        self.verticalLayout.addWidget(self.tablaUniversidades)


        self.retranslateUi(UniversidadPage)

        QMetaObject.connectSlotsByName(UniversidadPage)
    # setupUi

    def retranslateUi(self, UniversidadPage):
        UniversidadPage.setWindowTitle(QCoreApplication.translate("UniversidadPage", u"Universidad", None))
        self.labelTitulo.setText(QCoreApplication.translate("UniversidadPage", u"Gesti\u00f3n de Universidades", None))
        self.labelNombre.setText(QCoreApplication.translate("UniversidadPage", u"Nombre:", None))
        self.btnCrear.setText(QCoreApplication.translate("UniversidadPage", u"Crear", None))
        self.btnEditar.setText(QCoreApplication.translate("UniversidadPage", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("UniversidadPage", u"Eliminar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("UniversidadPage", u"Limpiar", None))
        ___qtablewidgetitem = self.tablaUniversidades.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("UniversidadPage", u"ID", None));
        ___qtablewidgetitem1 = self.tablaUniversidades.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("UniversidadPage", u"Nombre", None));
    # retranslateUi

