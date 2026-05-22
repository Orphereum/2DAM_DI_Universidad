# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PremioEx.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_PremioPage(object):
    def setupUi(self, PremioPage):
        if not PremioPage.objectName():
            PremioPage.setObjectName(u"PremioPage")
        PremioPage.resize(929, 422)
        self.labelTitulo = QLabel(PremioPage)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setGeometry(QRect(9, 9, 227, 28))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(PremioPage)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 70, 891, 311))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnNuevo = QPushButton(self.widget)
        self.btnNuevo.setObjectName(u"btnNuevo")

        self.verticalLayout.addWidget(self.btnNuevo)

        self.btnEditar = QPushButton(self.widget)
        self.btnEditar.setObjectName(u"btnEditar")

        self.verticalLayout.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(self.widget)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.verticalLayout.addWidget(self.btnEliminar)

        self.btnExportar = QPushButton(self.widget)
        self.btnExportar.setObjectName(u"btnExportar")

        self.verticalLayout.addWidget(self.btnExportar)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(228, 258, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.tablePremios = QTableWidget(self.widget)
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

        self.horizontalLayout.addWidget(self.tablePremios)


        self.retranslateUi(PremioPage)

        QMetaObject.connectSlotsByName(PremioPage)
    # setupUi

    def retranslateUi(self, PremioPage):
        PremioPage.setWindowTitle(QCoreApplication.translate("PremioPage", u"Gesti\u00f3n de Premios", None))
        self.labelTitulo.setText(QCoreApplication.translate("PremioPage", u"Premios a la Excelencia", None))
        self.btnNuevo.setText(QCoreApplication.translate("PremioPage", u"Nuevo", None))
        self.btnEditar.setText(QCoreApplication.translate("PremioPage", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("PremioPage", u"Eliminar", None))
        self.btnExportar.setText(QCoreApplication.translate("PremioPage", u"Exportar PDF", None))
        ___qtablewidgetitem = self.tablePremios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PremioPage", u"ID", None));
        ___qtablewidgetitem1 = self.tablePremios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PremioPage", u"Nombre del Premio", None));
        ___qtablewidgetitem2 = self.tablePremios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PremioPage", u"Descripci\u00f3n", None));
    # retranslateUi

