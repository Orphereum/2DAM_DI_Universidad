# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Asignatura.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_AsignaturasView(object):
    def setupUi(self, AsignaturasView):
        if not AsignaturasView.objectName():
            AsignaturasView.setObjectName(u"AsignaturasView")
        AsignaturasView.resize(900, 700)
        self.verticalLayout = QVBoxLayout(AsignaturasView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacerTop = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerTop)

        self.lblTitulo = QLabel(AsignaturasView)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setPointSize(42)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.widgetContexto = QWidget(AsignaturasView)
        self.widgetContexto.setObjectName(u"widgetContexto")
        self.hboxLayout = QHBoxLayout(self.widgetContexto)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.horizontalSpacerLeft = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.horizontalSpacerLeft)

        self.lblContexto = QLabel(self.widgetContexto)
        self.lblContexto.setObjectName(u"lblContexto")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblContexto.setFont(font1)

        self.hboxLayout.addWidget(self.lblContexto)

        self.cb_grado_filtro = QComboBox(self.widgetContexto)
        self.cb_grado_filtro.setObjectName(u"cb_grado_filtro")
        self.cb_grado_filtro.setMinimumWidth(250)

        self.hboxLayout.addWidget(self.cb_grado_filtro)

        self.horizontalSpacerRight = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.horizontalSpacerRight)


        self.verticalLayout.addWidget(self.widgetContexto)

        self.frameMain = QFrame(AsignaturasView)
        self.frameMain.setObjectName(u"frameMain")
        self.frameMain.setFrameShape(QFrame.StyledPanel)
        self.vboxLayout = QVBoxLayout(self.frameMain)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.lblTablaTitulo = QLabel(self.frameMain)
        self.lblTablaTitulo.setObjectName(u"lblTablaTitulo")
        self.lblTablaTitulo.setFont(font1)

        self.vboxLayout.addWidget(self.lblTablaTitulo)

        self.tbl_asignaturas = QTableWidget(self.frameMain)
        self.tbl_asignaturas.setObjectName(u"tbl_asignaturas")

        self.vboxLayout.addWidget(self.tbl_asignaturas)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.btn_nueva = QPushButton(self.frameMain)
        self.btn_nueva.setObjectName(u"btn_nueva")

        self.hboxLayout1.addWidget(self.btn_nueva)

        self.btn_editar = QPushButton(self.frameMain)
        self.btn_editar.setObjectName(u"btn_editar")

        self.hboxLayout1.addWidget(self.btn_editar)

        self.btn_eliminar = QPushButton(self.frameMain)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.hboxLayout1.addWidget(self.btn_eliminar)

        self.btn_refrescar = QPushButton(self.frameMain)
        self.btn_refrescar.setObjectName(u"btn_refrescar")

        self.hboxLayout1.addWidget(self.btn_refrescar)

        self.btnExportarPdf = QPushButton(self.frameMain)
        self.btnExportarPdf.setObjectName(u"btnExportarPdf")

        self.hboxLayout1.addWidget(self.btnExportarPdf)

        self.spacerButtons = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout1.addItem(self.spacerButtons)


        self.vboxLayout.addLayout(self.hboxLayout1)


        self.verticalLayout.addWidget(self.frameMain)

        self.lbl_estado = QLabel(AsignaturasView)
        self.lbl_estado.setObjectName(u"lbl_estado")
        self.lbl_estado.setMinimumHeight(24)
        self.lbl_estado.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_estado)

        self.verticalSpacerBottom = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerBottom)


        self.retranslateUi(AsignaturasView)

        QMetaObject.connectSlotsByName(AsignaturasView)
    # setupUi

    def retranslateUi(self, AsignaturasView):
        AsignaturasView.setWindowTitle(QCoreApplication.translate("AsignaturasView", u"Asignaturas", None))
        self.lblTitulo.setText(QCoreApplication.translate("AsignaturasView", u"ASIGNATURAS", None))
        self.lblContexto.setText(QCoreApplication.translate("AsignaturasView", u"Grado seleccionado:", None))
        self.lblTablaTitulo.setText(QCoreApplication.translate("AsignaturasView", u"Listado de asignaturas", None))
        self.btn_nueva.setText(QCoreApplication.translate("AsignaturasView", u"Nueva", None))
        self.btn_editar.setText(QCoreApplication.translate("AsignaturasView", u"Editar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("AsignaturasView", u"Eliminar", None))
        self.btn_refrescar.setText(QCoreApplication.translate("AsignaturasView", u"Refrescar", None))
        self.btnExportarPdf.setText(QCoreApplication.translate("AsignaturasView", u"Exportar PDF", None))
        self.lbl_estado.setText(QCoreApplication.translate("AsignaturasView", u"Listo", None))
    # retranslateUi

