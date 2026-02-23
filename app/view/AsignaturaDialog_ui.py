# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AsignaturaDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_AsignaturaDialog(object):
    def setupUi(self, AsignaturaDialog):
        if not AsignaturaDialog.objectName():
            AsignaturaDialog.setObjectName(u"AsignaturaDialog")
        AsignaturaDialog.resize(480, 420)
        AsignaturaDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(AsignaturaDialog)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.lblTitulo = QLabel(AsignaturaDialog)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setPointSize(22)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.lineSeparator = QFrame(AsignaturaDialog)
        self.lineSeparator.setObjectName(u"lineSeparator")
        self.lineSeparator.setFrameShape(QFrame.HLine)
        self.lineSeparator.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.lineSeparator)

        self.groupDatos = QGroupBox(AsignaturaDialog)
        self.groupDatos.setObjectName(u"groupDatos")
        self.formLayout = QFormLayout(self.groupDatos)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight)
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(10)
        self.lblNombre = QLabel(self.groupDatos)
        self.lblNombre.setObjectName(u"lblNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txt_nombre = QLineEdit(self.groupDatos)
        self.txt_nombre.setObjectName(u"txt_nombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_nombre)

        self.lblCreditos = QLabel(self.groupDatos)
        self.lblCreditos.setObjectName(u"lblCreditos")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblCreditos)

        self.sp_creditos = QSpinBox(self.groupDatos)
        self.sp_creditos.setObjectName(u"sp_creditos")
        self.sp_creditos.setMinimum(1)
        self.sp_creditos.setMaximum(30)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sp_creditos)

        self.lblCurso = QLabel(self.groupDatos)
        self.lblCurso.setObjectName(u"lblCurso")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblCurso)

        self.cb_curso = QComboBox(self.groupDatos)
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.setObjectName(u"cb_curso")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cb_curso)

        self.lblCuatrimestre = QLabel(self.groupDatos)
        self.lblCuatrimestre.setObjectName(u"lblCuatrimestre")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblCuatrimestre)

        self.cb_cuatrimestre = QComboBox(self.groupDatos)
        self.cb_cuatrimestre.addItem("")
        self.cb_cuatrimestre.addItem("")
        self.cb_cuatrimestre.setObjectName(u"cb_cuatrimestre")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cb_cuatrimestre)

        self.lblGrado = QLabel(self.groupDatos)
        self.lblGrado.setObjectName(u"lblGrado")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblGrado)

        self.cb_grado = QComboBox(self.groupDatos)
        self.cb_grado.setObjectName(u"cb_grado")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cb_grado)

        self.lblObligatoria = QLabel(self.groupDatos)
        self.lblObligatoria.setObjectName(u"lblObligatoria")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblObligatoria)

        self.chk_obligatoria = QCheckBox(self.groupDatos)
        self.chk_obligatoria.setObjectName(u"chk_obligatoria")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.chk_obligatoria)


        self.verticalLayout.addWidget(self.groupDatos)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(12)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.spacerButtons = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.spacerButtons)

        self.btn_guardar = QPushButton(AsignaturaDialog)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setMinimumWidth(100)

        self.buttonsLayout.addWidget(self.btn_guardar)

        self.btn_cancelar = QPushButton(AsignaturaDialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setMinimumWidth(100)

        self.buttonsLayout.addWidget(self.btn_cancelar)


        self.verticalLayout.addLayout(self.buttonsLayout)


        self.retranslateUi(AsignaturaDialog)

        QMetaObject.connectSlotsByName(AsignaturaDialog)
    # setupUi

    def retranslateUi(self, AsignaturaDialog):
        AsignaturaDialog.setWindowTitle(QCoreApplication.translate("AsignaturaDialog", u"Asignatura", None))
        self.lblTitulo.setText(QCoreApplication.translate("AsignaturaDialog", u"ASIGNATURA", None))
        self.groupDatos.setTitle(QCoreApplication.translate("AsignaturaDialog", u"Datos de la asignatura", None))
        self.lblNombre.setText(QCoreApplication.translate("AsignaturaDialog", u"Nombre:", None))
        self.lblCreditos.setText(QCoreApplication.translate("AsignaturaDialog", u"Cr\u00e9ditos:", None))
        self.lblCurso.setText(QCoreApplication.translate("AsignaturaDialog", u"Curso:", None))
        self.cb_curso.setItemText(0, QCoreApplication.translate("AsignaturaDialog", u"1", None))
        self.cb_curso.setItemText(1, QCoreApplication.translate("AsignaturaDialog", u"2", None))
        self.cb_curso.setItemText(2, QCoreApplication.translate("AsignaturaDialog", u"3", None))
        self.cb_curso.setItemText(3, QCoreApplication.translate("AsignaturaDialog", u"4", None))

        self.lblCuatrimestre.setText(QCoreApplication.translate("AsignaturaDialog", u"Cuatrimestre:", None))
        self.cb_cuatrimestre.setItemText(0, QCoreApplication.translate("AsignaturaDialog", u"1", None))
        self.cb_cuatrimestre.setItemText(1, QCoreApplication.translate("AsignaturaDialog", u"2", None))

        self.lblGrado.setText(QCoreApplication.translate("AsignaturaDialog", u"Grado:", None))
        self.lblObligatoria.setText(QCoreApplication.translate("AsignaturaDialog", u"Obligatoria:", None))
        self.chk_obligatoria.setText(QCoreApplication.translate("AsignaturaDialog", u"S\u00ed", None))
        self.btn_guardar.setText(QCoreApplication.translate("AsignaturaDialog", u"Guardar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("AsignaturaDialog", u"Cancelar", None))
    # retranslateUi

