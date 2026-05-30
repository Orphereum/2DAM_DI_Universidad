# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PremioEx.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_PremioPage(object):
    def setupUi(self, PremioPage):
        if not PremioPage.objectName():
            PremioPage.setObjectName(u"PremioPage")
        PremioPage.resize(929, 422)
        self.mainLayout = QVBoxLayout(PremioPage)
        self.mainLayout.setObjectName(u"mainLayout")
        self.labelTitulo = QLabel(PremioPage)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout.addWidget(self.labelTitulo)

        self.contentLayout = QHBoxLayout()
        self.contentLayout.setObjectName(u"contentLayout")
        self.tablePremios = QTableWidget(PremioPage)
        if (self.tablePremios.columnCount() < 3):
            self.tablePremios.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablePremios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablePremios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablePremios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tablePremios.setObjectName(u"tablePremios")
        self.tablePremios.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablePremios.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.contentLayout.addWidget(self.tablePremios)

        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnNuevo = QPushButton(PremioPage)
        self.btnNuevo.setObjectName(u"btnNuevo")

        self.buttonLayout.addWidget(self.btnNuevo)

        self.btnEditar = QPushButton(PremioPage)
        self.btnEditar.setObjectName(u"btnEditar")

        self.buttonLayout.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(PremioPage)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.buttonLayout.addWidget(self.btnEliminar)

        self.btnExportar = QPushButton(PremioPage)
        self.btnExportar.setObjectName(u"btnExportar")

        self.buttonLayout.addWidget(self.btnExportar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.buttonLayout.addItem(self.verticalSpacer)


        self.contentLayout.addLayout(self.buttonLayout)


        self.mainLayout.addLayout(self.contentLayout)


        self.retranslateUi(PremioPage)

        QMetaObject.connectSlotsByName(PremioPage)
    # setupUi

    def retranslateUi(self, PremioPage):
        PremioPage.setWindowTitle(QCoreApplication.translate("PremioPage", u"Gesti\u00f3n de Premios", None))
        self.labelTitulo.setText(QCoreApplication.translate("PremioPage", u"Premios a la Excelencia", None))
        ___qtablewidgetitem = self.tablePremios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PremioPage", u"ID", None));
        ___qtablewidgetitem1 = self.tablePremios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PremioPage", u"Nombre del Premio", None));
        ___qtablewidgetitem2 = self.tablePremios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PremioPage", u"Descripci\u00f3n", None));
        self.btnNuevo.setText(QCoreApplication.translate("PremioPage", u"Nuevo", None))
        self.btnEditar.setText(QCoreApplication.translate("PremioPage", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("PremioPage", u"Eliminar", None))
        self.btnExportar.setText(QCoreApplication.translate("PremioPage", u"Exportar PDF", None))
    # retranslateUi

