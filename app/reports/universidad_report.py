# app/reports/universidad_report.py
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from datetime import datetime
import os

class GeneradorInformeUniversidades_Facultades:

    def __init__(self, universidades):
        """
        Constructor del reporte de Jaime Ponce.
        Mantiene la estructura intacta pero renueva el diseño estético general.
        """
        self.universidades = universidades
        # Metadatos corporativos obligatorios de Jaime
        self.NOMBRE = "INFORME DE GENERAL DE UNIVERSIDADES"
        self.AUTOR = "Jaime Ponce Sáez"
        self.FECHA = datetime.now().strftime("%d/%m/%y")
        self.UNIVERSIDAD = "Universidad Castilla-LaMancha UCLM"

    def generar(self, ruta_pdf):
        # Configuración del documento base con márgenes limpios y optimizados
        doc = SimpleDocTemplate(
            ruta_pdf,
            pagesize=A4,
            topMargin=5.2 * cm,       # Espacio amplio para el nuevo banner geométrico superior
            bottomMargin=4.5 * cm,    # Espacio holgado para la distribución limpia del pie
            leftMargin=2.4 * cm,      # Estructura de márgenes asimétricos modernos
            rightMargin=2.4 * cm
        )
        elements = []
        estilo = getSampleStyleSheet()
        
        # Rediseño del bloque de texto de bajada (Alineado a la izquierda, look moderno)
        estilo_cursiva_y_centrado = ParagraphStyle(
            "CursivaYCentrado",
            parent=estilo["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            textColor=colors.HexColor("#6B7280"), # Tono gris tenue sofisticado
            alignment=TA_LEFT,
            leading=14
        )
        
        elements.append(Paragraph("<b>Registro Técnico:</b> Control de centros universitarios dependientes, datos de localización y canales de comunicación.", estilo_cursiva_y_centrado))
        elements.append(Spacer(1, 25))
        
        # Estilos tipográficos exclusivos para diferenciar las secciones de Jaime
        estilo_titulo_sede = ParagraphStyle(
            "TituloSedeJaime",
            parent=estilo["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13,
            textColor=colors.HexColor("#065F46"), # Verde esmeralda institucional
            spaceAfter=3
        )
        
        estilo_sub_sede = ParagraphStyle(
            "SubSedeJaime",
            parent=estilo["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9,
            textColor=colors.HexColor("#374151")
        )
        
        # Recorrido de los datos estructurados de las sedes
        for univ in self.universidades:
            nombre_universidad = univ['nombre']
            facultades = univ.get('facultades', [])
            num_facultades = len(facultades)
            
            # Títulos de sección renovados con tipografía limpia y estructurada
            elements.append(Paragraph(f"CAMPUS REGISTRADO: {nombre_universidad.upper()}", estilo_titulo_sede))
            elements.append(Paragraph(f"Infraestructuras académicas activas: <b>{num_facultades} centros</b>", estilo_sub_sede))
            elements.append(Spacer(1, 10))
            
            # Cabeceras de columnas para la estructura tabular
            data = [["Código", "Nombre de la Facultad / Centro", "Teléfono de Contacto"]]
            
            if num_facultades > 0:
                for fac in facultades:
                    id_fac = str(fac.get('id_facultad', 'N/A'))
                    nom_fac = fac.get('nombre', 'Sin nombre')
                    tel_fac = fac.get('telefono', 'Sin teléfono')
                    data.append([id_fac, nom_fac, tel_fac])
            else:
                data.append(["-", "No hay facultades registradas en esta sede", "-"])
            
            # 🎨 NUEVO DISEÑO DE TABLA: Enfoque de "Líneas Flotantes" Tecnológicas (Sin bordes duros)
            tabla = Table(data, colWidths=[2.2 * cm, 9.8 * cm, 4.2 * cm])
            tabla.setStyle(TableStyle([
                # Eliminamos rejillas completas por separadores horizontales minimalistas
                ("LINEBELOW", (0, 0), (-1, -1), 0.5, colors.HexColor("#E5E7EB")),
                ("LINEBELOW", (0, 0), (-1, 0), 1.5, colors.HexColor("#065F46")), # Subrayado grueso en cabecera
                
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#1F2937")),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (0, 0), (0, -1), "CENTER"),    
                ("ALIGN", (2, 0), (2, -1), "CENTER"),    
                
                # Cabecera totalmente distinta: Fondo transparente con texto destacado en Verde Oscuro
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F3F4F6")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#065F46")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 10),
                
                ("FONTNAME", (1, 1), (1, -1), "Helvetica-Bold"),
                
                # Degradado alterno muy limpio usando un patrón de fondo claro tecnológico
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F9FAFB")]),
                
                # Mayor separación vertical para que los datos no queden comprimidos
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]))
            
            elements.append(tabla)
            elements.append(Spacer(1, 24))  # Espaciado amplio entre bloques
        
        doc.build(elements, onLaterPages=self.encabezado_y_pie, onFirstPage=self.encabezado_y_pie)
        
    def encabezado_y_pie(self, canvas, doc):
        canvas.saveState()
        width, height = A4
        
        # -- ENCABEZADO GEOMÉTRICO (DASHBOARD) --
        # Dibujamos un bloque superior sólido de diseño moderno para enmarcar la cabecera
        canvas.setFillColor(colors.HexColor("#065F46"))
        canvas.rect(0, height - 3.8 * cm, width, 3.8 * cm, stroke=0, fill=1)
        
        # Franja decorativa inferior del banner
        canvas.setFillColor(colors.HexColor("#047857"))
        canvas.rect(0, height - 4.0 * cm, width, 0.2 * cm, stroke=0, fill=1)
        
        # Intentamos acoplar el logotipo oficial sobre el bloque de color
        try:
            canvas.drawImage(
                "app/assets/logo_universidadUCLM.png",
                2.4 * cm,
                height - 2.8 * cm,
                width=2.0 * cm,
                height=2.0 * cm,
                preserveAspectRatio=True
            )
        except Exception:
            # Fallback elegante integrado en el banner
            canvas.setStrokeColor(colors.white)
            canvas.rect(2.4 * cm, height - 2.6 * cm, 2.0 * cm, 1.2 * cm, stroke=1, fill=0)
            canvas.setFillColor(colors.white)
            canvas.setFont("Helvetica-Bold", 8)
            canvas.drawString(2.6 * cm, height - 2.1 * cm, "UCLM")
        
        # Configuración tipográfica del título principal (Texto en blanco arriba del banner)
        canvas.setFont("Helvetica-Bold", 14)
        canvas.setFillColor(colors.white)
        canvas.drawString(5.0 * cm, height - 2.2 * cm, self.NOMBRE)
        
        # Metadatos superiores refinados
        canvas.setFont("Helvetica", 9)
        canvas.setFillColor(colors.HexColor("#D1FAE5")) # Texto verde claro legible
        canvas.drawString(5.0 * cm, height - 2.8 * cm, f"Especialista: {self.AUTOR}")
        canvas.drawRightString(width - 2.4 * cm, height - 2.8 * cm, f"Fecha Ref: {self.FECHA}")
        
        # -- PIE DE PÁGINA TECNOLÓGICO --
        # Línea divisoria inferior sutil
        canvas.setStrokeColor(colors.HexColor("#E5E7EB"))
        canvas.setLineWidth(1)
        canvas.line(2.4 * cm, 2.4 * cm, width - 2.4 * cm, 2.4 * cm)
        
        # Textos informativos inferiores redistribuidos lateralmente
        canvas.setFont("Helvetica-Bold", 8.5)
        canvas.setFillColor(colors.HexColor("#374151"))
        canvas.drawString(2.4 * cm, 1.5 * cm, self.UNIVERSIDAD.upper())
        
        canvas.setFont("Helvetica", 8.5)
        canvas.setFillColor(colors.HexColor("#6B7280"))
        canvas.drawRightString(width - 2.4 * cm, 1.5 * cm, f"Documento General  |  Pág. {doc.page}")
        
        canvas.restoreState()