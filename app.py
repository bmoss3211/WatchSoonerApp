import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import os

# This class loads the UI designed in Qt Designer
class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            # Contruct the path to the .ui file dynamically
            ui_file_path = os.path.join(os.path.dirname(__file__), 'src', 'ui', 'main_window.ui')

            # Load .ui file directly to keep UI separate from logic
            uic.loadUi(ui_file_path, self)


            self.pushButton.clicked.connect(self.on_button_click)

            self.label.setText("Hello from Python!")

        def on_button_click(self):
            print("Button clicked!")
            self.label.setText("Button was clicked!")

if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = MainWindow()
     window.show()
     sys.exit(app.exec())