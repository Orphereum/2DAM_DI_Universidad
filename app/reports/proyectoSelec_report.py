from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from datetime import datetime
import os

class GeneradorInformeProyecto:

    def __init__(self, grupo, proyecto, subvenciones):
        self.grupo = grupo
        self.proyecto = proyecto
        self.subvenciones = subvenciones
        # INICIALIZACION
        self.NOMBRE = f"INFORME DEL PROYECTO {proyecto[1]}"
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
        
        elements.append(Paragraph("Informe generado para mostrar las subvenciones obtenidas de dicho proyecto", estilo_cursiva_y_centrado))
        elements.append(Spacer(1,12))
        
        # Grupo
        elements.append(Paragraph(f"Grupo: {self.grupo}", estilo["Heading2"]))
        elements.append(Spacer(1, 0.2 * cm))

        # Proyecto
        elements.append(Paragraph(f"Proyecto: {self.proyecto[1]}", estilo["Normal"]))
        elements.append(Paragraph(f"Descripción: {self.proyecto[2]}", estilo["Normal"]))
        elements.append(Spacer(1, 0.3 * cm))

        # Tabla de subvenciones
        data = [["Subvención", "Importe (€)"]]

        total = 0

        for s in self.subvenciones:
            data.append([s[1], f"{s[2]} €"])
            total += s[2]

        data.append(["Total:", f"{total} €"])

        tabla = Table(data)
        tabla.setStyle(TableStyle([
            ("GRID", (0,0), (-1,-1), 0.45, colors.black),
            ("BACKGROUND", (0,0), (-1,-1), "#D1858E"),
            ("TEXTCOLOR", (0,0), (-1,-1), colors.white),
            ("FONTNAME", (0,0), (-1,-1), "Courier"),
            ("FONTSIZE", (0,0), (-1,-1), 10),
            # cabecera
            ("BACKGROUND", (0,0), (-1,0), "#850815"),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,0), 12),
            # cabecera COLUMNA-NOMBRE SUBVENCION
            ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold")
            
        ]))
        elements.append(tabla)

        doc.build(elements,  onLaterPages=self.encabezado_y_pie, onFirstPage=self.encabezado_y_pie)
        
    def encabezado_y_pie(self, canvas, doc):
        canvas.saveState()
        
        width, height = A4
        
        # -- ENCABEZADO --
        #Logo
        # RUTA
        ruta_logo = os.path.join(os.path.dirname(__file__), "logo_universidadUCLM.png")
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
        