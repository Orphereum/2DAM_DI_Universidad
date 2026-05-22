# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Facultad.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(880, 614)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 851, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblFacultad = QLabel(self.verticalLayoutWidget)
        self.lblFacultad.setObjectName(u"lblFacultad")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFacultad.sizePolicy().hasHeightForWidth())
        self.lblFacultad.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(30)
        self.lblFacultad.setFont(font)
        self.lblFacultad.setTextFormat(Qt.TextFormat.MarkdownText)
        self.lblFacultad.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.lblFacultad)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.actualizarPB = QPushButton(self.verticalLayoutWidget)
        self.actualizarPB.setObjectName(u"actualizarPB")

        self.gridLayout.addWidget(self.actualizarPB, 1, 2, 1, 1)

        self.guardarPB = QPushButton(self.verticalLayoutWidget)
        self.guardarPB.setObjectName(u"guardarPB")

        self.gridLayout.addWidget(self.guardarPB, 1, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit)


        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)

        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 0, 2, 1, 1)

        self.eliminarPorNombrePB = QPushButton(self.verticalLayoutWidget)
        self.eliminarPorNombrePB.setObjectName(u"eliminarPorNombrePB")

        self.gridLayout.addWidget(self.eliminarPorNombrePB, 2, 1, 1, 1)

        self.eliminarPB = QPushButton(self.verticalLayoutWidget)
        self.eliminarPB.setObjectName(u"eliminarPB")

        self.gridLayout.addWidget(self.eliminarPB, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lblFacultad.setText(QCoreApplication.translate("Dialog", u"Facultad", None))
        self.actualizarPB.setText(QCoreApplication.translate("Dialog", u"Actualizar Facultad", None))
        self.guardarPB.setText(QCoreApplication.translate("Dialog", u"Guardar Facultad", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nombre:", None))
        self.eliminarPorNombrePB.setText(QCoreApplication.translate("Dialog", u"Eliminar Facultad", None))
        self.eliminarPB.setText(QCoreApplication.translate("Dialog", u"Eliminar Seleccionada", None))
    # retranslateUi

