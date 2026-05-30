from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime
import os


def generar_pdf_profesores(profesores, ruta):
    doc = SimpleDocTemplate(ruta, pagesize=landscape(A4))
    styles = getSampleStyleSheet()
    elementos = []

    normal = ParagraphStyle(
        "normal",
        parent=styles["Normal"],
        fontSize=8,
        leading=10
    )

    logo_path = os.path.join("app", "assets", "logo_UniversidadUCLM.png")
    logo = Image(logo_path, width=80, height=50) if os.path.exists(logo_path) else ""

    titulo = Paragraph(
        "<b>INFORME DE PROFESORES</b><br/>Sistema de Gestión Universitaria",
        styles["Title"]
    )

    cabecera = Table([[logo, titulo]], colWidths=[100, 650])
    cabecera.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
    ]))

    elementos.append(cabecera)
    elementos.append(Spacer(1, 12))

    data = [[
        "Nombre",
        "Correo",
        "Teléfono",
        "Título",
        "Departamento",
        "Jefe",
        "Asignaturas"
    ]]

    for p in profesores:
        asignaturas = ", ".join(p.asignaturas) if p.asignaturas else "Sin asignaturas"

        data.append([
            Paragraph(p.nombre or "", normal),
            Paragraph(p.correo or "", normal),
            p.telefono or "",
            Paragraph(p.titulo or "", normal),
            str(p.id_departamento or ""),
            "Sí" if p.jefe_dtp else "No",
            Paragraph(asignaturas, normal)
        ])

    tabla = Table(
        data,
        repeatRows=1,
        colWidths=[130, 150, 80, 120, 85, 45, 180]
    )

    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2c3e50")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),

        ("GRID", (0, 0), (-1, -1), 0.3, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [
            colors.whitesmoke,
            colors.lightgrey
        ]),

        ("ALIGN", (4, 1), (5, -1), "CENTER"),
    ]))

    elementos.append(tabla)
    elementos.append(Spacer(1, 20))

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    elementos.append(Paragraph(f"<i>Informe generado el {fecha}</i>", styles["Italic"]))

    doc.build(elementos)