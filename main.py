import sys
from PySide6.QtWidgets import QApplication

from app.controller.AppController import AppController
from app.styles.style_manager import StyleManager

import app.resources.resources_rc

 
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Gestor Universidad")
    print("ANTES DE ESTILOS")
    # 🔥 ESTILOS PRIMERO
    StyleManager.apply(app)
    print("DESPUES DE ESTILOS")

    # 🔥 CONTROLLER (ya hace show internamente)
    controller = AppController()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()