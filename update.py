import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Display File Content")
        self.resize(500,500)
        # Create a QTextEdit widget
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        # Load the content of the file
        file_name = 'update.txt'
        self.load_file_content(file_name)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_file_content(self, file_name):
        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                content = file.read()
                self.text_edit.setPlainText(content)
        else:
            print(f"File {file_name} does not exist.")
            self.text_edit.setPlainText(f"The file '{file_name}' does not exist.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
