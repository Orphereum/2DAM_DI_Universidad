from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer,
    Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from datetime import datetime
import os


class EdificioReportGenerator:
    """
    Genera un informe PDF de edificios agrupados por facultad.
    Modelado sobre GradoReportGenerator (grado_report.py).
    """

    def __init__(self, edificios_data, facultades_dict, output_path="informe_edificios.pdf"):
        """
        edificios_data  : lista de objetos Edificio
        facultades_dict : {id_facultad: nombre_facultad}
        """
        self.edificios = edificios_data
        self.facultades_dict = facultades_dict

        self.doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=2 * cm,
            leftMargin=2 * cm,
            topMargin=2 * cm,
            bottomMargin=2 * cm,
        )
        self.story = []
        self.styles = getSampleStyleSheet()
        self._crear_estilos()

    # -------------------------
    # ESTILOS
    # -------------------------
    def _crear_estilos(self):
        self.estilo_titulo = ParagraphStyle(
            "TituloPrincipal",
            parent=self.styles["Title"],
            fontSize=28,
            textColor=colors.HexColor("#7A1C2E"),
            spaceAfter=10,
            alignment=TA_CENTER,
            fontName="Helvetica-Bold",
        )
        self.estilo_subtitulo = ParagraphStyle(
            "Subtitulo",
            parent=self.styles["Normal"],
            fontSize=14,
            textColor=colors.HexColor("#555555"),
            alignment=TA_CENTER,
            spaceAfter=20,
        )
        self.estilo_seccion = ParagraphStyle(
            "EncabezadoSeccion",
            parent=self.styles["Heading2"],
            fontSize=16,
            textColor=colors.HexColor("#7A1C2E"),
            spaceAfter=15,
            spaceBefore=20,
            fontName="Helvetica-Bold",
        )
        self.estilo_pie = ParagraphStyle(
            "Pie",
            parent=self.styles["Normal"],
            fontSize=9,
            textColor=colors.grey,
            alignment=TA_CENTER,
        )

    # -------------------------
    # ENTRADA PÚBLICA
    # -------------------------
    def generar_informe(self):
        self._portada()
        self._resumen_ejecutivo()
        self._tabla_detallada()
        self._estadisticas_por_facultad()
        self._pie_pagina()
        self.doc.build(self.story)
        print(f"Informe generado: {self.doc.filename}")

    # -------------------------
    # SECCIONES
    # -------------------------
    def _portada(self):
        self.story.append(Spacer(1, 1.5 * inch))
        self.story.append(Paragraph("INFORME DE EDIFICIOS", self.estilo_titulo))
        self.story.append(Spacer(1, 0.3 * inch))
        self.story.append(
            Paragraph("Sistema de Gestión Universitaria", self.estilo_subtitulo)
        )
        self.story.append(
            Paragraph(
                f"Fecha: {datetime.now().strftime('%d/%m/%Y')}",
                self.estilo_subtitulo,
            )
        )
        self.story.append(Spacer(1, 2 * inch))

        # Línea decorativa (igual que grado_report)
        linea = Table([[""]], colWidths=[6 * inch])
        linea.setStyle(
            TableStyle(
                [("LINEABOVE", (0, 0), (-1, 0), 3, colors.HexColor("#7A1C2E"))]
            )
        )
        self.story.append(linea)

    def _resumen_ejecutivo(self):
        self.story.append(Paragraph("RESUMEN EJECUTIVO", self.estilo_seccion))

        total = len(self.edificios)
        facultades_con_edificios = len(set(e.id_facultad for e in self.edificios))
        promedio = round(total / facultades_con_edificios, 1) if facultades_con_edificios else 0

        data = [
            ["Métrica", "Valor"],
            ["Total de edificios", str(total)],
            ["Facultades con edificios", str(facultades_con_edificios)],
            ["Media edificios / facultad", str(promedio)],
        ]

        tabla = Table(data, colWidths=[3 * inch, 2.5 * inch])
        tabla.setStyle(
            TableStyle(
                [
                    # Cabecera
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7A1C2E")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, 0), 12),
                    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
                    # Contenido
                    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                    ("FONTSIZE", (0, 1), (-1, -1), 11),
                    ("ALIGN", (1, 1), (1, -1), "CENTER"),
                    ("GRID", (0, 0), (-1, -1), 1, colors.HexColor("#cccccc")),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    (
                        "ROWBACKGROUNDS",
                        (0, 1),
                        (-1, -1),
                        [colors.HexColor("#f5f0f1"), colors.white],
                    ),
                ]
            )
        )
        self.story.append(tabla)
        self.story.append(Spacer(1, 0.5 * inch))

    def _tabla_detallada(self):
        self.story.append(
            Paragraph("LISTADO COMPLETO DE EDIFICIOS", self.estilo_seccion)
        )

        data = [["N°", "Nombre del Edificio", "Facultad"]]
        for idx, edificio in enumerate(self.edificios, 1):
            nombre_fac = self.facultades_dict.get(edificio.id_facultad, "Desconocida")
            data.append([str(idx), edificio.nombre, nombre_fac])

        tabla = Table(data, colWidths=[0.5 * inch, 2.5 * inch, 3 * inch])
        tabla.setStyle(
            TableStyle(
                [
                    # Cabecera
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7A1C2E")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, 0), 11),
                    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                    # Contenido
                    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                    ("FONTSIZE", (0, 1), (-1, -1), 10),
                    ("ALIGN", (0, 1), (0, -1), "CENTER"),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    (
                        "ROWBACKGROUNDS",
                        (0, 1),
                        (-1, -1),
                        [colors.white, colors.HexColor("#f5f0f1")],
                    ),
                ]
            )
        )
        self.story.append(tabla)
        self.story.append(Spacer(1, 0.5 * inch))

    def _estadisticas_por_facultad(self):
        self.story.append(
            Paragraph("ESTADÍSTICAS POR FACULTAD", self.estilo_seccion)
        )

        # Agrupar conteo por facultad
        conteo: dict[str, int] = {}
        for edificio in self.edificios:
            nombre_fac = self.facultades_dict.get(edificio.id_facultad, "Desconocida")
            conteo[nombre_fac] = conteo.get(nombre_fac, 0) + 1

        data = [["Facultad", "Nº Edificios"]]
        for nombre_fac, cantidad in sorted(conteo.items()):
            data.append([nombre_fac, str(cantidad)])

        tabla = Table(data, colWidths=[4 * inch, 1.5 * inch])
        tabla.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#A8324A")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    (
                        "ROWBACKGROUNDS",
                        (0, 1),
                        (-1, -1),
                        [colors.HexColor("#f5f0f1"), colors.white],
                    ),
                ]
            )
        )
        self.story.append(tabla)

    def _pie_pagina(self):
        self.story.append(Spacer(1, 1 * inch))
        self.story.append(
            Paragraph(
                "Generado automáticamente por Sistema Gestor Universidad",
                self.estilo_pie,
            )
        )
        self.story.append(
            Paragraph(f"2DAM DI - {datetime.now().year}", self.estilo_pie)
        )


# -------------------------
# FUNCIÓN AUXILIAR (igual que en grado_report)
# -------------------------
def generar_informe_edificios(edificios, facultades_dict):
    """
    Crea la carpeta reports/ si no existe, genera el PDF y devuelve la ruta.
    Uso:
        pdf_path = generar_informe_edificios(edificios, facultades_dict)
    """
    os.makedirs("reports", exist_ok=True)
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"reports/informe_edificios_{fecha}.pdf"

    report = EdificioReportGenerator(edificios, facultades_dict, nombre_archivo)
    report.generar_informe()
    return nombre_archivo