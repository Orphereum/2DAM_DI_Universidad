from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from datetime import datetime
import os

class GeneradorInformeProyectos_Grupos:

    def __init__(self, grupos):
        self.grupos = grupos
        # INICIALIZACION
        self.NOMBRE = "INFORME DE GRUPOS Y PROYECTOS"
        self.AUTOR = "Alejandro Prada Sánchez"
        self.FECHA = datetime.now().strftime("%d/%m/%y")
        self.UNIVERSIDAD = "Universidad Castilla-LaMancha UCLM"
        

    def generar(self, ruta_pdf):

        doc = SimpleDocTemplate(
            ruta_pdf,
            pagesizes=A4,
            topMargin=5*cm,
            bottomMargin=5*cm,
            leftMargin=2*cm,
            rightMargin=2*cm
        )
        elements = []
        estilo = getSampleStyleSheet()
        
        estilo_cursiva_y_centrado = ParagraphStyle(
            "CursivaYCentrado",
            parent=estilo["Italic"],
            alignment=TA_CENTER
        )
        
        elements.append(Paragraph("Informe generado para mostrar los proyectos y subvenciones por grupo", estilo_cursiva_y_centrado))
        elements.append(Spacer(1, 12))
        
        # Recorrer cada grupo
        for grupo in self.grupos:
            nombre_grupo = grupo['nombre']
            proyectos = grupo['proyectos']
            num_proyectos = len(proyectos)
            
            # Nombre del grupo
            elements.append(Paragraph(f"Grupo: {nombre_grupo}", estilo["Heading2"]))
            elements.append(Spacer(1, 0.2 * cm))
            
            # Número de proyectos
            elements.append(Paragraph(f"Nº proyectos: {num_proyectos}", estilo["Normal"]))
            elements.append(Spacer(1, 0.3 * cm))
            
            # Crear tabla de proyectos con conteo de subvenciones
            data = [["Nombre del proyecto", "Nº de subvenciones"]]
            
            for proyecto in proyectos:
                nombre_proyecto = proyecto['nombre']
                num_subvenciones = len(proyecto.get('subvenciones', []))
                data.append([nombre_proyecto, str(num_subvenciones)])
            
            # Crear la tabla
            tabla = Table(data)
            tabla.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, -1), 0.45, colors.black),
                #("BACKGROUND", (0, 0), (-1, -1), "#D1858E"), filas alternas abajo
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("FONTNAME", (0, 0), (-1, -1), "Courier"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("ALIGN", (1, 0), (1, -1), "CENTER"),
                # Cabecera
                ("BACKGROUND", (0, 0), (-1, 0), "#850815"),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 12),
                # Columna nombre del proyecto
                ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
                # Filas alternas (opcional)
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), ["#D1858E", "#DD9CA3"]),
            ]))
            
            elements.append(tabla)
            elements.append(Spacer(1, 1 * cm))  # Espacio entre grupos
        
        # Construir el PDF
        doc.build(elements, onLaterPages=self.encabezado_y_pie, onFirstPage=self.encabezado_y_pie)
        
    def encabezado_y_pie(self, canvas, doc):
        canvas.saveState()
        
        width, height = A4
        
        # -- ENCABEZADO --
        #Logo
        # RUTA
        canvas.drawImage(
            "app/assets/logo_universidadUCLM.png",
            2*cm,
            27*cm,
            width=3*cm,
            height=3*cm,
            preserveAspectRatio=True
        )
        
        # Titulo
        canvas.setFont("Helvetica-Bold", 14)
        canvas.drawCentredString(width/2, 25.5*cm, self.NOMBRE)
        canvas.setFont("Helvetica", 9)
        canvas.drawString(2*cm, height-2.7*cm, self.AUTOR)
        canvas.drawRightString(width - 2*cm, height-2.7*cm, self.FECHA)
        
        # Linea 1
        canvas.line(
            doc.leftMargin,
            26.8*cm,
            width - doc.rightMargin,
            26.8*cm
        )
        # contenido tabla platypus
        
        # Linea 2
        canvas.line(
            doc.leftMargin,
            2.5*cm,
            width - doc.rightMargin,
            2.5*cm
        )
        # -- PIE DE PAGINA --
        # Izquierda
        canvas.setFont("Helvetica", 9)
        canvas.drawString(2*cm, 1.5*cm, self.UNIVERSIDAD)
        # Derecha
        canvas.drawRightString(width-2*cm, 1.5*cm, f"Página {doc.page}")
        
        canvas.restoreState()