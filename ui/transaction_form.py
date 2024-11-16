from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit,
    QTextEdit, QComboBox, QDateEdit, QCalendarWidget, QGroupBox, QDialog, QGridLayout
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont

from utils.calendar_dialog import CalendarDialog

class TransactionForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Transaction")
        self.setGeometry(200, 200, 500, 600)
        self.setStyleSheet("background-color: #f7f9fc;")
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Encabezado
        title_label = QLabel("New Transaction")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setStyleSheet("color: #37474f;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Grupo: Tipo de transacción
        type_group = QGroupBox("Transaction Type")
        type_group.setStyleSheet("font-size: 12px; font-weight: bold;")
        type_layout = QHBoxLayout(type_group)

        self.btn_income = QPushButton("Income")
        self.btn_income.setCheckable(True)
        self.btn_income.setStyleSheet(self.get_transaction_type_button_style(False))
        self.btn_income.clicked.connect(lambda: self.update_transaction_type("Income"))
        type_layout.addWidget(self.btn_income)

        self.btn_expense = QPushButton("Expense")
        self.btn_expense.setCheckable(True)
        self.btn_expense.setStyleSheet(self.get_transaction_type_button_style(False))
        self.btn_expense.clicked.connect(lambda: self.update_transaction_type("Expense"))
        type_layout.addWidget(self.btn_expense)

        main_layout.addWidget(type_group)

        # Grupo: Detalles de la transacción
        details_group = QGroupBox("Transaction Details")
        details_group.setStyleSheet("font-size: 12px; font-weight: bold;")
        details_layout = QVBoxLayout(details_group)

        # Monto
        amount_label = QLabel("Amount:")
        amount_label.setFont(QFont("Arial", 12, QFont.Bold))
        details_layout.addWidget(amount_label)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter the amount")
        self.amount_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #b0bec5;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
        """)
        details_layout.addWidget(self.amount_input)

        # Etiquetas
        label_layout = QHBoxLayout()
        label_label = QLabel("Category:")
        label_label.setFont(QFont("Arial", 12, QFont.Bold))
        label_layout.addWidget(label_label)

        self.label_combo = QComboBox()
        self.label_combo.addItems(["Food", "Transport", "Rent"])
        self.label_combo.setStyleSheet("""
            QComboBox {
                padding: 6px;
                border: 1px solid #b0bec5;
                border-radius: 4px;
                font-size: 14px;
                background-color: white;
            }
        """)
        label_layout.addWidget(self.label_combo)

        self.add_label_button = QPushButton("+ Add Category")
        self.add_label_button.setStyleSheet("""
            QPushButton {
                color: #2979ff;
                font-size: 12px;
                background: none;
                border: none;
            }
            QPushButton:hover {
                text-decoration: underline;
            }
        """)
        self.add_label_button.clicked.connect(self.add_category)
        label_layout.addWidget(self.add_label_button)

        details_layout.addLayout(label_layout)

        # Fecha
        date_label = QLabel("Date:")
        date_label.setFont(QFont("Arial", 12, QFont.Bold))
        details_layout.addWidget(date_label)

        date_layout = QHBoxLayout()
        self.date_edit = QDateEdit(QDate.currentDate())

        self.date_edit.setStyleSheet("""
            QDateEdit {
                border: 1px solid #b0bec5;
                border-radius: 4px;
                padding: 6px;
                font-size: 14px;
            }
        """)
        date_layout.addWidget(self.date_edit)

        self.calendar_button = QPushButton("📅")
        self.calendar_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                background-color: #e3f2fd;
                border: 1px solid #b0bec5;
                border-radius: 4px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #bbdefb;
            }
        """)
        self.calendar_button.clicked.connect(self.open_calendar)
        date_layout.addWidget(self.calendar_button)

        details_layout.addLayout(date_layout)
        main_layout.addWidget(details_group)

        # Descripción
        description_label = QLabel("Description:")
        description_label.setFont(QFont("Arial", 8, QFont.Bold))
        main_layout.addWidget(description_label)

        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Add a description or notes")
        self.description_input.setStyleSheet("""
            QTextEdit {
                border: 1px solid #b0bec5;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
        """)
        main_layout.addWidget(self.description_input)

        # Botones de acción
        buttons_layout = QHBoxLayout()

        self.add_button = QPushButton("Add")
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #2979ff;
                color: white;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
        """)
        self.add_button.clicked.connect(self.add_transaction)
        buttons_layout.addWidget(self.add_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #90caf9;
                color: white;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #64b5f6;
            }
        """)
        self.cancel_button.clicked.connect(self.close)
        buttons_layout.addWidget(self.cancel_button)

        main_layout.addLayout(buttons_layout)

    def get_transaction_type_button_style(self, selected):
        if selected:
            return """
                QPushButton {
                    background-color: #2979ff;
                    color: white;
                    border-radius: 6px;
                    padding: 10px 20px;
                    font-size: 14px;
                    font-weight: bold;
                }
            """
        return """
            QPushButton {
                background-color: #e3f2fd;
                color: #2979ff;
                border: 1px solid #2979ff;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 14px;
            }
        """

    def update_transaction_type(self, transaction_type):
        self.btn_income.setStyleSheet(self.get_transaction_type_button_style(transaction_type == "Income"))
        self.btn_expense.setStyleSheet(self.get_transaction_type_button_style(transaction_type == "Expense"))

    def open_calendar(self):
        dialog = CalendarDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.date_edit.setDate(dialog.selected_date)

    def add_category(self):
        print("Add category functionality placeholder.")

    def add_transaction(self):
        print("Transaction added placeholder.")


