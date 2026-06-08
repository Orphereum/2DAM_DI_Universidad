# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GrupoInv.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_GruposInvView(object):
    def setupUi(self, GruposInvView):
        if not GruposInvView.objectName():
            GruposInvView.setObjectName(u"GruposInvView")
        GruposInvView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(GruposInvView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacerTop = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerTop)

        self.lblTitulo = QLabel(GruposInvView)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(42)
        font.setBold(True)
        self.lblTitulo.setFont(font)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.frameMain = QFrame(GruposInvView)
        self.frameMain.setObjectName(u"frameMain")
        self.frameMain.setFrameShape(QFrame.StyledPanel)
        self.vboxLayout = QVBoxLayout(self.frameMain)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.lblTablaTitulo = QLabel(self.frameMain)
        self.lblTablaTitulo.setObjectName(u"lblTablaTitulo")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblTablaTitulo.setFont(font1)

        self.vboxLayout.addWidget(self.lblTablaTitulo)

        self.tbl_grupos = QTableWidget(self.frameMain)
        self.tbl_grupos.setObjectName(u"tbl_grupos")

        self.vboxLayout.addWidget(self.tbl_grupos)

        self.hboxButtons = QHBoxLayout()
        self.hboxButtons.setObjectName(u"hboxButtons")
        self.btn_nuevo = QPushButton(self.frameMain)
        self.btn_nuevo.setObjectName(u"btn_nuevo")

        self.hboxButtons.addWidget(self.btn_nuevo)

        self.btn_editar = QPushButton(self.frameMain)
        self.btn_editar.setObjectName(u"btn_editar")

        self.hboxButtons.addWidget(self.btn_editar)

        self.btn_eliminar = QPushButton(self.frameMain)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.hboxButtons.addWidget(self.btn_eliminar)

        self.btn_refrescar = QPushButton(self.frameMain)
        self.btn_refrescar.setObjectName(u"btn_refrescar")

        self.hboxButtons.addWidget(self.btn_refrescar)

        self.btnExportarPdf = QPushButton(self.frameMain)
        self.btnExportarPdf.setObjectName(u"btnExportarPdf")

        self.hboxButtons.addWidget(self.btnExportarPdf)

        self.btnGraficos = QPushButton(self.frameMain)
        self.btnGraficos.setObjectName(u"btnGraficos")

        self.hboxButtons.addWidget(self.btnGraficos)

        self.spacerButtons = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxButtons.addItem(self.spacerButtons)


        self.vboxLayout.addLayout(self.hboxButtons)


        self.verticalLayout.addWidget(self.frameMain)

        self.lbl_estado = QLabel(GruposInvView)
        self.lbl_estado.setObjectName(u"lbl_estado")
        self.lbl_estado.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_estado)

        self.verticalSpacerBottom = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerBottom)


        self.retranslateUi(GruposInvView)

        QMetaObject.connectSlotsByName(GruposInvView)
    # setupUi

    def retranslateUi(self, GruposInvView):
        GruposInvView.setWindowTitle(QCoreApplication.translate("GruposInvView", u"Grupos de Investigaci\u00f3n", None))
        self.lblTitulo.setText(QCoreApplication.translate("GruposInvView", u"GRUPOS DE INVESTIGACI\u00d3N", None))
        self.lblTablaTitulo.setText(QCoreApplication.translate("GruposInvView", u"Listado de grupos", None))
        self.btn_nuevo.setText(QCoreApplication.translate("GruposInvView", u"Nuevo", None))
        self.btn_editar.setText(QCoreApplication.translate("GruposInvView", u"Editar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("GruposInvView", u"Eliminar", None))
        self.btn_refrescar.setText(QCoreApplication.translate("GruposInvView", u"Refrescar", None))
        self.btnExportarPdf.setText(QCoreApplication.translate("GruposInvView", u"Exportar PDF", None))
        self.btnGraficos.setText(QCoreApplication.translate("GruposInvView", u"Gr\u00e1ficos", None))
        self.lbl_estado.setText(QCoreApplication.translate("GruposInvView", u"Listo", None))
    # retranslateUi

