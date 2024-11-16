from PyQt5.QtWidgets import (
     QVBoxLayout,  QCalendarWidget, QDialog
)

class CalendarDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Date")
        self.setGeometry(300, 300, 400, 300)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setStyleSheet("""
            QCalendarWidget {
                border: 1px solid #b0bec5;
                border-radius: 4px;
                background-color: white;
            }
        """)
        self.calendar.clicked.connect(self.select_date)

        layout = QVBoxLayout(self)
        layout.addWidget(self.calendar)

    def select_date(self):
        self.selected_date = self.calendar.selectedDate()
        self.accept()

