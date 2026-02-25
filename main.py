import sys
import os
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from app.controller.AppController import AppController
import app.resources.resources_rc

def resource_path(relative_path):
    """Ruta para desarrollo y PyInstaller"""
    try:
        base_path = Path(sys._MEIPASS)
    except Exception:
        base_path = Path(__file__).parent
    return base_path / relative_path

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Gestor Universidad")
    
    # Icono de ventana desde tu archivo
    icon_path = resource_path("app/assets/universidad.ico")
    app.setWindowIcon(QIcon(str(icon_path)))
    
    controller = AppController()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
