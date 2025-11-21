# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        if not HomeWindow.objectName():
            HomeWindow.setObjectName(u"HomeWindow")
        HomeWindow.resize(1139, 732)
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setPointSize(24)
        font.setBold(True)
        HomeWindow.setFont(font)
        self.centralwidget = QWidget(HomeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(250, 70, 881, 621))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 70, 231, 621))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.menuWidget = QWidget()
        self.menuWidget.setObjectName(u"menuWidget")
        self.menuWidget.setGeometry(QRect(0, 0, 217, 1200))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.menuWidget.sizePolicy().hasHeightForWidth())
        self.menuWidget.setSizePolicy(sizePolicy)
        self.menuWidget.setMinimumSize(QSize(0, 700))
        self.verticalLayoutWidget = QWidget(self.menuWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 221, 1015))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblSectionGeneral = QLabel(self.verticalLayoutWidget)
        self.lblSectionGeneral.setObjectName(u"lblSectionGeneral")

        self.verticalLayout.addWidget(self.lblSectionGeneral)

        self.btnUniversidad = QPushButton(self.verticalLayoutWidget)
        self.btnUniversidad.setObjectName(u"btnUniversidad")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(22)
        font1.setBold(False)
        self.btnUniversidad.setFont(font1)
        self.btnUniversidad.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout.addWidget(self.btnUniversidad)

        self.btnFacultad = QPushButton(self.verticalLayoutWidget)
        self.btnFacultad.setObjectName(u"btnFacultad")
        self.btnFacultad.setFont(font1)

        self.verticalLayout.addWidget(self.btnFacultad)

        self.btnEdificio = QPushButton(self.verticalLayoutWidget)
        self.btnEdificio.setObjectName(u"btnEdificio")
        self.btnEdificio.setFont(font1)

        self.verticalLayout.addWidget(self.btnEdificio)

        self.btnGrado = QPushButton(self.verticalLayoutWidget)
        self.btnGrado.setObjectName(u"btnGrado")
        self.btnGrado.setFont(font1)

        self.verticalLayout.addWidget(self.btnGrado)

        self.btnDepartamento = QPushButton(self.verticalLayoutWidget)
        self.btnDepartamento.setObjectName(u"btnDepartamento")
        self.btnDepartamento.setFont(font1)

        self.verticalLayout.addWidget(self.btnDepartamento)

        self.lblSectionAcademico = QLabel(self.verticalLayoutWidget)
        self.lblSectionAcademico.setObjectName(u"lblSectionAcademico")

        self.verticalLayout.addWidget(self.lblSectionAcademico)

        self.btnAlumno = QPushButton(self.verticalLayoutWidget)
        self.btnAlumno.setObjectName(u"btnAlumno")
        self.btnAlumno.setFont(font1)

        self.verticalLayout.addWidget(self.btnAlumno)

        self.btnProfesor = QPushButton(self.verticalLayoutWidget)
        self.btnProfesor.setObjectName(u"btnProfesor")
        self.btnProfesor.setFont(font1)

        self.verticalLayout.addWidget(self.btnProfesor)

        self.btnAsignatura = QPushButton(self.verticalLayoutWidget)
        self.btnAsignatura.setObjectName(u"btnAsignatura")
        self.btnAsignatura.setFont(font1)

        self.verticalLayout.addWidget(self.btnAsignatura)

        self.btnClase = QPushButton(self.verticalLayoutWidget)
        self.btnClase.setObjectName(u"btnClase")
        self.btnClase.setFont(font1)

        self.verticalLayout.addWidget(self.btnClase)

        self.btnDebate = QPushButton(self.verticalLayoutWidget)
        self.btnDebate.setObjectName(u"btnDebate")
        self.btnDebate.setFont(font1)

        self.verticalLayout.addWidget(self.btnDebate)

        self.btnPremio = QPushButton(self.verticalLayoutWidget)
        self.btnPremio.setObjectName(u"btnPremio")
        self.btnPremio.setFont(font1)
        self.btnPremio.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout.addWidget(self.btnPremio)

        self.lblSectionInvestigacion = QLabel(self.verticalLayoutWidget)
        self.lblSectionInvestigacion.setObjectName(u"lblSectionInvestigacion")

        self.verticalLayout.addWidget(self.lblSectionInvestigacion)

        self.btnInvestigacion = QPushButton(self.verticalLayoutWidget)
        self.btnInvestigacion.setObjectName(u"btnInvestigacion")
        self.btnInvestigacion.setFont(font1)

        self.verticalLayout.addWidget(self.btnInvestigacion)

        self.btnProyecto = QPushButton(self.verticalLayoutWidget)
        self.btnProyecto.setObjectName(u"btnProyecto")
        self.btnProyecto.setFont(font1)

        self.verticalLayout.addWidget(self.btnProyecto)

        self.btnSubvencion = QPushButton(self.verticalLayoutWidget)
        self.btnSubvencion.setObjectName(u"btnSubvencion")
        font2 = QFont()
        font2.setFamilies([u"Dubai"])
        font2.setPointSize(22)
        font2.setBold(False)
        self.btnSubvencion.setFont(font2)

        self.verticalLayout.addWidget(self.btnSubvencion)

        self.btnPublicacion = QPushButton(self.verticalLayoutWidget)
        self.btnPublicacion.setObjectName(u"btnPublicacion")
        self.btnPublicacion.setFont(font1)

        self.verticalLayout.addWidget(self.btnPublicacion)

        self.scrollArea.setWidget(self.menuWidget)
        HomeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HomeWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1139, 33))
        HomeWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HomeWindow)
        self.statusbar.setObjectName(u"statusbar")
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)

        QMetaObject.connectSlotsByName(HomeWindow)
    # setupUi

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QCoreApplication.translate("HomeWindow", u"MainWindow", None))
        self.lblSectionGeneral.setText(QCoreApplication.translate("HomeWindow", u"General", None))
        self.btnUniversidad.setText(QCoreApplication.translate("HomeWindow", u"Universidad", None))
        self.btnFacultad.setText(QCoreApplication.translate("HomeWindow", u"Facultades", None))
        self.btnEdificio.setText(QCoreApplication.translate("HomeWindow", u"Edificios", None))
        self.btnGrado.setText(QCoreApplication.translate("HomeWindow", u"Grados", None))
        self.btnDepartamento.setText(QCoreApplication.translate("HomeWindow", u"Dptos.", None))
        self.lblSectionAcademico.setText(QCoreApplication.translate("HomeWindow", u"Ac\u00e1demico", None))
        self.btnAlumno.setText(QCoreApplication.translate("HomeWindow", u"Alumnos", None))
        self.btnProfesor.setText(QCoreApplication.translate("HomeWindow", u"Profesores", None))
        self.btnAsignatura.setText(QCoreApplication.translate("HomeWindow", u"Asignaturas", None))
        self.btnClase.setText(QCoreApplication.translate("HomeWindow", u"Clases", None))
        self.btnDebate.setText(QCoreApplication.translate("HomeWindow", u"Debates", None))
        self.btnPremio.setText(QCoreApplication.translate("HomeWindow", u"Premios", None))
        self.lblSectionInvestigacion.setText(QCoreApplication.translate("HomeWindow", u"Investigaci\u00f3n", None))
        self.btnInvestigacion.setText(QCoreApplication.translate("HomeWindow", u"Gr. Inv.", None))
        self.btnProyecto.setText(QCoreApplication.translate("HomeWindow", u"Proyectos", None))
        self.btnSubvencion.setText(QCoreApplication.translate("HomeWindow", u"Subvenciones", None))
        self.btnPublicacion.setText(QCoreApplication.translate("HomeWindow", u"Publicaciones", None))
    # retranslateUi

