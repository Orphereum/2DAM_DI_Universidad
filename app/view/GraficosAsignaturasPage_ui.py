# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GraficosAsignaturasPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_GraficosAsignaturasPage(object):
    def setupUi(self, GraficosAsignaturasPage):
        if not GraficosAsignaturasPage.objectName():
            GraficosAsignaturasPage.setObjectName(u"GraficosAsignaturasPage")
        self.vboxLayout = QVBoxLayout(GraficosAsignaturasPage)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.btn_volver = QPushButton(GraficosAsignaturasPage)
        self.btn_volver.setObjectName(u"btn_volver")

        self.hboxLayout.addWidget(self.btn_volver)

        self.spacerHeader = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerHeader)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.lblTitulo = QLabel(GraficosAsignaturasPage)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.lblTitulo)

        self.frameFiltros = QFrame(GraficosAsignaturasPage)
        self.frameFiltros.setObjectName(u"frameFiltros")
        self.gridLayout = QGridLayout(self.frameFiltros)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frameFiltros)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.cb_grado = QComboBox(self.frameFiltros)
        self.cb_grado.setObjectName(u"cb_grado")

        self.gridLayout.addWidget(self.cb_grado, 0, 1, 1, 1)

        self.label1 = QLabel(self.frameFiltros)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 0, 2, 1, 1)

        self.cb_curso = QComboBox(self.frameFiltros)
        self.cb_curso.setObjectName(u"cb_curso")

        self.gridLayout.addWidget(self.cb_curso, 0, 3, 1, 1)

        self.btn_reset = QPushButton(self.frameFiltros)
        self.btn_reset.setObjectName(u"btn_reset")

        self.gridLayout.addWidget(self.btn_reset, 0, 4, 1, 1)

        self.label2 = QLabel(self.frameFiltros)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)

        self.cb_cuatrimestre = QComboBox(self.frameFiltros)
        self.cb_cuatrimestre.setObjectName(u"cb_cuatrimestre")

        self.gridLayout.addWidget(self.cb_cuatrimestre, 1, 1, 1, 1)

        self.label3 = QLabel(self.frameFiltros)
        self.label3.setObjectName(u"label3")

        self.gridLayout.addWidget(self.label3, 1, 2, 1, 1)

        self.cb_tipo = QComboBox(self.frameFiltros)
        self.cb_tipo.setObjectName(u"cb_tipo")

        self.gridLayout.addWidget(self.cb_tipo, 1, 3, 1, 1)

        self.btn_exportar = QPushButton(self.frameFiltros)
        self.btn_exportar.setObjectName(u"btn_exportar")

        self.gridLayout.addWidget(self.btn_exportar, 1, 4, 1, 1)


        self.vboxLayout.addWidget(self.frameFiltros)

        self.lbl_resumen = QLabel(GraficosAsignaturasPage)
        self.lbl_resumen.setObjectName(u"lbl_resumen")

        self.vboxLayout.addWidget(self.lbl_resumen)

        self.gridLayout1 = QGridLayout()
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.frame_grafico1 = QFrame(GraficosAsignaturasPage)
        self.frame_grafico1.setObjectName(u"frame_grafico1")
        self.vboxLayout1 = QVBoxLayout(self.frame_grafico1)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.label4 = QLabel(self.frame_grafico1)
        self.label4.setObjectName(u"label4")

        self.vboxLayout1.addWidget(self.label4)

        self.grafico_curso = QWidget(self.frame_grafico1)
        self.grafico_curso.setObjectName(u"grafico_curso")

        self.vboxLayout1.addWidget(self.grafico_curso)


        self.gridLayout1.addWidget(self.frame_grafico1, 0, 0, 1, 1)

        self.frame_grafico2 = QFrame(GraficosAsignaturasPage)
        self.frame_grafico2.setObjectName(u"frame_grafico2")
        self.vboxLayout2 = QVBoxLayout(self.frame_grafico2)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.label5 = QLabel(self.frame_grafico2)
        self.label5.setObjectName(u"label5")

        self.vboxLayout2.addWidget(self.label5)

        self.grafico_tipo = QWidget(self.frame_grafico2)
        self.grafico_tipo.setObjectName(u"grafico_tipo")

        self.vboxLayout2.addWidget(self.grafico_tipo)


        self.gridLayout1.addWidget(self.frame_grafico2, 0, 1, 1, 1)

        self.frame_grafico3 = QFrame(GraficosAsignaturasPage)
        self.frame_grafico3.setObjectName(u"frame_grafico3")
        self.vboxLayout3 = QVBoxLayout(self.frame_grafico3)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.label6 = QLabel(self.frame_grafico3)
        self.label6.setObjectName(u"label6")

        self.vboxLayout3.addWidget(self.label6)

        self.grafico_creditos = QWidget(self.frame_grafico3)
        self.grafico_creditos.setObjectName(u"grafico_creditos")

        self.vboxLayout3.addWidget(self.grafico_creditos)


        self.gridLayout1.addWidget(self.frame_grafico3, 1, 0, 1, 1)

        self.frame_grafico4 = QFrame(GraficosAsignaturasPage)
        self.frame_grafico4.setObjectName(u"frame_grafico4")
        self.vboxLayout4 = QVBoxLayout(self.frame_grafico4)
        self.vboxLayout4.setObjectName(u"vboxLayout4")
        self.label7 = QLabel(self.frame_grafico4)
        self.label7.setObjectName(u"label7")

        self.vboxLayout4.addWidget(self.label7)

        self.grafico_cuatrimestre = QWidget(self.frame_grafico4)
        self.grafico_cuatrimestre.setObjectName(u"grafico_cuatrimestre")

        self.vboxLayout4.addWidget(self.grafico_cuatrimestre)


        self.gridLayout1.addWidget(self.frame_grafico4, 1, 1, 1, 1)


        self.vboxLayout.addLayout(self.gridLayout1)


        self.retranslateUi(GraficosAsignaturasPage)

        QMetaObject.connectSlotsByName(GraficosAsignaturasPage)
    # setupUi

    def retranslateUi(self, GraficosAsignaturasPage):
        self.btn_volver.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"\u2190 Volver", None))
        self.lblTitulo.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Dashboard de Asignaturas", None))
        self.label.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Grado:", None))
        self.label1.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Curso:", None))
        self.btn_reset.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Vaciar campos", None))
        self.label2.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Cuatrimestre:", None))
        self.label3.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Tipo:", None))
        self.btn_exportar.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Exportar", None))
        self.lbl_resumen.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Filtros activos...", None))
        self.label4.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Asignaturas por curso", None))
        self.label5.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Tipo de asignaturas", None))
        self.label6.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Cr\u00e9ditos por curso", None))
        self.label7.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Distribuci\u00f3n por cuatrimestre", None))
        pass
    # retranslateUi

