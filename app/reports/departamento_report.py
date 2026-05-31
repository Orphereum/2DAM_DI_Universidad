from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from datetime import datetime
import os


class DepartamentoReportGenerator:
    def __init__(
        self, departamentos_data, facultades_dict, output_path="informe_departamentos.pdf"
    ):
        self.departamentos = departamentos_data
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
        self._resumen_ejecutivo()
        self._tabla_detallada()
        self._estadisticas_por_facultad()
        self._pie_pagina()
        self.doc.build(self.story)
        print(f"Informe generado: {self.doc.filename}")

    def _portada(self):
        self.story.append(Spacer(1, 1.5 * inch))
        self.story.append(Paragraph("INFORME DE DEPARTAMENTOS", self.estilo_titulo))
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

        linea = Table([[""]], colWidths=[6.7 * inch])
        linea.setStyle(
            TableStyle([("LINEABOVE", (0, 0), (-1, 0), 3, colors.HexColor("#7A1C2E"))])
        )
        self.story.append(linea)

    def _resumen_ejecutivo(self):
        self.story.append(Paragraph("RESUMEN EJECUTIVO", self.estilo_seccion))

        total = len(self.departamentos)
        facultades_con_departamentos = len(
            set(d.id_facultad for d in self.departamentos)
        )
        promedio = (
            round(total / facultades_con_departamentos, 1)
            if facultades_con_departamentos
            else 0
        )

        data = [
            ["Métrica", "Valor"],
            ["Total de departamentos", str(total)],
            ["Facultades con departamentos", str(facultades_con_departamentos)],
            ["Media departamentos / facultad", str(promedio)],
        ]

        tabla = Table(data, colWidths=[3.5 * inch, 3.2 * inch])
        tabla.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7A1C2E")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, 0), 12),
                    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
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
            Paragraph("LISTADO COMPLETO DE DEPARTAMENTOS", self.estilo_seccion)
        )

        data = [["N°", "ID", "Nombre del Departamento", "Facultad"]]
        for idx, depto in enumerate(self.departamentos, 1):
            nombre_facultad = self.facultades_dict.get(
                depto.id_facultad, depto.facultad or "Desconocida"
            )
            data.append(
                [
                    str(idx),
                    str(depto.id_departamento),
                    depto.nombre,
                    nombre_facultad,
                ]
            )

        tabla = Table(
            data, colWidths=[0.6 * inch, 1.2 * inch, 2.7 * inch, 2.2 * inch]
        )
        tabla.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7A1C2E")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, 0), 11),
                    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                    ("FONTSIZE", (0, 1), (-1, -1), 10),
                    ("ALIGN", (0, 1), (1, -1), "CENTER"),
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

        conteo = {}
        for depto in self.departamentos:
            nombre_facultad = self.facultades_dict.get(
                depto.id_facultad, depto.facultad or "Desconocida"
            )
            conteo[nombre_facultad] = conteo.get(nombre_facultad, 0) + 1

        data = [["Facultad", "Nº Departamentos"]]
        for nombre_facultad, cantidad in sorted(conteo.items()):
            data.append([nombre_facultad, str(cantidad)])

        tabla = Table(data, colWidths=[4.2 * inch, 2.5 * inch])
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


def generar_informe_departamentos(departamentos, facultades_dict, output_path):
    report = DepartamentoReportGenerator(departamentos, facultades_dict, output_path)
    report.generar_informe()
    return output_path