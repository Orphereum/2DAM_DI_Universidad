import os
from PySide6.QtWidgets import QApplication


class StyleManager:

    @staticmethod
    def _get_styles_path():
        return os.path.dirname(__file__)

    # -------------------------
    # CARGAR ESTILO PRINCIPAL
    # -------------------------
    @staticmethod
    def load_style():
        base_path = StyleManager._get_styles_path()
        ruta = os.path.join(base_path, "app_style.qss")

        if not os.path.exists(ruta):
            print("⚠️ No se encontró app_style.qss")
            return ""

        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print("❌ Error cargando estilos:", e)
            return ""

    # -------------------------
    # APLICAR ESTILO GLOBAL
    # -------------------------
    @staticmethod
    def apply(app=None):
        if app is None:
            app = QApplication.instance()

        if app is None:
            print("❌ No hay QApplication activa")
            return

        style = StyleManager.load_style()
        app.setStyleSheet(style)

    # -------------------------
    # RECARGAR ESTILOS (HOT RELOAD)
    # -------------------------
    @staticmethod
    def reload():
        app = QApplication.instance()

        if app:
            StyleManager.apply(app)
            print("🎨 Estilos recargados correctamente")