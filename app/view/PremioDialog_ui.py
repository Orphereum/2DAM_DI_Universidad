# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PremioDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QPlainTextEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_PremioDialog(object):
    def setupUi(self, PremioDialog):
        if not PremioDialog.objectName():
            PremioDialog.setObjectName(u"PremioDialog")
        PremioDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(PremioDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelNombre = QLabel(PremioDialog)
        self.labelNombre.setObjectName(u"labelNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelNombre)

        self.txtNombre = QLineEdit(PremioDialog)
        self.txtNombre.setObjectName(u"txtNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.labelDesc = QLabel(PremioDialog)
        self.labelDesc.setObjectName(u"labelDesc")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelDesc)

        self.txtDescripcion = QPlainTextEdit(PremioDialog)
        self.txtDescripcion.setObjectName(u"txtDescripcion")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtDescripcion)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(PremioDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(PremioDialog)
        self.buttonBox.accepted.connect(PremioDialog.accept)
        self.buttonBox.rejected.connect(PremioDialog.reject)

        QMetaObject.connectSlotsByName(PremioDialog)
    # setupUi

    def retranslateUi(self, PremioDialog):
        PremioDialog.setWindowTitle(QCoreApplication.translate("PremioDialog", u"Detalle de Premio", None))
        self.labelNombre.setText(QCoreApplication.translate("PremioDialog", u"Nombre:", None))
        self.labelDesc.setText(QCoreApplication.translate("PremioDialog", u"Descripci\u00f3n:", None))
    # retranslateUi

