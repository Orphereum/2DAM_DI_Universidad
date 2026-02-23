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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.gridLayoutMain = QGridLayout(self.frameMain)
        self.gridLayoutMain.setObjectName(u"gridLayoutMain")
        self.grp_formulario = QGroupBox(self.frameMain)
        self.grp_formulario.setObjectName(u"grp_formulario")
        self.formLayout = QFormLayout(self.grp_formulario)
        self.formLayout.setObjectName(u"formLayout")
        self.labelNombre = QLabel(self.grp_formulario)
        self.labelNombre.setObjectName(u"labelNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelNombre)

        self.txt_nombre = QLineEdit(self.grp_formulario)
        self.txt_nombre.setObjectName(u"txt_nombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_nombre)

        self.labelCreditos = QLabel(self.grp_formulario)
        self.labelCreditos.setObjectName(u"labelCreditos")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelCreditos)

        self.sp_creditos = QSpinBox(self.grp_formulario)
        self.sp_creditos.setObjectName(u"sp_creditos")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sp_creditos)

        self.labelCurso = QLabel(self.grp_formulario)
        self.labelCurso.setObjectName(u"labelCurso")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelCurso)

        self.cb_curso = QComboBox(self.grp_formulario)
        self.cb_curso.setObjectName(u"cb_curso")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cb_curso)

        self.labelCuatrimestre = QLabel(self.grp_formulario)
        self.labelCuatrimestre.setObjectName(u"labelCuatrimestre")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.labelCuatrimestre)

        self.cb_cuatrimestre = QComboBox(self.grp_formulario)
        self.cb_cuatrimestre.setObjectName(u"cb_cuatrimestre")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cb_cuatrimestre)

        self.labelTipo = QLabel(self.grp_formulario)
        self.labelTipo.setObjectName(u"labelTipo")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.labelTipo)

        self.chk_obligatoria = QCheckBox(self.grp_formulario)
        self.chk_obligatoria.setObjectName(u"chk_obligatoria")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.chk_obligatoria)

        self.btn_guardar = QPushButton(self.grp_formulario)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.btn_guardar)

        self.btn_cancelar = QPushButton(self.grp_formulario)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.btn_cancelar)


        self.gridLayoutMain.addWidget(self.grp_formulario, 0, 0, 3, 1)

        self.lblTablaTitulo = QLabel(self.frameMain)
        self.lblTablaTitulo.setObjectName(u"lblTablaTitulo")
        self.lblTablaTitulo.setFont(font1)

        self.gridLayoutMain.addWidget(self.lblTablaTitulo, 0, 1, 1, 1)

        self.tbl_asignaturas = QTableWidget(self.frameMain)
        self.tbl_asignaturas.setObjectName(u"tbl_asignaturas")

        self.gridLayoutMain.addWidget(self.tbl_asignaturas, 1, 1, 1, 1)

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


        self.gridLayoutMain.addLayout(self.hboxLayout1, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.frameMain)

        self.verticalSpacerBottom = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerBottom)


        self.retranslateUi(AsignaturasView)

        QMetaObject.connectSlotsByName(AsignaturasView)
    # setupUi

    def retranslateUi(self, AsignaturasView):
        AsignaturasView.setWindowTitle(QCoreApplication.translate("AsignaturasView", u"Asignaturas", None))
        self.lblTitulo.setText(QCoreApplication.translate("AsignaturasView", u"ASIGNATURAS", None))
        self.lblContexto.setText(QCoreApplication.translate("AsignaturasView", u"Grado seleccionado:", None))
        self.grp_formulario.setTitle(QCoreApplication.translate("AsignaturasView", u"Datos de la asignatura", None))
        self.labelNombre.setText(QCoreApplication.translate("AsignaturasView", u"Nombre:", None))
        self.labelCreditos.setText(QCoreApplication.translate("AsignaturasView", u"Cr\u00e9ditos:", None))
        self.labelCurso.setText(QCoreApplication.translate("AsignaturasView", u"Curso:", None))
        self.labelCuatrimestre.setText(QCoreApplication.translate("AsignaturasView", u"Cuatrimestre:", None))
        self.labelTipo.setText(QCoreApplication.translate("AsignaturasView", u"Obligatoria:", None))
        self.btn_guardar.setText(QCoreApplication.translate("AsignaturasView", u"Guardar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("AsignaturasView", u"Cancelar", None))
        self.lblTablaTitulo.setText(QCoreApplication.translate("AsignaturasView", u"Listado de asignaturas", None))
        self.btn_nueva.setText(QCoreApplication.translate("AsignaturasView", u"Nueva", None))
        self.btn_editar.setText(QCoreApplication.translate("AsignaturasView", u"Editar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("AsignaturasView", u"Eliminar", None))
        self.btn_refrescar.setText(QCoreApplication.translate("AsignaturasView", u"Refrescar", None))
        self.btnExportarPdf.setText(QCoreApplication.translate("AsignaturasView", u"Exportar PDF", None))
    # retranslateUi

