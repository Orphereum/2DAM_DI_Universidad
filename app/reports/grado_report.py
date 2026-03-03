# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from datetime import datetime
import os


class GradoReportGenerator:
    def __init__(self, grados_data, facultad_nombre, output_path="informe_grados.pdf"):
        """
        grados_data: Lista de objetos Grado desde tabla
        facultad_nombre: Nombre de facultad actual
        """
        self.grados = grados_data
        self.facultad = facultad_nombre
        self.doc = SimpleDocTemplate(output_path, pagesize=A4,
                                     rightMargin=2*cm, leftMargin=2*cm,
                                     topMargin=2*cm, bottomMargin=2*cm)
        self.story = []
        self.styles = getSampleStyleSheet()
        self._crear_estilos_personalizados()
        
    def _crear_estilos_personalizados(self):
        # Titulo principal
        self.titulo_principal = ParagraphStyle(
            'TituloPrincipal',
            parent=self.styles['Title'],
            fontSize=28,
            textColor=colors.HexColor('#1a5490'),
            spaceAfter=10,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        # Subtitulo
        self.subtitulo = ParagraphStyle(
            'Subtitulo',
            parent=self.styles['Normal'],
            fontSize=14,
            textColor=colors.HexColor('#555555'),
            alignment=TA_CENTER,
            spaceAfter=30
        )
        
        # Encabezado seccion
        self.encabezado_seccion = ParagraphStyle(
            'EncabezadoSeccion',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#1a5490'),
            spaceAfter=15,
            spaceBefore=20,
            fontName='Helvetica-Bold'
        )
        
    def generar_informe(self):
        self._portada()
        self._resumen_ejecutivo()
        self._tabla_grados_detallada()
        self._estadisticas()
        self._pie_pagina()
        self._build_pdf()
        print(f"Informe generado: {self.doc.filename}")
    
    def _portada(self):
        # Titulo
        self.story.append(Spacer(1, 1.5*inch))
        self.story.append(Paragraph("INFORME DE GRADOS", self.titulo_principal))
        self.story.append(Spacer(1, 0.3*inch))
        
        # Subtitulo facultad
        self.story.append(Paragraph(
            f"Facultad: <b>{self.facultad}</b>",
            self.subtitulo
        ))
        self.story.append(Spacer(1, 0.2*inch))
        
        # Fecha
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        self.story.append(Paragraph(
            f"Fecha: {fecha_actual}",
            self.subtitulo
        ))
        
        self.story.append(Spacer(1, 2*inch))
        
        # Linea decorativa
        linea = Table([['']], colWidths=[6*inch])
        linea.setStyle(TableStyle([
            ('LINEABOVE', (0, 0), (-1, 0), 3, colors.HexColor('#1a5490'))
        ]))
        self.story.append(linea)
        
    def _resumen_ejecutivo(self):
        self.story.append(Paragraph("RESUMEN EJECUTIVO", self.encabezado_seccion))
        
        total_grados = len(self.grados)
        total_creditos = sum(g.creditos_totales for g in self.grados)
        duracion_promedio = sum(g.duracion_anios for g in self.grados) / total_grados if total_grados > 0 else 0
        
        resumen_data = [
            ['Metrica', 'Valor'],
            ['Total de Grados', str(total_grados)],
            ['Creditos Totales', str(total_creditos)],
            ['Duracion Promedio', f"{duracion_promedio:.1f} años"],
            ['Facultad', self.facultad]
        ]
        
        tabla_resumen = Table(resumen_data, colWidths=[3*inch, 2.5*inch])
        tabla_resumen.setStyle(TableStyle([
            # Encabezado
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a5490')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            # Contenido
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f0f5fa')),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (0, -1), 'LEFT'),
            ('ALIGN', (1, 1), (1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 11),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cccccc')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#f0f5fa'), colors.white])
        ]))
        
        self.story.append(tabla_resumen)
        self.story.append(Spacer(1, 0.5*inch))
    
    def _tabla_grados_detallada(self):
        self.story.append(Paragraph("LISTADO COMPLETO DE GRADOS", self.encabezado_seccion))
        
        # Headers
        data = [['N°', 'Nombre', 'Codigo', 'Duracion', 'Creditos', 'Tipo']]
        
        # Datos de tabla
        for idx, grado in enumerate(self.grados, 1):
            data.append([
                str(idx),
                grado.nombre,
                grado.codigo,
                f"{grado.duracion_anios} años",
                str(grado.creditos_totales),
                grado.tipo if grado.tipo else 'N/A'
            ])
        
        tabla = Table(data, colWidths=[0.5*inch, 2*inch, 1*inch, 1*inch, 1*inch, 1*inch])
        tabla.setStyle(TableStyle([
            # Encabezado
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5f8d')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            # Contenido
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('ALIGN', (0, 1), (0, -1), 'CENTER'),  # Numero
            ('ALIGN', (2, 1), (-1, -1), 'CENTER'),  # Codigo, duracion, creditos
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')])
        ]))
        
        self.story.append(tabla)
        self.story.append(Spacer(1, 0.5*inch))
    
    def _estadisticas(self):
        self.story.append(Paragraph("ESTADISTICAS POR TIPO", self.encabezado_seccion))
        
        # Agrupar por tipo
        tipos = {}
        for grado in self.grados:
            tipo = grado.tipo if grado.tipo else 'Sin especificar'
            if tipo not in tipos:
                tipos[tipo] = {'count': 0, 'creditos': 0}
            tipos[tipo]['count'] += 1
            tipos[tipo]['creditos'] += grado.creditos_totales
        
        data_tipos = [['Tipo', 'Cantidad', 'Creditos Totales']]
        for tipo, stats in tipos.items():
            data_tipos.append([
                tipo,
                str(stats['count']),
                str(stats['creditos'])
            ])
        
        tabla_stats = Table(data_tipos, colWidths=[2.5*inch, 1.5*inch, 1.5*inch])
        tabla_stats.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#28a745')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#e8f5e9'), colors.white])
        ]))
        
        self.story.append(tabla_stats)
    
    def _pie_pagina(self):
        self.story.append(Spacer(1, 1*inch))
        
        pie = ParagraphStyle(
            'Pie',
            parent=self.styles['Normal'],
            fontSize=9,
            textColor=colors.grey,
            alignment=TA_CENTER
        )
        
        self.story.append(Paragraph(
            "Generado automaticamente por Sistema Gestor Universidad",
            pie
        ))
        self.story.append(Paragraph(
            f"2DAM DI - {datetime.now().year}",
            pie
        ))
    
    def _build_pdf(self):
        self.doc.build(self.story)


# Funcion auxiliar para llamar desde GradoPage
def generar_informe_grados(grados, facultad_nombre):
    os.makedirs("reports", exist_ok=True)

    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"reports/informe_{facultad_nombre}_{fecha}.pdf"
    nombre_archivo = nombre_archivo.replace(" ", "_")

    report = GradoReportGenerator(grados, facultad_nombre, nombre_archivo)
    report.generar_informe()
    return nombre_archivo
