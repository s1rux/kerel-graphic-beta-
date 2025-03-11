from PyQt5 import QtWidgets, QtGui, QtCore

class CustomUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt UI Clone")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #3b82f6, stop:1 #1a1a1a);")

        # Desktop Label
        self.desktop_label = QtWidgets.QLabel("Kerel Graphic UI", self)
        self.desktop_label.setGeometry(400, 50, 300, 50)
        self.desktop_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold; font-family: 'Segoe UI'; border-radius: 10px; padding: 5px;")
        self.desktop_label.setAlignment(QtCore.Qt.AlignCenter)

        # Bottom Bar
        bottom_bar = QtWidgets.QWidget(self)
        bottom_bar.setGeometry(0, 540, 1000, 60)
        bottom_bar.setStyleSheet("background-color: #1a1a1a;")

        # Start Button
        self.start_button = QtWidgets.QPushButton("K", bottom_bar)
        self.start_button.setGeometry(10, 10, 40, 40)
        self.start_button.setStyleSheet("background-color: #0078D7; color: white; font-size: 16px; border-radius: 5px;")
        self.start_button.clicked.connect(self.toggle_start_menu)

        # Time and Date
        self.time_label = QtWidgets.QLabel("11:11", bottom_bar)
        self.time_label.setGeometry(900, 10, 80, 40)
        self.time_label.setStyleSheet("color: white; font-size: 20px;")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)

        # User Info
        user_label = QtWidgets.QLabel("KerEL TEST", bottom_bar)
        user_label.setGeometry(800, 10, 100, 40)
        user_label.setStyleSheet("color: white;")

        # Timer to update clock
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.update_time()
        self.start_menu_widget = None

    def update_time(self):
        current_time = QtCore.QTime.currentTime().toString("HH:mm")
        self.time_label.setText(current_time)
    
    def toggle_start_menu(self):
        if self.start_menu_widget and self.start_menu_widget.isVisible():
            self.start_menu_widget.hide()
        else:
            self.show_start_menu()

    def show_start_menu(self):
        self.start_menu_widget = QtWidgets.QWidget(self)
        self.start_menu_widget.setGeometry(50, 200, 300, 300)
        self.start_menu_widget.setStyleSheet("background-color: #2d2d2d; border-radius: 10px;")
        
        layout = QtWidgets.QVBoxLayout()
        
        label = QtWidgets.QLabel("KerEL", self.start_menu_widget)
        label.setStyleSheet("color: white; font-size: 16px; font-weight: bold; font-family: 'Segoe UI';")
        layout.addWidget(label)
        
        subtext = QtWidgets.QLabel("KerEL InterFace", self.start_menu_widget)
        subtext.setWordWrap(True)
        subtext.setStyleSheet("color: white; font-size: 12px; font-family: 'Segoe UI';")
        layout.addWidget(subtext)
        
        spacer = QtWidgets.QLabel("", self.start_menu_widget)
        layout.addWidget(spacer)
        
        button_layout = QtWidgets.QHBoxLayout()
        settings_button = QtWidgets.QPushButton()
        settings_button.setIcon(QtGui.QIcon("settings.png"))  # Add real path to settings icon
        settings_button.setIconSize(QtCore.QSize(24, 24))
        settings_button.setStyleSheet("background: transparent;")
        settings_button.clicked.connect(lambda: self.show_message("Открываем настройки..."))
        
        power_button = QtWidgets.QPushButton()
        power_button.setIcon(QtGui.QIcon("exit.png"))  # Add real path to power icon
        power_button.setIconSize(QtCore.QSize(24, 24))
        power_button.setStyleSheet("background: transparent;")
        power_button.clicked.connect(self.close)
        
        button_layout.addWidget(settings_button)
        button_layout.addWidget(power_button)
        
        layout.addLayout(button_layout)
        self.start_menu_widget.setLayout(layout)
        self.start_menu_widget.show()

        # Close menu when clicking outside
        self.start_menu_widget.mousePressEvent = self.close_start_menu
        self.start_button.mousePressEvent = lambda event: self.toggle_start_menu()

    def close_start_menu(self, event):
        self.start_menu_widget.hide()

    def show_message(self, text):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Сообщение")
        msg_box.setText(text)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = CustomUI()
    window.show()
    sys.exit(app.exec_())
