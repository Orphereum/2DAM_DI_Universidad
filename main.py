import sys
from PySide6.QtWidgets import QApplication
from app.controller.AppController import AppController
import app.resources.resources_rc


app = QApplication(sys.argv)
app.setApplicationName("Gestor Universidad")


controller = AppController()
# Iniciamos la base de datos cuando este lista (Init_db)

sys.exit(app.exec())

if __name__ == "__main__":
    main()
