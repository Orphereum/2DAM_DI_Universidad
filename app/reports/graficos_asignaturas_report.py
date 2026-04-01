def generar_pdf_graficos_pro(asignaturas, ruta, filtros):
    import matplotlib.pyplot as plt
    from reportlab.platypus import (
        SimpleDocTemplate, Image, Spacer,
        Paragraph, Table, TableStyle
    )
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import cm
    from datetime import datetime
    import tempfile
    import os

    styles = getSampleStyleSheet()
    elementos = []

    # =========================
    # CABECERA PRO (LOGO + TITULO)
    # =========================
    logo_path = os.path.join("app", "assets", "logo_UniversidadUCLM.png")

    logo = Image(logo_path, width=70, height=45) if os.path.exists(logo_path) else ""

    titulo = Paragraph(
        "<b>INFORME DE DASHBOARD ACADÉMICO</b>",
        styles["Title"]
    )

    subtitulo = Paragraph(
        "Sistema de Gestión Universitaria",
        styles["Normal"]
    )

    cabecera = Table([
        [logo, titulo],
        ["", subtitulo]
    ], colWidths=[80, 400])

    cabecera.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ]))

    elementos.append(cabecera)
    elementos.append(Spacer(1, 15))

    # =========================
    # FILTROS (CAJA PRO)
    # =========================
    tabla_filtros = Table([
        ["Grado", filtros.split("|")[0]],
        ["Curso", filtros.split("|")[1]],
        ["Cuatrimestre", filtros.split("|")[2]],
        ["Tipo", filtros.split("|")[3]],
    ], colWidths=[120, 300])

    tabla_filtros.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#7A1C2E")),
        ("TEXTCOLOR", (0, 0), (0, -1), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
    ]))

    elementos.append(tabla_filtros)
    elementos.append(Spacer(1, 20))

    # =========================
    # DATOS
    # =========================
    cursos = [1, 2, 3, 4]
    conteo = [0, 0, 0, 0]
    creditos = [0, 0, 0, 0]

    oblig = sum(1 for a in asignaturas if a.obligatoria)
    opt = sum(1 for a in asignaturas if not a.obligatoria)

    c1 = sum(1 for a in asignaturas if a.cuatrimestre == 1)
    c2 = sum(1 for a in asignaturas if a.cuatrimestre == 2)

    for a in asignaturas:
        if 1 <= a.curso <= 4:
            conteo[a.curso - 1] += 1
            creditos[a.curso - 1] += a.creditos

    # =========================
    # FUNCION GRAFICOS PRO
    # =========================
    def crear_barra(titulo, valores):
        fig = plt.figure(figsize=(5, 3.5))
        ax = fig.add_subplot(111)

        ax.bar(cursos, valores, color="#7A1C2E")
        ax.set_title(titulo, fontsize=11, fontweight="bold")

        ax.set_xticks(cursos)
        ax.set_xticklabels([f"{i}º" for i in cursos])

        ax.grid(axis="y", linestyle="--", alpha=0.3)

        path = os.path.join(tempfile.gettempdir(), f"{titulo}.png")
        plt.savefig(path, dpi=300, bbox_inches="tight")
        plt.close()

        return path

    def crear_pie(titulo, valores, labels):
        if sum(valores) == 0:
            valores = [1]
            labels = ["Sin datos"]

        fig = plt.figure(figsize=(5, 3.5))
        ax = fig.add_subplot(111)

        ax.pie(
            valores,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            colors=["#7A1C2E", "#A8324A"]
        )

        ax.set_title(titulo, fontsize=11, fontweight="bold")

        path = os.path.join(tempfile.gettempdir(), f"{titulo}.png")
        plt.savefig(path, dpi=300, bbox_inches="tight")
        plt.close()

        return path

    # =========================
    # CREAR GRAFICOS
    # =========================
    g1 = crear_barra("Asignaturas por curso", conteo)
    g2 = crear_pie("Tipo de asignaturas", [oblig, opt], ["Obligatorias", "Optativas"])
    g3 = crear_barra("Créditos por curso", creditos)
    g4 = crear_pie("Distribución por cuatrimestre", [c1, c2], ["1º", "2º"])

    # =========================
    # GRID PROFESIONAL
    # =========================
    tabla_graficos = Table([
        [
            Image(g1, width=8*cm, height=6*cm),
            Image(g2, width=8*cm, height=6*cm)
        ],
        [
            Image(g3, width=8*cm, height=6*cm),
            Image(g4, width=8*cm, height=6*cm)
        ]
    ], hAlign="CENTER")

    elementos.append(tabla_graficos)
    elementos.append(Spacer(1, 20))

    # =========================
    # PIE DE PÁGINA
    # =========================
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    elementos.append(Paragraph(
        f"Informe generado automáticamente el {fecha}",
        styles["Italic"]
    ))

    # =========================
    # GENERAR PDF
    # =========================
    doc = SimpleDocTemplate(ruta, pagesize=A4)
    doc.build(elementos)