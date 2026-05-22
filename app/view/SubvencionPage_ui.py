# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SubvencionPage.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Subvencion_page(object):
    def setupUi(self, Subvencion_page):
        if not Subvencion_page.objectName():
            Subvencion_page.setObjectName(u"Subvencion_page")
        Subvencion_page.resize(900, 600)
        self.verticalLayout = QVBoxLayout(Subvencion_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTituloSubvenciones = QLabel(Subvencion_page)
        self.labelTituloSubvenciones.setObjectName(u"labelTituloSubvenciones")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.labelTituloSubvenciones.setFont(font)
        self.labelTituloSubvenciones.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelTituloSubvenciones)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelNombre = QLabel(Subvencion_page)
        self.labelNombre.setObjectName(u"labelNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelNombre)

        self.inputNombre = QLineEdit(Subvencion_page)
        self.inputNombre.setObjectName(u"inputNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.inputNombre)

        self.labelMin = QLabel(Subvencion_page)
        self.labelMin.setObjectName(u"labelMin")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelMin)

        self.inputImporteMin = QLineEdit(Subvencion_page)
        self.inputImporteMin.setObjectName(u"inputImporteMin")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.inputImporteMin)

        self.labelMax = QLabel(Subvencion_page)
        self.labelMax.setObjectName(u"labelMax")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelMax)

        self.inputImporteMax = QLineEdit(Subvencion_page)
        self.inputImporteMax.setObjectName(u"inputImporteMax")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.inputImporteMax)

        self.LabelInicio = QLabel(Subvencion_page)
        self.LabelInicio.setObjectName(u"LabelInicio")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.LabelInicio)

        self.inputFechaInicio = QLineEdit(Subvencion_page)
        self.inputFechaInicio.setObjectName(u"inputFechaInicio")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.inputFechaInicio)

        self.labelFin = QLabel(Subvencion_page)
        self.labelFin.setObjectName(u"labelFin")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.labelFin)

        self.inputFechaFin = QLineEdit(Subvencion_page)
        self.inputFechaFin.setObjectName(u"inputFechaFin")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.inputFechaFin)

        self.labelEstado = QLabel(Subvencion_page)
        self.labelEstado.setObjectName(u"labelEstado")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.labelEstado)

        self.inputEstado = QLineEdit(Subvencion_page)
        self.inputEstado.setObjectName(u"inputEstado")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.inputEstado)


        self.verticalLayout.addLayout(self.formLayout)

        self.layoutBotones = QHBoxLayout()
        self.layoutBotones.setObjectName(u"layoutBotones")
        self.btn_guardar = QPushButton(Subvencion_page)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.layoutBotones.addWidget(self.btn_guardar)

        self.btn_editar = QPushButton(Subvencion_page)
        self.btn_editar.setObjectName(u"btn_editar")

        self.layoutBotones.addWidget(self.btn_editar)

        self.btn_eliminar = QPushButton(Subvencion_page)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.layoutBotones.addWidget(self.btn_eliminar)

        self.btn_limpiar = QPushButton(Subvencion_page)
        self.btn_limpiar.setObjectName(u"btn_limpiar")

        self.layoutBotones.addWidget(self.btn_limpiar)


        self.verticalLayout.addLayout(self.layoutBotones)

        self.tabla_subvenciones = QTableWidget(Subvencion_page)
        if (self.tabla_subvenciones.columnCount() < 7):
            self.tabla_subvenciones.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_subvenciones.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_subvenciones.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_subvenciones.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_subvenciones.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_subvenciones.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_subvenciones.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_subvenciones.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_subvenciones.setObjectName(u"tabla_subvenciones")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.tabla_subvenciones.setFont(font1)
        self.tabla_subvenciones.horizontalHeader().setDefaultSectionSize(125)

        self.verticalLayout.addWidget(self.tabla_subvenciones)


        self.retranslateUi(Subvencion_page)

        QMetaObject.connectSlotsByName(Subvencion_page)
    # setupUi

    def retranslateUi(self, Subvencion_page):
        Subvencion_page.setWindowTitle(QCoreApplication.translate("Subvencion_page", u"Subvenciones", None))
        self.labelTituloSubvenciones.setText(QCoreApplication.translate("Subvencion_page", u"Subvenciones", None))
        self.labelNombre.setText(QCoreApplication.translate("Subvencion_page", u"Nombre:", None))
        self.labelMin.setText(QCoreApplication.translate("Subvencion_page", u"Importe m\u00ednimo:", None))
        self.labelMax.setText(QCoreApplication.translate("Subvencion_page", u"Importe m\u00e1ximo:", None))
        self.LabelInicio.setText(QCoreApplication.translate("Subvencion_page", u"Fecha inicio:", None))
        self.labelFin.setText(QCoreApplication.translate("Subvencion_page", u"Fecha fin:", None))
        self.labelEstado.setText(QCoreApplication.translate("Subvencion_page", u"Estado:", None))
        self.btn_guardar.setText(QCoreApplication.translate("Subvencion_page", u"Guardar", None))
        self.btn_editar.setText(QCoreApplication.translate("Subvencion_page", u"Editar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Subvencion_page", u"Eliminar", None))
        self.btn_limpiar.setText(QCoreApplication.translate("Subvencion_page", u"Limpiar", None))
        ___qtablewidgetitem = self.tabla_subvenciones.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Subvencion_page", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_subvenciones.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Subvencion_page", u"Nombre", None));
        ___qtablewidgetitem2 = self.tabla_subvenciones.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Subvencion_page", u"Min", None));
        ___qtablewidgetitem3 = self.tabla_subvenciones.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Subvencion_page", u"Max", None));
        ___qtablewidgetitem4 = self.tabla_subvenciones.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Subvencion_page", u"Fecha inicio", None));
        ___qtablewidgetitem5 = self.tabla_subvenciones.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Subvencion_page", u"Fecha fin", None));
        ___qtablewidgetitem6 = self.tabla_subvenciones.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Subvencion_page", u"Estado", None));
    # retranslateUi

