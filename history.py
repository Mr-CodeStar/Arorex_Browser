import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

file=open("history.txt","r")
temp=file.readlines()
file.close()
data=[]
for i in temp:
    data.append(i.split("   "))


class TableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Arorex History')
        self.setGeometry(100, 100, 400, 300)
        
        self.create_table()

    def create_table(self):
        table_widget = QTableWidget()
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(len(data[0]))
        
        for i in range(len(data)):
            for j in range(len(data[0])):
                table_widget.setItem(i, j, QTableWidgetItem(data[i][j]))
        
        self.setCentralWidget(table_widget)

app = QApplication(sys.argv)
window = TableWindow()
window.show()
sys.exit(app.exec())
