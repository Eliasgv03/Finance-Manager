import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QPushButton, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance Manager")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #f3f6f9;")  # Fondo claro

        # Configuración inicial de la interfaz
        self.setup_ui()

    def setup_ui(self):
        # Configuración del widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Layout para botones de perfil y configuración
        header_layout = QHBoxLayout()
        header_layout.addStretch()

        # Botón de configuración
        self.btn_settings = QPushButton("⚙️")
        self.btn_settings.setFixedSize(30, 30)
        self.btn_settings.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                font-size: 16px;
                background-color: #2979ff;
                border-radius: 15px;
                border: none;
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
        """)
        self.btn_settings.setToolTip("Configuración")
        header_layout.addWidget(self.btn_settings)

        # Botón de perfil
        self.btn_profile = QPushButton("👤")
        self.btn_profile.setFixedSize(30, 30)
        self.btn_profile.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                font-size: 16px;
                background-color: #2979ff;
                border-radius: 15px;
                border: none;
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
        """)
        self.btn_profile.setToolTip("Preferencias")
        header_layout.addWidget(self.btn_profile)

        main_layout.addLayout(header_layout)

        # Título principal
        title_label = QLabel("Finance Manager")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setStyleSheet("color: #2979ff;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # ComboBox de moneda
        currency_layout = QVBoxLayout()
        currency_layout.setContentsMargins(40, 25, 0, 0)

        self.currency_combo = QComboBox()
        self.currency_combo.addItems(["USD", "EUR", "CUP"])
        self.currency_combo.setFixedWidth(80)
        self.currency_combo.setStyleSheet("""
            QComboBox {
                padding: 4px;
                font-size: 10px;
                color: #37474f;
                border: 1px solid #cfd8dc;
                border-radius: 4px;
                background-color: #ffffff;
            }
            QComboBox::item:selected {
                background-color: #bbdefb;
                color: #000000;
            }
        """)
        currency_layout.addWidget(self.currency_combo)
        main_layout.addLayout(currency_layout)

        # Layout para "Saldo" y el valor del saldo
        balance_layout = QVBoxLayout()
        balance_layout.setContentsMargins(40, 25, 0, 0)

        balance_label = QLabel("Saldo:")
        balance_label.setFont(QFont("Arial", 14, QFont.Bold))
        balance_label.setStyleSheet("color: #37474f;")
        balance_layout.addWidget(balance_label)

        # Valor del saldo
        self.balance_value = QLabel("$12,537")
        self.balance_value.setFont(QFont("Arial", 36, QFont.Bold))
        self.balance_value.setStyleSheet("color: #4caf50;")  # Verde para saldo positivo
        balance_layout.addWidget(self.balance_value, alignment=Qt.AlignCenter)
        balance_layout.addWidget(self.balance_value)

        main_layout.addLayout(balance_layout)

        # Botones circulares
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()

        # Botón de historial
        self.btn_history = QPushButton("///")
        self.btn_history.setFixedSize(60, 60)
        self.btn_history.setFont(QFont("Arial", 24, QFont.Bold))
        self.btn_history.setStyleSheet("""
             QPushButton {
                background-color: #2979ff;
                color: #ffffff;
                border-radius: 30px;
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
        """)
        self.btn_history.setToolTip("Historial")
        bottom_layout.addWidget(self.btn_history)

        # Botón de nuevo registro
        self.btn_add_record = QPushButton("+")
        self.btn_add_record.setFixedSize(60, 60)
        self.btn_add_record.setFont(QFont("Arial", 24, QFont.Bold))
        self.btn_add_record.setStyleSheet("""

            QPushButton {
                background-color: #2979ff;
                color: #ffffff;
                border-radius: 30px;
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
        """)
        self.btn_add_record.setToolTip("Nuevo Registro")
        bottom_layout.addWidget(self.btn_add_record)

        main_layout.addLayout(bottom_layout)

