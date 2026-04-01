from PySide6.QtWidgets import (
    QVBoxLayout, QMessageBox,
    QDialog, QFileDialog
)
from app.view.GraficosAsignaturasPage_ui import Ui_GraficosAsignaturasPage

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# 📄 REPORT
from app.reports.graficos_asignaturas_report import generar_pdf_graficos_pro

# 🎨 PALETA
COLORES = ["#7A1C2E", "#A8324A", "#D94F70", "#F28C8C"]


class GraficosAsignaturasPage(QDialog):

    def __init__(self, asignatura_service, parent=None):
        super().__init__(parent)

        # 🔒 MODAL
        self.setModal(True)

        # 🎨 CONFIG GLOBAL MATPLOTLIB
        plt.rcParams.update({
            "figure.facecolor": "#1E1E24",
            "axes.facecolor": "#24242C",
            "axes.edgecolor": "#FFFFFF",
            "axes.labelcolor": "#FFFFFF",
            "xtick.color": "#FFFFFF",
            "ytick.color": "#FFFFFF",
            "text.color": "#FFFFFF",
            "axes.titlecolor": "#FFFFFF",
            "grid.color": "#3A3A44",
            "legend.facecolor": "#2A2A33",
            "legend.edgecolor": "#3A3A44",
            "font.size": 9
        })

        self.service = asignatura_service

        self.ui = Ui_GraficosAsignaturasPage()
        self.ui.setupUi(self)

        # 🔙 BOTÓN VOLVER
        self.ui.btn_volver.clicked.connect(self.close)

        # 📊 Layouts
        self.layout_curso = QVBoxLayout(self.ui.grafico_curso)
        self.layout_tipo = QVBoxLayout(self.ui.grafico_tipo)
        self.layout_creditos = QVBoxLayout(self.ui.grafico_creditos)
        self.layout_cuatrimestre = QVBoxLayout(self.ui.grafico_cuatrimestre)

        self._cargar_filtros()
        self._conectar_eventos()
        self.actualizar_dashboard()

    # -------------------------
    # EVENTOS
    # -------------------------
    def _conectar_eventos(self):
        self.ui.cb_grado.currentIndexChanged.connect(self.actualizar_dashboard)
        self.ui.cb_curso.currentIndexChanged.connect(self.actualizar_dashboard)
        self.ui.cb_cuatrimestre.currentIndexChanged.connect(self.actualizar_dashboard)
        self.ui.cb_tipo.currentIndexChanged.connect(self.actualizar_dashboard)

        self.ui.btn_reset.clicked.connect(self.reset_filtros)
        self.ui.btn_exportar.clicked.connect(self.exportar_graficos)

    # -------------------------
    # FILTROS
    # -------------------------
    def _cargar_filtros(self):
        self.ui.cb_curso.addItems(["Todos", "1", "2", "3", "4"])
        self.ui.cb_cuatrimestre.addItems(["Todos", "1", "2"])
        self.ui.cb_tipo.addItems(["Todas", "Obligatorias", "Optativas"])

        grados = self.service.obtener_grados()
        for g in grados:
            self.ui.cb_grado.addItem(g.nombre, g.id_grado)

    def _get_filtros(self):
        curso = self.ui.cb_curso.currentText()
        cuatri = self.ui.cb_cuatrimestre.currentText()
        tipo_str = self.ui.cb_tipo.currentText()

        if tipo_str == "Obligatorias":
            tipo = 1
        elif tipo_str == "Optativas":
            tipo = 0
        else:
            tipo = None

        return curso, cuatri, tipo

    def obtener_filtradas(self):
        id_grado = self.ui.cb_grado.currentData()
        curso, cuatri, tipo = self._get_filtros()

        return self.service.obtener_asignaturas_filtradas(
            id_grado, curso, cuatri, tipo
        )

    # -------------------------
    # RESUMEN
    # -------------------------
    def _actualizar_resumen(self):
        texto = (
            f"{self.ui.cb_grado.currentText()} | "
            f"Curso: {self.ui.cb_curso.currentText()} | "
            f"Cuatrimestre: {self.ui.cb_cuatrimestre.currentText()} | "
            f"Tipo: {self.ui.cb_tipo.currentText()}"
        )
        self.ui.lbl_resumen.setText(texto)

    # -------------------------
    # DASHBOARD
    # -------------------------
    def actualizar_dashboard(self):
        asignaturas = self.obtener_filtradas()

        print("DEBUG TOTAL:", len(asignaturas))

        self._actualizar_resumen()

        self._grafico_curso(asignaturas)
        self._grafico_tipo(asignaturas)
        self._grafico_creditos(asignaturas)
        self._grafico_cuatrimestre(asignaturas)

    # -------------------------
    # GRÁFICOS
    # -------------------------
    def _grafico_curso(self, asignaturas):
        cursos = [1, 2, 3, 4]
        conteo = [0, 0, 0, 0]

        for a in asignaturas:
            if 1 <= a.curso <= 4:
                conteo[a.curso - 1] += 1

        self._dibujar_barra(self.layout_curso, cursos, conteo, "Asignaturas por curso")

    def _grafico_tipo(self, asignaturas):
        oblig = sum(1 for a in asignaturas if a.obligatoria)
        opt = sum(1 for a in asignaturas if not a.obligatoria)

        self._dibujar_pie(
            self.layout_tipo,
            ["Obligatorias", "Optativas"],
            [oblig, opt],
            "Tipo de asignaturas"
        )

    def _grafico_creditos(self, asignaturas):
        cursos = [1, 2, 3, 4]
        creditos = [0, 0, 0, 0]

        for a in asignaturas:
            if 1 <= a.curso <= 4:
                creditos[a.curso - 1] += a.creditos

        self._dibujar_barra(self.layout_creditos, cursos, creditos, "Créditos por curso")

    def _grafico_cuatrimestre(self, asignaturas):
        c1 = sum(1 for a in asignaturas if a.cuatrimestre == 1)
        c2 = sum(1 for a in asignaturas if a.cuatrimestre == 2)

        self._dibujar_pie(
            self.layout_cuatrimestre,
            ["1º Cuatrimestre", "2º Cuatrimestre"],
            [c1, c2],
            "Distribución por cuatrimestre"
        )

    # -------------------------
    # DIBUJAR BARRAS
    # -------------------------
    def _dibujar_barra(self, layout, x, y, titulo):
        self._limpiar(layout)

        fig = Figure(figsize=(6, 3.5), tight_layout=True)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        bars = ax.bar(x, y, color=COLORES, edgecolor="#FFFFFF", linewidth=0.5)

        ax.set_title(titulo, fontsize=11, weight="bold")
        ax.set_xlabel("Curso")
        ax.set_ylabel("Cantidad")

        ax.set_xticks(x)
        ax.set_xticklabels([f"{i}º" for i in x])

        ax.set_ylim(0, max(y) * 1.2 if max(y) > 0 else 1)

        ax.grid(axis='y', linestyle='--', alpha=0.2)

        for spine in ax.spines.values():
            spine.set_visible(False)

        for bar in bars:
            h = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width()/2,
                h,
                f"{h}",
                ha='center',
                va='bottom',
                fontsize=9,
                fontweight='bold'
            )

        layout.addWidget(canvas)

    # -------------------------
    # DIBUJAR PIE (SIN ERRORES)
    # -------------------------
    def _dibujar_pie(self, layout, labels, values, titulo):
        self._limpiar(layout)

        total = sum(values)

        if total == 0:
            values = [1]
            labels = ["Sin datos"]

        fig = Figure(figsize=(4, 3.5), tight_layout=True)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        wedges, _, _ = ax.pie(
            values,
            labels=labels,
            autopct=lambda p: f"{p:.1f}%" if total > 0 else "",
            colors=COLORES[:len(values)],
            startangle=90,
            wedgeprops={"edgecolor": "#1E1E24"},
            textprops={"color": "white", "fontsize": 9}
        )

        ax.set_title(titulo, fontsize=11, weight="bold")

        if total > 0:
            ax.legend(wedges, labels)

        layout.addWidget(canvas)

    # -------------------------
    # LIMPIAR
    # -------------------------
    def _limpiar(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    # -------------------------
    # RESET
    # -------------------------
    def reset_filtros(self):
        self.ui.cb_curso.setCurrentIndex(0)
        self.ui.cb_cuatrimestre.setCurrentIndex(0)
        self.ui.cb_tipo.setCurrentIndex(0)
        self.ui.cb_grado.setCurrentIndex(0)

    # -------------------------
    # EXPORTAR PDF PRO
    # -------------------------
    def exportar_graficos(self):
        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar PDF",
            "",
            "PDF (*.pdf)"
        )

        if not ruta:
            return

        asignaturas = self.obtener_filtradas()
        filtros = self.ui.lbl_resumen.text()

        generar_pdf_graficos_pro(asignaturas, ruta, filtros)

        QMessageBox.information(self, "Exportado", "Informe generado correctamente")