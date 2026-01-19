# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Asignaturas.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_AsignaturasView(object):
    def setupUi(self, AsignaturasView):
        if not AsignaturasView.objectName():
            AsignaturasView.setObjectName(u"AsignaturasView")
        AsignaturasView.resize(700, 650)
        self.verticalLayout = QVBoxLayout(AsignaturasView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacerTop = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerTop)

        self.frameHeader = QFrame(AsignaturasView)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.gridLayoutHeader = QGridLayout(self.frameHeader)
        self.gridLayoutHeader.setObjectName(u"gridLayoutHeader")
        self.lblTitulo = QLabel(self.frameHeader)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setPointSize(24)
        font.setBold(True)
        self.lblTitulo.setFont(font)

        self.gridLayoutHeader.addWidget(self.lblTitulo, 0, 1, 1, 1)

        self.spacerLeft = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutHeader.addItem(self.spacerLeft, 0, 0, 1, 1)

        self.spacerRight = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutHeader.addItem(self.spacerRight, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.frameHeader)

        self.frameContexto = QFrame(AsignaturasView)
        self.frameContexto.setObjectName(u"frameContexto")
        self.frameContexto.setFrameShape(QFrame.Shape.StyledPanel)
        self.gridLayoutContexto = QGridLayout(self.frameContexto)
        self.gridLayoutContexto.setObjectName(u"gridLayoutContexto")
        self.lblContexto = QLabel(self.frameContexto)
        self.lblContexto.setObjectName(u"lblContexto")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        self.lblContexto.setFont(font1)

        self.gridLayoutContexto.addWidget(self.lblContexto, 0, 1, 1, 1)

        self.spacerCtxLeft = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutContexto.addItem(self.spacerCtxLeft, 0, 0, 1, 1)

        self.spacerCtxRight = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutContexto.addItem(self.spacerCtxRight, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.frameContexto)

        self.frameMain = QFrame(AsignaturasView)
        self.frameMain.setObjectName(u"frameMain")
        self.frameMain.setFrameShape(QFrame.Shape.StyledPanel)
        self.gridLayoutMain = QGridLayout(self.frameMain)
        self.gridLayoutMain.setObjectName(u"gridLayoutMain")
        self.filtersLayout = QHBoxLayout()
        self.filtersLayout.setObjectName(u"filtersLayout")
        self.txt_buscar = QLineEdit(self.frameMain)
        self.txt_buscar.setObjectName(u"txt_buscar")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.txt_buscar.setFont(font2)

        self.filtersLayout.addWidget(self.txt_buscar)

        self.lblCurso = QLabel(self.frameMain)
        self.lblCurso.setObjectName(u"lblCurso")

        self.filtersLayout.addWidget(self.lblCurso)

        self.cb_curso = QComboBox(self.frameMain)
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.setObjectName(u"cb_curso")

        self.filtersLayout.addWidget(self.cb_curso)

        self.lblCuatrimestre = QLabel(self.frameMain)
        self.lblCuatrimestre.setObjectName(u"lblCuatrimestre")

        self.filtersLayout.addWidget(self.lblCuatrimestre)

        self.cb_cuatrimestre = QComboBox(self.frameMain)
        self.cb_cuatrimestre.addItem("")
        self.cb_cuatrimestre.addItem("")
        self.cb_cuatrimestre.addItem("")
        self.cb_cuatrimestre.setObjectName(u"cb_cuatrimestre")

        self.filtersLayout.addWidget(self.cb_cuatrimestre)

        self.lblTipo = QLabel(self.frameMain)
        self.lblTipo.setObjectName(u"lblTipo")

        self.filtersLayout.addWidget(self.lblTipo)

        self.cb_obligatoria = QComboBox(self.frameMain)
        self.cb_obligatoria.addItem("")
        self.cb_obligatoria.addItem("")
        self.cb_obligatoria.addItem("")
        self.cb_obligatoria.setObjectName(u"cb_obligatoria")

        self.filtersLayout.addWidget(self.cb_obligatoria)


        self.gridLayoutMain.addLayout(self.filtersLayout, 0, 0, 1, 2)

        self.tbl_asignaturas = QTableWidget(self.frameMain)
        self.tbl_asignaturas.setObjectName(u"tbl_asignaturas")

        self.gridLayoutMain.addWidget(self.tbl_asignaturas, 1, 0, 4, 1)

        self.btn_nueva = QPushButton(self.frameMain)
        self.btn_nueva.setObjectName(u"btn_nueva")

        self.gridLayoutMain.addWidget(self.btn_nueva, 1, 1, 1, 1)

        self.btn_editar = QPushButton(self.frameMain)
        self.btn_editar.setObjectName(u"btn_editar")

        self.gridLayoutMain.addWidget(self.btn_editar, 2, 1, 1, 1)

        self.btn_eliminar = QPushButton(self.frameMain)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.gridLayoutMain.addWidget(self.btn_eliminar, 3, 1, 1, 1)

        self.btn_refrescar = QPushButton(self.frameMain)
        self.btn_refrescar.setObjectName(u"btn_refrescar")

        self.gridLayoutMain.addWidget(self.btn_refrescar, 4, 1, 1, 1)

        self.relationsLayout = QHBoxLayout()
        self.relationsLayout.setObjectName(u"relationsLayout")
        self.btn_profesores = QPushButton(self.frameMain)
        self.btn_profesores.setObjectName(u"btn_profesores")

        self.relationsLayout.addWidget(self.btn_profesores)

        self.btn_alumnos = QPushButton(self.frameMain)
        self.btn_alumnos.setObjectName(u"btn_alumnos")

        self.relationsLayout.addWidget(self.btn_alumnos)

        self.btn_clases = QPushButton(self.frameMain)
        self.btn_clases.setObjectName(u"btn_clases")

        self.relationsLayout.addWidget(self.btn_clases)


        self.gridLayoutMain.addLayout(self.relationsLayout, 5, 0, 1, 2)

        self.lbl_estado = QLabel(self.frameMain)
        self.lbl_estado.setObjectName(u"lbl_estado")

        self.gridLayoutMain.addWidget(self.lbl_estado, 6, 0, 1, 2)


        self.verticalLayout.addWidget(self.frameMain)


        self.retranslateUi(AsignaturasView)

        QMetaObject.connectSlotsByName(AsignaturasView)
    # setupUi

    def retranslateUi(self, AsignaturasView):
        AsignaturasView.setWindowTitle(QCoreApplication.translate("AsignaturasView", u"Asignaturas", None))
        self.lblTitulo.setText(QCoreApplication.translate("AsignaturasView", u"ASIGNATURAS", None))
        self.lblContexto.setText(QCoreApplication.translate("AsignaturasView", u"Grado seleccionado:", None))
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("AsignaturasView", u"Buscar asignatura...", None))
        self.lblCurso.setText(QCoreApplication.translate("AsignaturasView", u"Curso:", None))
        self.cb_curso.setItemText(0, QCoreApplication.translate("AsignaturasView", u"Todos", None))
        self.cb_curso.setItemText(1, QCoreApplication.translate("AsignaturasView", u"1\u00ba", None))
        self.cb_curso.setItemText(2, QCoreApplication.translate("AsignaturasView", u"2\u00ba", None))
        self.cb_curso.setItemText(3, QCoreApplication.translate("AsignaturasView", u"3\u00ba", None))
        self.cb_curso.setItemText(4, QCoreApplication.translate("AsignaturasView", u"4\u00ba", None))

        self.lblCuatrimestre.setText(QCoreApplication.translate("AsignaturasView", u"Cuatrimestre:", None))
        self.cb_cuatrimestre.setItemText(0, QCoreApplication.translate("AsignaturasView", u"Todos", None))
        self.cb_cuatrimestre.setItemText(1, QCoreApplication.translate("AsignaturasView", u"1\u00ba", None))
        self.cb_cuatrimestre.setItemText(2, QCoreApplication.translate("AsignaturasView", u"2\u00ba", None))

        self.lblTipo.setText(QCoreApplication.translate("AsignaturasView", u"Tipo:", None))
        self.cb_obligatoria.setItemText(0, QCoreApplication.translate("AsignaturasView", u"Todas", None))
        self.cb_obligatoria.setItemText(1, QCoreApplication.translate("AsignaturasView", u"Obligatorias", None))
        self.cb_obligatoria.setItemText(2, QCoreApplication.translate("AsignaturasView", u"Optativas", None))

        self.btn_nueva.setText(QCoreApplication.translate("AsignaturasView", u"Nueva", None))
        self.btn_editar.setText(QCoreApplication.translate("AsignaturasView", u"Editar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("AsignaturasView", u"Eliminar", None))
        self.btn_refrescar.setText(QCoreApplication.translate("AsignaturasView", u"Refrescar", None))
        self.btn_profesores.setText(QCoreApplication.translate("AsignaturasView", u"Profesores", None))
        self.btn_alumnos.setText(QCoreApplication.translate("AsignaturasView", u"Alumnos", None))
        self.btn_clases.setText(QCoreApplication.translate("AsignaturasView", u"Clases", None))
        self.lbl_estado.setText(QCoreApplication.translate("AsignaturasView", u"Listo", None))
    # retranslateUi

