# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GradoPage.ui'
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
    QFrame, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(657, 628)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.lblgrado = QLabel(Form)
        self.lblgrado.setObjectName(u"lblgrado")
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        self.lblgrado.setFont(font)
        self.lblgrado.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblgrado)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.cb_facultad = QComboBox(self.widget)
        self.cb_facultad.setObjectName(u"cb_facultad")
        self.cb_facultad.setMaximumSize(QSize(200, 200))

        self.gridLayout_2.addWidget(self.cb_facultad, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_nuevo = QPushButton(self.frame_3)
        self.btn_nuevo.setObjectName(u"btn_nuevo")
        self.btn_nuevo.setMaximumSize(QSize(100000, 16777215))

        self.gridLayout.addWidget(self.btn_nuevo, 2, 5, 1, 1)

        self.btn_eliminar = QPushButton(self.frame_3)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.gridLayout.addWidget(self.btn_eliminar, 4, 5, 1, 1)

        self.tbl_grados = QTableWidget(self.frame_3)
        if (self.tbl_grados.columnCount() < 7):
            self.tbl_grados.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_grados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_grados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_grados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_grados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_grados.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_grados.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_grados.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tbl_grados.setObjectName(u"tbl_grados")

        self.gridLayout.addWidget(self.tbl_grados, 1, 5, 1, 1)

        self.grp_formulario = QGroupBox(self.frame_3)
        self.grp_formulario.setObjectName(u"grp_formulario")
        self.grp_formulario.setMinimumSize(QSize(200, 200))
        self.formLayout_2 = QFormLayout(self.grp_formulario)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.grp_formulario)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.txt_nombre = QLineEdit(self.grp_formulario)
        self.txt_nombre.setObjectName(u"txt_nombre")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_nombre)

        self.label_5 = QLabel(self.grp_formulario)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_7 = QLabel(self.grp_formulario)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label_8 = QLabel(self.grp_formulario)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.label_6 = QLabel(self.grp_formulario)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.label_9 = QLabel(self.grp_formulario)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.txt_codigo = QLineEdit(self.grp_formulario)
        self.txt_codigo.setObjectName(u"txt_codigo")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_codigo)

        self.sp_duracion = QSpinBox(self.grp_formulario)
        self.sp_duracion.setObjectName(u"sp_duracion")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.sp_duracion)

        self.sp_creditos = QSpinBox(self.grp_formulario)
        self.sp_creditos.setObjectName(u"sp_creditos")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.sp_creditos)

        self.cb_tipo = QComboBox(self.grp_formulario)
        self.cb_tipo.setObjectName(u"cb_tipo")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cb_tipo)

        self.chk_activo = QCheckBox(self.grp_formulario)
        self.chk_activo.setObjectName(u"chk_activo")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.chk_activo)

        self.btn_guardar = QPushButton(self.grp_formulario)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.FieldRole, self.btn_guardar)

        self.btn_cancelar = QPushButton(self.grp_formulario)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.LabelRole, self.btn_cancelar)


        self.gridLayout.addWidget(self.grp_formulario, 1, 1, 2, 1)

        self.btn_refrescar = QPushButton(self.frame_3)
        self.btn_refrescar.setObjectName(u"btn_refrescar")

        self.gridLayout.addWidget(self.btn_refrescar, 5, 5, 1, 1)

        self.btn_editar = QPushButton(self.frame_3)
        self.btn_editar.setObjectName(u"btn_editar")

        self.gridLayout.addWidget(self.btn_editar, 3, 5, 1, 1)

        self.widget_2 = QWidget(self.frame_3)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 16777215))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 5, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblgrado.setText(QCoreApplication.translate("Form", u"GRADO", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Facultad:", None))
        self.btn_nuevo.setText(QCoreApplication.translate("Form", u"Nuevo", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        ___qtablewidgetitem = self.tbl_grados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id_grado", None));
        ___qtablewidgetitem1 = self.tbl_grados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"nombre", None));
        ___qtablewidgetitem2 = self.tbl_grados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"c\u00f3digo", None));
        ___qtablewidgetitem3 = self.tbl_grados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"duracion (a\u00f1os)", None));
        ___qtablewidgetitem4 = self.tbl_grados.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"cr\u00e9ditos", None));
        ___qtablewidgetitem5 = self.tbl_grados.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"tipo", None));
        ___qtablewidgetitem6 = self.tbl_grados.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"estado", None));
        self.grp_formulario.setTitle(QCoreApplication.translate("Form", u"Campos", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Nombre:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"C\u00f3digo:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Duraci\u00f3n:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Cr\u00e9ditos:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Tipo:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Estado:", None))
        self.chk_activo.setText(QCoreApplication.translate("Form", u"Activo", None))
        self.btn_guardar.setText(QCoreApplication.translate("Form", u"Guardar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.btn_refrescar.setText(QCoreApplication.translate("Form", u"Refrescar", None))
        self.btn_editar.setText(QCoreApplication.translate("Form", u"Editar", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Grados:", None))
    # retranslateUi

