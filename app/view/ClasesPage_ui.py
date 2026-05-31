# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClasesPage.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(883, 631)
        self.centralWidget = QWidget(Form)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setGeometry(QRect(0, 0, 883, 631))
        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 10, 20, 10)
        self.gridLayout.setRowStretch(0, 0)
        self.gridLayout.setRowStretch(1, 0)
        self.gridLayout.setRowStretch(2, 1)
        self.lblTitulo = QLabel(self.centralWidget)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lblTitulo, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCrear = QPushButton(self.centralWidget)
        self.btnCrear.setObjectName(u"btnCrear")

        self.horizontalLayout.addWidget(self.btnCrear)

        self.btnEditar = QPushButton(self.centralWidget)
        self.btnEditar.setObjectName(u"btnEditar")

        self.horizontalLayout.addWidget(self.btnEditar)

        self.btnBorrar = QPushButton(self.centralWidget)
        self.btnBorrar.setObjectName(u"btnBorrar")

        self.horizontalLayout.addWidget(self.btnBorrar)

        self.btnRefrescar = QPushButton(self.centralWidget)
        self.btnRefrescar.setObjectName(u"btnRefrescar")

        self.horizontalLayout.addWidget(self.btnRefrescar)

        self.btnExportarPDF = QPushButton(self.centralWidget)
        self.btnExportarPDF.setObjectName(u"btnExportarPDF")

        self.horizontalLayout.addWidget(self.btnExportarPDF)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.tblClases = QTableWidget(self.centralWidget)
        if (self.tblClases.columnCount() < 4):
            self.tblClases.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblClases.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblClases.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblClases.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblClases.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblClases.setObjectName(u"tblClases")
        self.tblClases.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblClases.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tblClases, 2, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblTitulo.setText(QCoreApplication.translate("Form", u"Gestion de Clases", None))
        self.btnCrear.setText(QCoreApplication.translate("Form", u"Crear", None))
        self.btnEditar.setText(QCoreApplication.translate("Form", u"Editar", None))
        self.btnBorrar.setText(QCoreApplication.translate("Form", u"Borrar", None))
        self.btnRefrescar.setText(QCoreApplication.translate("Form", u"Refrescar", None))
        self.btnExportarPDF.setText(QCoreApplication.translate("Form", u"Exportar PDF", None))
        ___qtablewidgetitem = self.tblClases.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tblClases.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem2 = self.tblClases.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Capacidad", None));
        ___qtablewidgetitem3 = self.tblClases.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Edificio", None));
    # retranslateUi
