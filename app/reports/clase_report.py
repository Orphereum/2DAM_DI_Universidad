import os
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart, HorizontalBarChart
from reportlab.graphics.charts.legends import Legend


class ClaseReportGenerator:
    """Genera un informe PDF de Clases con estilo profesional y gráficos."""

    @staticmethod
    def encabezado_y_pie(canvas, doc):
        """Agrega encabezado y pie personalizados en cada página"""
        canvas.saveState()
        ancho, alto = A4
        
        # Línea superior azul
        canvas.setStrokeColor(colors.HexColor("#1F5BA8"))
        canvas.setLineWidth(2)
        canvas.line(1.5*cm, alto - 2.8*cm, ancho - 1.5*cm, alto - 2.8*cm)

        # Título encabezado
        canvas.setFont('Helvetica-Bold', 14)
        canvas.setFillColor(colors.HexColor("#1F5BA8"))
        canvas.drawString(1.5*cm, alto - 1.5*cm, "GESTOR UNIVERSIDAD - CLASES")
        
        # Fecha
        canvas.setFont('Helvetica', 10)
        canvas.setFillColor(colors.black)
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        canvas.drawRightString(ancho - 1.5*cm, alto - 1.5*cm, f"Fecha: {fecha}")

        # Línea inferior pie
        canvas.setStrokeColor(colors.HexColor("#1F5BA8"))
        canvas.setLineWidth(1)
        canvas.line(1.5*cm, 2*cm, ancho - 1.5*cm, 2*cm)
        
        # Texto pie
        canvas.setFont('Helvetica', 8)
        canvas.drawString(1.5*cm, 1.5*cm, "Informe generado por Sistema de Gestión Universitaria")
        canvas.drawRightString(ancho - 1.5*cm, 1.5*cm, f"Página {doc.page}")
        
        canvas.restoreState()

    def __init__(self, clases_data, edificios_data=None, output_path="informe_clases.pdf"):
        self.clases = clases_data
        self.edificios_list = edificios_data if edificios_data else []
        self.edificios_dict = {ed.id: ed.nombre for ed in self.edificios_list}
        self.doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=1.5 * cm,
            leftMargin=1.5 * cm,
            topMargin=3 * cm,
            bottomMargin=2.5 * cm,
        )
        self.story = []
        self.styles = getSampleStyleSheet()
        self._crear_estilos()

    def _crear_estilos(self):
        self.estilo_titulo = ParagraphStyle(
            "TituloPrincipal",
            parent=self.styles["Title"],
            fontSize=20,
            textColor=colors.HexColor("#1F5BA8"),
            spaceAfter=10,
            alignment=TA_CENTER,
            fontName="Helvetica-Bold",
        )
        self.estilo_subtitulo = ParagraphStyle(
            "Subtitulo",
            parent=self.styles["Normal"],
            fontSize=11,
            textColor=colors.HexColor("#666666"),
            alignment=TA_CENTER,
            spaceAfter=20,
        )
        self.estilo_seccion = ParagraphStyle(
            "EncabezadoSeccion",
            parent=self.styles["Heading2"],
            fontSize=13,
            textColor=colors.HexColor("#1F5BA8"),
            spaceAfter=12,
            spaceBefore=15,
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
        self._grafico_capacidades()
        self._grafico_edificios()
        self._tabla_clases()
        self.doc.build(self.story, onFirstPage=self.encabezado_y_pie, onLaterPages=self.encabezado_y_pie)

    def _portada(self):
        self.story.append(Spacer(1, 1.5 * cm))
        self.story.append(Paragraph("INFORME DE CLASES", self.estilo_titulo))
        self.story.append(Spacer(1, 0.3 * cm))
        self.story.append(
            Paragraph("Sistema de Gestión Universitaria", self.estilo_subtitulo)
        )
        self.story.append(
            Paragraph(
                f"Generado: {datetime.now().strftime('%d/%m/%Y a las %H:%M')}",
                self.estilo_subtitulo,
            )
        )
        self.story.append(Spacer(1, 2 * cm))

        linea = Table([[""]], colWidths=[6 * cm])
        linea.setStyle(
            TableStyle(
                [("LINEABOVE", (0, 0), (-1, 0), 3, colors.HexColor("#1F5BA8"))]
            )
        )
        self.story.append(linea)

    def _resumen(self):
        self.story.append(Paragraph("RESUMEN ESTADÍSTICO", self.estilo_seccion))
        total = len(self.clases)
        capacidad_total = sum(clase.capacidad for clase in self.clases)
        capacidad_promedio = capacidad_total / total if total > 0 else 0
        
        data_resumen = [
            ["MÉTRICA", "VALOR"],
            ["Total de Clases", str(total)],
            ["Capacidad Total", str(capacidad_total) + " estudiantes"],
            ["Capacidad Promedio", f"{capacidad_promedio:.1f} estudiantes"],
        ]
        
        tabla_resumen = Table(data_resumen, colWidths=[8*cm, 8*cm], rowHeights=0.7*cm)
        tabla_resumen.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1F5BA8")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#E8F0F7"), colors.white])
        ]))
        
        self.story.append(tabla_resumen)
        self.story.append(Spacer(1, 0.5 * cm))

    def _grafico_capacidades(self):
        """Gráfico de barras verticales con capacidad de cada clase"""
        self.story.append(Paragraph("Capacidad por Clase", self.estilo_seccion))
        self.story.append(Spacer(1, 0.2*cm))
        
        if len(self.clases) > 0:
            grafico = self._crear_grafico_capacidades()
            self.story.append(grafico)
        else:
            self.story.append(Paragraph("No hay datos disponibles", self.styles["Normal"]))
        
        self.story.append(Spacer(1, 0.5*cm))

    def _crear_grafico_capacidades(self):
        """Crea gráfico de barras verticales"""
        d = Drawing(500, 250)
        
        nombres = [clase.nombre for clase in self.clases]
        capacidades = [clase.capacidad for clase in self.clases]
        
        bc = VerticalBarChart()
        bc.x = 80
        bc.y = 40
        bc.height = 180
        bc.width = 350
        bc.data = [capacidades]
        
        bc.valueAxis.valueMin = 0
        bc.categoryAxis.categoryNames = nombres
        bc.categoryAxis.labels.fontName = 'Helvetica'
        bc.categoryAxis.labels.fontSize = 8
        
        bc.bars[0].fillColor = colors.HexColor("#1F5BA8")
        bc.barLabelFormat = '%d'
        bc.barLabels.nudge = 5
        
        d.add(bc)
        return d

    def _grafico_edificios(self):
        """Gráfico de distribución de clases por edificio"""
        self.story.append(Paragraph("Distribución de Clases por Edificio", self.estilo_seccion))
        self.story.append(Spacer(1, 0.2*cm))
        
        # Contar clases por edificio
        edificios_count = {}
        for clase in self.clases:
            nombre_ed = self.edificios_dict.get(clase.id_edificio, "Desconocido")
            edificios_count[nombre_ed] = edificios_count.get(nombre_ed, 0) + 1
        
        if edificios_count:
            grafico = self._crear_grafico_edificios(edificios_count)
            self.story.append(grafico)
        else:
            self.story.append(Paragraph("No hay datos disponibles", self.styles["Normal"]))
        
        self.story.append(Spacer(1, 0.5*cm))

    def _crear_grafico_edificios(self, edificios_count):
        """Crea gráfico de barras horizontales"""
        d = Drawing(500, max(150, len(edificios_count) * 30))
        
        nombres = list(edificios_count.keys())
        valores = list(edificios_count.values())
        
        bc = HorizontalBarChart()
        bc.x = 100
        bc.y = 20
        bc.height = max(120, len(nombres) * 25)
        bc.width = 300
        bc.data = [valores]
        
        bc.valueAxis.valueMin = 0
        bc.categoryAxis.categoryNames = nombres
        bc.categoryAxis.labels.fontName = 'Helvetica'
        bc.categoryAxis.labels.fontSize = 9
        
        bc.bars[0].fillColor = colors.HexColor("#4A90E2")
        bc.barLabelFormat = '%d'
        bc.barLabels.nudge = 5
        
        d.add(bc)
        return d

    def _tabla_clases(self):
        """Tabla detallada de todas las clases"""
        self.story.append(Paragraph("LISTADO DETALLADO DE CLASES", self.estilo_seccion))

        encabezados = ["ID", "Nombre", "Capacidad", "Edificio"]
        datos = [encabezados]

        for clase in self.clases:
            nombre_edificio = self.edificios_dict.get(clase.id_edificio, "N/A")
            datos.append([
                str(clase.id_clase),
                clase.nombre,
                str(clase.capacidad),
                nombre_edificio,
            ])

        col_widths = [1.5 * cm, 5 * cm, 3 * cm, 6 * cm]
        tabla = Table(datos, colWidths=col_widths, repeatRows=1)
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F5BA8")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 10),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            ("TOPPADDING", (0, 0), (-1, 0), 8),
            ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F5F5F5")),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#EFEFEF")]),
            ("FONTSIZE", (0, 1), (-1, -1), 9),
            ("ALIGN", (0, 1), (0, -1), "CENTER"),
            ("ALIGN", (2, 1), (2, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
            ("TOPPADDING", (0, 1), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
        ]))
        self.story.append(tabla)
