# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GraficosAsignaturasPage.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_GraficosAsignaturasPage(object):
    def setupUi(self, GraficosAsignaturasPage):
        if not GraficosAsignaturasPage.objectName():
            GraficosAsignaturasPage.setObjectName(u"GraficosAsignaturasPage")
        GraficosAsignaturasPage.resize(900, 600)
        self.vboxLayout = QVBoxLayout(GraficosAsignaturasPage)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.lblTitulo = QLabel(GraficosAsignaturasPage)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.lblTitulo)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.btn_curso = QPushButton(GraficosAsignaturasPage)
        self.btn_curso.setObjectName(u"btn_curso")

        self.hboxLayout.addWidget(self.btn_curso)

        self.btn_tipo = QPushButton(GraficosAsignaturasPage)
        self.btn_tipo.setObjectName(u"btn_tipo")

        self.hboxLayout.addWidget(self.btn_tipo)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.frame_grafico = QFrame(GraficosAsignaturasPage)
        self.frame_grafico.setObjectName(u"frame_grafico")
        self.frame_grafico.setFrameShape(QFrame.StyledPanel)
        self.vboxLayout1 = QVBoxLayout(self.frame_grafico)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.widget_grafico = QWidget(self.frame_grafico)
        self.widget_grafico.setObjectName(u"widget_grafico")

        self.vboxLayout1.addWidget(self.widget_grafico)


        self.vboxLayout.addWidget(self.frame_grafico)


        self.retranslateUi(GraficosAsignaturasPage)

        QMetaObject.connectSlotsByName(GraficosAsignaturasPage)
    # setupUi

    def retranslateUi(self, GraficosAsignaturasPage):
        GraficosAsignaturasPage.setWindowTitle(QCoreApplication.translate("GraficosAsignaturasPage", u"Gr\u00e1ficos de Asignaturas", None))
        self.lblTitulo.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Gr\u00e1ficos de Asignaturas", None))
        self.lblTitulo.setStyleSheet(QCoreApplication.translate("GraficosAsignaturasPage", u"font-size: 20px; font-weight: bold;", None))
        self.btn_curso.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Asignaturas por Curso", None))
        self.btn_tipo.setText(QCoreApplication.translate("GraficosAsignaturasPage", u"Obligatorias vs Optativas", None))
    # retranslateUi

