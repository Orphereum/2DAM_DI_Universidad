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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_InformeAsignaturasPage(object):
    def setupUi(self, InformeAsignaturasPage):
        if not InformeAsignaturasPage.objectName():
            InformeAsignaturasPage.setObjectName(u"InformeAsignaturasPage")
        InformeAsignaturasPage.resize(798, 486)
        self.verticalLayout = QVBoxLayout(InformeAsignaturasPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitulo = QLabel(InformeAsignaturasPage)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.groupFiltros = QGroupBox(InformeAsignaturasPage)
        self.groupFiltros.setObjectName(u"groupFiltros")
        self.gridLayout = QGridLayout(self.groupFiltros)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelTipoInforme = QLabel(self.groupFiltros)
        self.labelTipoInforme.setObjectName(u"labelTipoInforme")

        self.gridLayout.addWidget(self.labelTipoInforme, 0, 0, 1, 1)

        self.cb_tipo_informe = QComboBox(self.groupFiltros)
        self.cb_tipo_informe.addItem("")
        self.cb_tipo_informe.setObjectName(u"cb_tipo_informe")

        self.gridLayout.addWidget(self.cb_tipo_informe, 0, 1, 1, 1)

        self.labelGrado = QLabel(self.groupFiltros)
        self.labelGrado.setObjectName(u"labelGrado")

        self.gridLayout.addWidget(self.labelGrado, 1, 0, 1, 1)

        self.cb_grado = QComboBox(self.groupFiltros)
        self.cb_grado.setObjectName(u"cb_grado")

        self.gridLayout.addWidget(self.cb_grado, 1, 1, 1, 1)

        self.labelCurso = QLabel(self.groupFiltros)
        self.labelCurso.setObjectName(u"labelCurso")

        self.gridLayout.addWidget(self.labelCurso, 2, 0, 1, 1)

        self.cb_curso = QComboBox(self.groupFiltros)
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.setObjectName(u"cb_curso")

        self.gridLayout.addWidget(self.cb_curso, 2, 1, 1, 1)

        self.labelCuatrimestre = QLabel(self.groupFiltros)
        self.labelCuatrimestre.setObjectName(u"labelCuatrimestre")

        self.gridLayout.addWidget(self.labelCuatrimestre, 3, 0, 1, 1)

        self.cb_cuatrimestre = QComboBox(self.groupFiltros)
        self.cb_cuatrimestre.addItem("")
        self.cb_cuatrimestre.addItem("")
        self.cb_cuatrimestre.addItem("")
        self.cb_cuatrimestre.setObjectName(u"cb_cuatrimestre")

        self.gridLayout.addWidget(self.cb_cuatrimestre, 3, 1, 1, 1)

        self.labelTipo = QLabel(self.groupFiltros)
        self.labelTipo.setObjectName(u"labelTipo")

        self.gridLayout.addWidget(self.labelTipo, 4, 0, 1, 1)

        self.cb_tipo = QComboBox(self.groupFiltros)
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.setObjectName(u"cb_tipo")

        self.gridLayout.addWidget(self.cb_tipo, 4, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupFiltros)

        self.btn_generar = QPushButton(InformeAsignaturasPage)
        self.btn_generar.setObjectName(u"btn_generar")

        self.verticalLayout.addWidget(self.btn_generar)

        self.tbl_resultados = QTableWidget(InformeAsignaturasPage)
        if (self.tbl_resultados.columnCount() < 5):
            self.tbl_resultados.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_resultados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_resultados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_resultados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_resultados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_resultados.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tbl_resultados.setObjectName(u"tbl_resultados")
        self.tbl_resultados.setColumnCount(5)

        self.verticalLayout.addWidget(self.tbl_resultados)

        self.btn_exportar = QPushButton(InformeAsignaturasPage)
        self.btn_exportar.setObjectName(u"btn_exportar")

        self.verticalLayout.addWidget(self.btn_exportar)


        self.retranslateUi(InformeAsignaturasPage)

        QMetaObject.connectSlotsByName(InformeAsignaturasPage)
    # setupUi

    def retranslateUi(self, InformeAsignaturasPage):
        InformeAsignaturasPage.setWindowTitle(QCoreApplication.translate("InformeAsignaturasPage", u"Informe de Asignaturas", None))
        self.lblTitulo.setStyleSheet(QCoreApplication.translate("InformeAsignaturasPage", u"font-size: 18px; font-weight: bold;", None))
        self.lblTitulo.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Informe de Asignaturas", None))
        self.groupFiltros.setTitle(QCoreApplication.translate("InformeAsignaturasPage", u"Filtros", None))
        self.labelTipoInforme.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Tipo informe:", None))
        self.cb_tipo_informe.setItemText(0, QCoreApplication.translate("InformeAsignaturasPage", u"Asignaturas", None))

        self.labelGrado.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Grado:", None))
        self.labelCurso.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Curso:", None))
        self.cb_curso.setItemText(0, QCoreApplication.translate("InformeAsignaturasPage", u"Todos", None))
        self.cb_curso.setItemText(1, QCoreApplication.translate("InformeAsignaturasPage", u"1", None))
        self.cb_curso.setItemText(2, QCoreApplication.translate("InformeAsignaturasPage", u"2", None))
        self.cb_curso.setItemText(3, QCoreApplication.translate("InformeAsignaturasPage", u"3", None))
        self.cb_curso.setItemText(4, QCoreApplication.translate("InformeAsignaturasPage", u"4", None))

        self.labelCuatrimestre.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Cuatrimestre:", None))
        self.cb_cuatrimestre.setItemText(0, QCoreApplication.translate("InformeAsignaturasPage", u"Todos", None))
        self.cb_cuatrimestre.setItemText(1, QCoreApplication.translate("InformeAsignaturasPage", u"1", None))
        self.cb_cuatrimestre.setItemText(2, QCoreApplication.translate("InformeAsignaturasPage", u"2", None))

        self.labelTipo.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Tipo:", None))
        self.cb_tipo.setItemText(0, QCoreApplication.translate("InformeAsignaturasPage", u"Todas", None))
        self.cb_tipo.setItemText(1, QCoreApplication.translate("InformeAsignaturasPage", u"Obligatorias", None))
        self.cb_tipo.setItemText(2, QCoreApplication.translate("InformeAsignaturasPage", u"Optativas", None))

        self.btn_generar.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Generar informe", None))
        ___qtablewidgetitem = self.tbl_resultados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Nombre", None));
        ___qtablewidgetitem1 = self.tbl_resultados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Cr\u00e9ditos", None));
        ___qtablewidgetitem2 = self.tbl_resultados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Curso", None));
        ___qtablewidgetitem3 = self.tbl_resultados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Cuatrimestre", None));
        ___qtablewidgetitem4 = self.tbl_resultados.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Obligatoria", None));
        self.btn_exportar.setText(QCoreApplication.translate("InformeAsignaturasPage", u"Exportar a PDF", None))
    # retranslateUi

