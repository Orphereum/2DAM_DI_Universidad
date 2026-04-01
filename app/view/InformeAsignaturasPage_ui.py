# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InformeAsignaturasPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
class Ui_InformeAsignaturasPage(object):
    def setupUi(self, InformeAsignaturasPage):
        if not InformeAsignaturasPage.objectName():
            InformeAsignaturasPage.setObjectName(u"InformeAsignaturasPage")
        self.vboxLayout = QVBoxLayout(InformeAsignaturasPage)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.lblTitulo = QLabel(InformeAsignaturasPage)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.lblTitulo)

        self.groupFiltros = QGroupBox(InformeAsignaturasPage)
        self.groupFiltros.setObjectName(u"groupFiltros")
        self.gridLayout = QGridLayout(self.groupFiltros)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupFiltros)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.cb_grado = QComboBox(self.groupFiltros)
        self.cb_grado.setObjectName(u"cb_grado")

        self.gridLayout.addWidget(self.cb_grado, 0, 1, 1, 1)

        self.label1 = QLabel(self.groupFiltros)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 1, 0, 1, 1)

        self.cb_curso = QComboBox(self.groupFiltros)
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.setObjectName(u"cb_curso")

        self.gridLayout.addWidget(self.cb_curso, 1, 1, 1, 1)

        self.label2 = QLabel(self.groupFiltros)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 2, 0, 1, 1)

        self.cb_cuatrimestre = QComboBox(self.groupFiltros)
        self.cb_cuatrimestre.addItem("")
        self.cb_cuatrimestre.addItem("")
        self.cb_cuatrimestre.addItem("")
        self.cb_cuatrimestre.setObjectName(u"cb_cuatrimestre")

        self.gridLayout.addWidget(self.cb_cuatrimestre, 2, 1, 1, 1)

        self.label3 = QLabel(self.groupFiltros)
        self.label3.setObjectName(u"label3")

        self.gridLayout.addWidget(self.label3, 3, 0, 1, 1)

        self.cb_tipo = QComboBox(self.groupFiltros)
        self.cb_tipo.setObjectName(u"cb_tipo")

        self.gridLayout.addWidget(self.cb_tipo, 3, 1, 1, 1)


        self.vboxLayout.addWidget(self.groupFiltros)

        self.tbl_resultados = QTableWidget(InformeAsignaturasPage)
        self.tbl_resultados.setObjectName(u"tbl_resultados")

        self.vboxLayout.addWidget(self.tbl_resultados)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.btn_generar = QPushButton(InformeAsignaturasPage)
        self.btn_generar.setObjectName(u"btn_generar")

        self.hboxLayout.addWidget(self.btn_generar)

        self.btn_exportar = QPushButton(InformeAsignaturasPage)
        self.btn_exportar.setObjectName(u"btn_exportar")

        self.hboxLayout.addWidget(self.btn_exportar)

        self.btn_cerrar = QPushButton(InformeAsignaturasPage)
        self.btn_cerrar.setObjectName(u"btn_cerrar")

        self.hboxLayout.addWidget(self.btn_cerrar)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.retranslateUi(InformeAsignaturasPage)

        QMetaObject.connectSlotsByName(InformeAsignaturasPage)
    # setupUi

    def retranslateUi(self, InformeAsignaturasPage):
        InformeAsignaturasPage.setWindowTitle(QCoreApplication.translate("InformeAsignaturasPage", u"Informe de Asignaturas", None))
        self.lblTitulo.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Informe de Asignaturas", None))
        self.groupFiltros.setTitle(QCoreApplication.translate("InformeAsignaturasPage", u"Filtros", None))
        self.label.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Grado:", None))
        self.label1.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Curso:", None))
        self.cb_curso.setItemText(0, QCoreApplication.translate("InformeAsignaturasPage", u"Todos", None))
        self.cb_curso.setItemText(1, QCoreApplication.translate("InformeAsignaturasPage", u"1", None))
        self.cb_curso.setItemText(2, QCoreApplication.translate("InformeAsignaturasPage", u"2", None))
        self.cb_curso.setItemText(3, QCoreApplication.translate("InformeAsignaturasPage", u"3", None))
        self.cb_curso.setItemText(4, QCoreApplication.translate("InformeAsignaturasPage", u"4", None))

        self.label2.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Cuatrimestre:", None))
        self.cb_cuatrimestre.setItemText(0, QCoreApplication.translate("InformeAsignaturasPage", u"Todos", None))
        self.cb_cuatrimestre.setItemText(1, QCoreApplication.translate("InformeAsignaturasPage", u"1", None))
        self.cb_cuatrimestre.setItemText(2, QCoreApplication.translate("InformeAsignaturasPage", u"2", None))

        self.label3.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Tipo:", None))
        self.btn_generar.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Generar informe", None))
        self.btn_exportar.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Exportar PDF", None))
        self.btn_cerrar.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Cerrar", None))
    # retranslateUi

