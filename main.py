import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow  # Importamos la clase MainWindow desde el archivo donde definiste la interfaz

def main():
    # Crear la aplicación
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Estilo visual opcional

    # Crear la ventana principal
    main_window = MainWindow()
    main_window.show()

    # Ejecutar el loop principal de la aplicación
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
