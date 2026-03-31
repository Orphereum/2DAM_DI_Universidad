from PySide6.QtWidgets import QWidget, QVBoxLayout
from app.view.GraficosAsignaturasPage_ui import Ui_GraficosAsignaturasPage

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class GraficosAsignaturasPage(QWidget):
    def __init__(self, asignatura_service, parent=None):
        super().__init__(parent)

        self.service = asignatura_service

        self.ui = Ui_GraficosAsignaturasPage()
        self.ui.setupUi(self)

        # Layout donde se dibuja el gráfico
        self.layout = QVBoxLayout(self.ui.widget_grafico)

        self._conectar_eventos()

    # -------------------------
    # EVENTOS
    # -------------------------
    def _conectar_eventos(self):
        self.ui.btn_curso.clicked.connect(self.grafico_por_curso)
        self.ui.btn_tipo.clicked.connect(self.grafico_por_tipo)

    # -------------------------
    # GRÁFICO POR CURSO
    # -------------------------
    def grafico_por_curso(self):
        asignaturas = self.service.obtener_asignaturas()

        cursos = [1, 2, 3, 4]
        conteo = [0, 0, 0, 0]

        for a in asignaturas:
            conteo[a.curso - 1] += 1

        self._dibujar_barra(cursos, conteo, "Asignaturas por curso")

    # -------------------------
    # GRÁFICO POR TIPO
    # -------------------------
    def grafico_por_tipo(self):
        asignaturas = self.service.obtener_asignaturas()

        obligatorias = sum(1 for a in asignaturas if a.obligatoria)
        optativas = sum(1 for a in asignaturas if not a.obligatoria)

        self._dibujar_pie(
            ["Obligatorias", "Optativas"],
            [obligatorias, optativas],
            "Tipo de asignaturas"
        )

    # -------------------------
    # DIBUJAR BARRAS
    # -------------------------
    def _dibujar_barra(self, x, y, titulo):
        self._limpiar()

        fig = Figure()
        canvas = FigureCanvas(fig)

        ax = fig.add_subplot(111)
        ax.bar(x, y)
        ax.set_title(titulo)

        self.layout.addWidget(canvas)

    # -------------------------
    # DIBUJAR PIE
    # -------------------------
    def _dibujar_pie(self, labels, values, titulo):
        self._limpiar()

        fig = Figure()
        canvas = FigureCanvas(fig)

        ax = fig.add_subplot(111)
        ax.pie(values, labels=labels, autopct="%1.1f%%")
        ax.set_title(titulo)

        self.layout.addWidget(canvas)

    # -------------------------
    # LIMPIAR GRÁFICO ANTERIOR
    # -------------------------
    def _limpiar(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()