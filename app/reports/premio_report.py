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


class PremioReportGenerator:
    """Genera un informe PDF de Premios a la Excelencia."""

    def __init__(self, premios_data, output_path="informe_premios.pdf"):
        self.premios = premios_data
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

    def generar_informe(self):
        self._portada()
        self._resumen()
        self._tabla_premios()
        self._pie_pagina()
        self.doc.build(self.story)

    def _portada(self):
        self.story.append(Spacer(1, 1.5 * inch))
        self.story.append(Paragraph("INFORME DE PREMIOS A LA EXCELENCIA", self.estilo_titulo))
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

        linea = Table([[""]], colWidths=[6 * inch])
        linea.setStyle(
            TableStyle(
                [("LINEABOVE", (0, 0), (-1, 0), 3, colors.HexColor("#7A1C2E"))]
            )
        )
        self.story.append(linea)

    def _resumen(self):
        self.story.append(Paragraph("RESUMEN", self.estilo_seccion))
        total = len(self.premios)
        texto = f"Total de premios registrados: <b>{total}</b>"
        self.story.append(Paragraph(texto, self.styles["Normal"]))
        self.story.append(Spacer(1, 0.3 * inch))

    def _tabla_premios(self):
        self.story.append(Paragraph("LISTADO DE PREMIOS", self.estilo_seccion))

        encabezados = ["ID", "Nombre del Premio", "Descripción"]
        datos = [encabezados]

        for premio in self.premios:
            datos.append([
                str(premio.id_premio),
                premio.nombre_premio,
                premio.descripcion_premio or "Sin descripción",
            ])

        col_widths = [1 * cm, 6 * cm, 10 * cm]
        tabla = Table(datos, colWidths=col_widths, repeatRows=1)
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7A1C2E")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 11),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
            ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F9F9F9")),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F2F2F2")]),
            ("FONTSIZE", (0, 1), (-1, -1), 9),
            ("ALIGN", (0, 1), (0, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
            ("TOPPADDING", (0, 1), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
        ]))
        self.story.append(tabla)
        self.story.append(Spacer(1, 0.5 * inch))

    def _pie_pagina(self):
        self.story.append(Spacer(1, 0.5 * inch))
        linea = Table([[""]], colWidths=[6 * inch])
        linea.setStyle(
            TableStyle(
                [("LINEABOVE", (0, 0), (-1, 0), 1, colors.HexColor("#7A1C2E"))]
            )
        )
        self.story.append(linea)
        self.story.append(Spacer(1, 0.2 * inch))
        self.story.append(
            Paragraph(
                f"Generado el {datetime.now().strftime('%d/%m/%Y a las %H:%M')} — Sistema de Gestión Universitaria",
                self.estilo_pie,
            )
        )
