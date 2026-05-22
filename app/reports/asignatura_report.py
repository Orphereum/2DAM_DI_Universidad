from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle,
    Paragraph, Spacer, Image
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os


def generar_pdf_asignaturas(asignaturas, ruta, filtros):
    doc = SimpleDocTemplate(ruta, pagesize=A4)
    styles = getSampleStyleSheet()

    elementos = []

    # =========================
    # CABECERA (LOGO + TITULO)
    # =========================
    logo_path = os.path.join("app", "assets", "logo_UniversidadUCLM.png")

    logo = None
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=80, height=50)

    titulo = Paragraph(
        "<b>INFORME DE ASIGNATURAS</b><br/>Sistema de Gestión Universitaria",
        styles["Title"]
    )

    cabecera_data = [[logo, titulo]]
    cabecera = Table(cabecera_data, colWidths=[100, 400])

    cabecera.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))

    elementos.append(cabecera)
    elementos.append(Spacer(1, 10))

    # =========================
    # LINEA SEPARADORA
    # =========================
    linea = Table([[""]], colWidths=[500])
    linea.setStyle(TableStyle([
        ("LINEABOVE", (0, 0), (-1, -1), 1, colors.grey)
    ]))
    elementos.append(linea)
    elementos.append(Spacer(1, 10))

    # =========================
    # SUBTÍTULO
    # =========================
    subtitulo = Paragraph(
        f"<b>Grado:</b> {filtros['grado']}",
        styles["Heading2"]
    )
    elementos.append(subtitulo)
    elementos.append(Spacer(1, 10))

    # =========================
    # FILTROS
    # =========================
    filtros_data = [
        ["Curso", filtros["curso"]],
        ["Cuatrimestre", filtros["cuatrimestre"]],
        ["Tipo", filtros["tipo"]],
    ]

    tabla_filtros = Table(filtros_data, colWidths=[150, 200])

    tabla_filtros.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ]))

    elementos.append(tabla_filtros)
    elementos.append(Spacer(1, 20))

    # =========================
    # TABLA PRINCIPAL
    # =========================
    data = [["Nombre", "Créditos", "Curso", "Cuatrimestre", "Tipo"]]

    for a in asignaturas:
        data.append([
            a.nombre,
            str(a.creditos),
            str(a.curso),
            str(a.cuatrimestre),
            "Obligatoria" if a.obligatoria else "Optativa"
        ])

    tabla = Table(data, repeatRows=1)

    tabla.setStyle(TableStyle([
        # Cabecera
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2c3e50")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        # Celdas
        ("GRID", (0, 0), (-1, -1), 0.3, colors.grey),
        ("ALIGN", (1, 1), (-1, -1), "CENTER"),

        # Alternancia
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.whitesmoke, colors.lightgrey]),
    ]))

    elementos.append(tabla)
    elementos.append(Spacer(1, 20))

    # =========================
    # PIE
    # =========================
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    pie = Paragraph(
        f"Informe generado el {fecha}",
        styles["Italic"]
    )

    elementos.append(pie)

    # =========================
    # GENERAR
    # =========================
    doc.build(elementos)