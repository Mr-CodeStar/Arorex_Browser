from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWebEngineWidgets import QWebEngineView  # Import QWebEngineView
from PyQt6.QtWebChannel import QWebChannel
from PyQt6.QtCore import QUrl
import os
from datetime import datetime
import subprocess
import platform

class Bridge(QtCore.QObject):
    @QtCore.pyqtSlot(str)
    def searchTextEntered(self, text):
        ui.fetch_search_text(text.strip())

class Ui_MainWindow(object):
    def __init__(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1265, 884)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.button_container_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.button_container_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.button_container_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.button_container_frame.setObjectName("button_container_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.button_container_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.button_frame_1 = QtWidgets.QFrame(parent=self.button_container_frame)
        self.button_frame_1.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.button_frame_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.button_frame_1.setObjectName("button_frame_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.button_frame_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backword_button_2 = QtWidgets.QPushButton(parent=self.button_frame_1)
        self.backword_button_2.setObjectName("backword_button_2")
        self.horizontalLayout.addWidget(self.backword_button_2)
        self.forword_button_2 = QtWidgets.QPushButton(parent=self.button_frame_1)
        self.forword_button_2.setObjectName("forword_button_2")
        self.horizontalLayout.addWidget(self.forword_button_2)
        self.home_button_2 = QtWidgets.QPushButton(parent=self.button_frame_1)
        self.home_button_2.setObjectName("home_button_2")
        self.horizontalLayout.addWidget(self.home_button_2)

        self.horizontalLayout_4.addWidget(self.button_frame_1)

        self.search_frame = QtWidgets.QFrame(parent=self.button_container_frame)
        self.search_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.search_frame.setObjectName("search_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.search_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.search_label = QtWidgets.QLabel(parent=self.search_frame)
        self.search_label.setObjectName("search_label")
        self.horizontalLayout_3.addWidget(self.search_label)
        self.gui_search_line = QtWidgets.QLineEdit(parent=self.search_frame)
        self.gui_search_line.setObjectName("gui_search_line")
        self.horizontalLayout_3.addWidget(self.gui_search_line)

        self.horizontalLayout_4.addWidget(self.search_frame)

        self.button_frame_2 = QtWidgets.QFrame(parent=self.button_container_frame)
        self.button_frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.button_frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.button_frame_2.setObjectName("button_frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.button_frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.new_window_button = QtWidgets.QPushButton(parent=self.button_frame_2)
        self.new_window_button.setObjectName("new_window_button")
        self.horizontalLayout_2.addWidget(self.new_window_button)
        self.history_button = QtWidgets.QPushButton(parent=self.button_frame_2)
        self.history_button.setObjectName("history_button")
        self.horizontalLayout_2.addWidget(self.history_button)
        self.update_button = QtWidgets.QPushButton(parent=self.button_frame_2)
        self.update_button.setObjectName("update_button")
        self.horizontalLayout_2.addWidget(self.update_button)
        self.horizontalLayout_4.addWidget(self.button_frame_2)

        self.verticalLayout.addWidget(self.button_container_frame)

        self.html_container_frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.html_container_frame.sizePolicy().hasHeightForWidth())
        self.html_container_frame.setSizePolicy(sizePolicy)
        self.html_container_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.html_container_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.html_container_frame.setObjectName("html_container_frame")
        self.html_layout = QtWidgets.QVBoxLayout(self.html_container_frame)
        self.html_layout.setObjectName("html_layout")
        self.verticalLayout.addWidget(self.html_container_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1265, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.bridge = Bridge()
        self.channel = QWebChannel()
        self.channel.registerObject("bridge", self.bridge)
        self.browser_home_page()

        ############ button function call#####################
        self.gui_search_line.returnPressed.connect(self.fetch_search_text)
        self.home_button_2.clicked.connect(self.browser_home_page)
        self.history_button.clicked.connect(self.history)
        self.backword_button_2.clicked.connect(self.backword)
        self.forword_button_2.clicked.connect(self.forword)
        self.new_window_button.clicked.connect(self.new_window_func)
        self.update_button.clicked.connect(self.update)

    ################# setup function value representation###############
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Arorex Browser  1.0.0.0"))
        self.backword_button_2.setText(_translate("MainWindow", "⟲"))
        self.forword_button_2.setText(_translate("MainWindow", "⟳"))
        self.home_button_2.setText(_translate("MainWindow", "🏠"))
        self.search_label.setText(_translate("MainWindow", "Link-Search"))
        self.new_window_button.setText(_translate("MainWindow", "+"))
        self.history_button.setText(_translate("MainWindow", "⥀"))
        self.update_button.setText(_translate("MainWindow", "⚙️"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
    
    ###########button functions###############################

    def browser_home_page(self):
        while self.html_layout.count():
            child = self.html_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        self.web_view = QWebEngineView(parent=self.html_container_frame)
        self.html_layout.addWidget(self.web_view)
        html_file_path = os.path.join(QtCore.QDir.currentPath(), 'home.html')
        self.web_view.load(QtCore.QUrl.fromLocalFile(html_file_path))
        self.web_view.page().setWebChannel(self.channel)

    def fetch_search_text(self, text=None):
        date_time=datetime.now()
        date=date_time.strftime("%Y-%m-%d")
        time=date_time.strftime("%H:%M:%S")
        history_file=open("history.txt","a")
        if text:
            value=text.strip()+"    "+date+"    "+time+"\n"
            history_file.write(value)
            if text.startswith("https://"):
                self.browser_search(text.strip())
            else:
                result="https://google.com/search?q="+text.strip()
                self.browser_search(result)
            history_file.close()
            return

        search_text = self.gui_search_line.text()
        self.gui_search_line.clear()
        value=search_text.strip()+"    "+date+"    "+time+"\n"
        history_file.write(value)
        if search_text.startswith("https://"):
            self.browser_search(text.strip())
        else:
            result="https://google.com/search?q="+search_text.strip()
            self.browser_search(result)
        history_file.close()

    def browser_search(self, text):
        while self.html_layout.count():
            child = self.html_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.web_view = QWebEngineView(parent=self.html_container_frame)
        self.html_layout.addWidget(self.web_view)
        self.web_view.setUrl(QUrl(text))

    def history(self):
        subprocess.Popen(["python","history.py"])
    def backword(self):
        self.backword_button_2.clicked.connect(self.web_view.back)
    def forword(self):
        self.forword_button_2.clicked.connect(self.web_view.forward)
    def new_window_func(self):
        new_button = QtWidgets.QPushButton(f"New Button {self.html_layout.count() + 1}", parent=self.html_container_frame)
        new_button.setObjectName(f"new_button_{self.html_layout.count() + 1}")
        
        if not hasattr(self, 'button_column_layout'):
            self.button_column_layout = QtWidgets.QHBoxLayout()
            self.html_layout.addLayout(self.button_column_layout)
        new_button.clicked.connect(self.run_practice_script)
        self.button_column_layout.addWidget(new_button)
    def run_practice_script(self):
        subprocess.Popen(["python", "browser.py"])
    def update(self):
        subprocess.Popen(["python","update.py"])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    with open("browser.qss", "r") as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
