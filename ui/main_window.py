import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QPushButton, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from ui.transaction_form import TransactionForm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance Manager")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #f4f7fc;")  # Fondo suave
        self.setup_ui()

    def setup_ui(self):
        # Configuración del widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(25)

        # Header layout
        header_layout = QHBoxLayout()
        header_layout.addStretch()

        self.btn_profile = self.create_icon_button("👤", "Profile")
        header_layout.addWidget(self.btn_profile)

        self.btn_settings = self.create_icon_button("⚙️", "Settings")
        header_layout.addWidget(self.btn_settings)

        main_layout.addLayout(header_layout)

        # Title label
        title_label = QLabel("Finance Manager")
        title_label.setFont(QFont("Arial", 28, QFont.Bold))
        title_label.setStyleSheet("color: #3b5998;")
        title_label.setAlignment( Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Balance section
        balance_layout = QVBoxLayout()
        balance_layout.setContentsMargins(40, 25, 40, 0)

        # Currency selector

        self.currency_combo = QComboBox()
        self.currency_combo.addItems(["USD", "EUR", "CUP"])
        self.currency_combo.setFixedWidth(100)
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

        balance_label = QLabel("Balance")
        balance_label.setFont(QFont("Arial", 14, QFont.Bold))
        balance_label.setStyleSheet("color: #5a5a5a;")
        balance_label.setAlignment(Qt.AlignCenter)
        balance_label.setFixedHeight(30)

        self.balance_value = QLabel("$12,537")
        self.balance_value.setFont(QFont("Arial", 36, QFont.Bold))
        self.balance_value.setStyleSheet("color: #4caf50;")
        self.balance_value.setAlignment(Qt.AlignCenter)
        self.balance_value.setFixedHeight(50)

        # Alinear el valor y el combo box en el layout horizontal

        balance_layout.addWidget(balance_label)
        balance_layout.addWidget(self.currency_combo)
        balance_layout.addWidget(self.balance_value)

        balance_layout.setStretchFactor(self.currency_combo, 1)
        balance_layout.setStretchFactor(balance_label, 1)


       # balance_layout.addSpacing(20)  # Espacio entre el combo y el saldo


        main_layout.addLayout(balance_layout)

        # Footer layout for buttons
        footer_layout = QHBoxLayout()
        footer_layout.addStretch()

        self.btn_history = self.create_circle_button("|||", "View your transaction history")
        footer_layout.addWidget(self.btn_history)

        self.btn_add_record = self.create_circle_button("+", "Add a new transaction")
        self.btn_add_record.clicked.connect(self.open_new_transaction_form)
        footer_layout.addWidget(self.btn_add_record)

        main_layout.addLayout(footer_layout)

    def create_icon_button(self, icon: str, tooltip: str) -> QPushButton:
        button = QPushButton(icon)
        button.setFixedSize(40, 40)
        button.setFont(QFont("Arial", 16, QFont.Bold))
        button.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                background-color: #3b5998;
                border-radius: 20px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2b4170;
            }
        """)
        button.setToolTip(tooltip)
        return button

    def create_circle_button(self, text: str, tooltip: str) -> QPushButton:
        button = QPushButton(text)
        button.setFixedSize(60, 60)
        button.setFont(QFont("Arial", 18, QFont.Bold))
        button.setStyleSheet("""
            QPushButton {
                background-color: #2979ff;
                color: #ffffff;
                border-radius: 30px;
                box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
        """)
        button.setToolTip(tooltip)
        return button

    def open_new_transaction_form(self):
        self.transaction_form = TransactionForm()
        self.transaction_form.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
