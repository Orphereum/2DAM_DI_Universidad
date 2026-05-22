from PySide6.QtCore import QCoreApplication, QDate, QMetaObject, Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QDateEdit,
    QFormLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)


class Ui_Publicacion_page(object):
    def setupUi(self, Publicacion_page):
        if not Publicacion_page.objectName():
            Publicacion_page.setObjectName("Publicacion_page")

        Publicacion_page.resize(900, 600)
        self.verticalLayout = QVBoxLayout(Publicacion_page)
        self.verticalLayout.setObjectName("verticalLayout")

        self.labelTitulo = QLabel(Publicacion_page)
        self.labelTitulo.setObjectName("labelTitulo")
        font = self.labelTitulo.font()
        font.setPointSize(24)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.labelTitulo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.labelTituloPublicacion = QLabel(Publicacion_page)
        self.inputTitulo = QLineEdit(Publicacion_page)
        self.formLayout.addRow(self.labelTituloPublicacion, self.inputTitulo)

        self.labelDescripcion = QLabel(Publicacion_page)
        self.inputDescripcion = QPlainTextEdit(Publicacion_page)
        self.inputDescripcion.setMaximumHeight(90)
        self.formLayout.addRow(self.labelDescripcion, self.inputDescripcion)

        self.labelFecha = QLabel(Publicacion_page)
        self.inputFecha = QDateEdit(Publicacion_page)
        self.inputFecha.setCalendarPopup(True)
        self.inputFecha.setDisplayFormat("yyyy-MM-dd")
        self.inputFecha.setDate(QDate.currentDate())
        self.formLayout.addRow(self.labelFecha, self.inputFecha)

        self.labelTipo = QLabel(Publicacion_page)
        self.inputTipo = QLineEdit(Publicacion_page)
        self.formLayout.addRow(self.labelTipo, self.inputTipo)

        self.labelGrupoDebate = QLabel(Publicacion_page)
        self.comboGrupoDebate = QComboBox(Publicacion_page)
        self.formLayout.addRow(self.labelGrupoDebate, self.comboGrupoDebate)

        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayoutBotones = QHBoxLayout()
        self.horizontalLayoutBotones.setObjectName("horizontalLayoutBotones")

        self.btn_guardar = QPushButton(Publicacion_page)
        self.btn_editar = QPushButton(Publicacion_page)
        self.btn_eliminar = QPushButton(Publicacion_page)
        self.btn_limpiar = QPushButton(Publicacion_page)

        self.horizontalLayoutBotones.addWidget(self.btn_guardar)
        self.horizontalLayoutBotones.addWidget(self.btn_editar)
        self.horizontalLayoutBotones.addWidget(self.btn_eliminar)
        self.horizontalLayoutBotones.addWidget(self.btn_limpiar)
        self.verticalLayout.addLayout(self.horizontalLayoutBotones)

        self.tabla_publicaciones = QTableWidget(Publicacion_page)
        self.tabla_publicaciones.setObjectName("tabla_publicaciones")
        self.tabla_publicaciones.setColumnCount(7)
        self.tabla_publicaciones.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.tabla_publicaciones.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tabla_publicaciones.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.tabla_publicaciones.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.tabla_publicaciones.setColumnHidden(5, True)

        for column in range(7):
            item = QTableWidgetItem()
            self.tabla_publicaciones.setHorizontalHeaderItem(column, item)

        self.verticalLayout.addWidget(self.tabla_publicaciones)

        self.retranslateUi(Publicacion_page)
        QMetaObject.connectSlotsByName(Publicacion_page)

    def retranslateUi(self, Publicacion_page):
        Publicacion_page.setWindowTitle(
            QCoreApplication.translate("Publicacion_page", "Publicaciones")
        )
        self.labelTitulo.setText(
            QCoreApplication.translate("Publicacion_page", "Publicaciones")
        )
        self.labelTituloPublicacion.setText(
            QCoreApplication.translate("Publicacion_page", "Titulo:")
        )
        self.labelDescripcion.setText(
            QCoreApplication.translate("Publicacion_page", "Descripcion:")
        )
        self.labelFecha.setText(
            QCoreApplication.translate(
                "Publicacion_page",
                "Fecha publicacion:"
            )
        )
        self.labelTipo.setText(
            QCoreApplication.translate("Publicacion_page", "Tipo:")
        )
        self.labelGrupoDebate.setText(
            QCoreApplication.translate("Publicacion_page", "Grupo debate:")
        )
        self.btn_guardar.setText(
            QCoreApplication.translate("Publicacion_page", "Guardar")
        )
        self.btn_editar.setText(
            QCoreApplication.translate("Publicacion_page", "Editar")
        )
        self.btn_eliminar.setText(
            QCoreApplication.translate("Publicacion_page", "Eliminar")
        )
        self.btn_limpiar.setText(
            QCoreApplication.translate("Publicacion_page", "Limpiar")
        )

        headers = [
            "ID",
            "Titulo",
            "Descripcion",
            "Fecha",
            "Tipo",
            "ID grupo",
            "Grupo debate",
        ]
        for column, text in enumerate(headers):
            self.tabla_publicaciones.horizontalHeaderItem(column).setText(
                QCoreApplication.translate("Publicacion_page", text)
            )
