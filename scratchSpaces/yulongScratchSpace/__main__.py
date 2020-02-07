from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout, QLabel, QSizePolicy, \
    QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QLinearGradient, QBrush, QPalette, QFont, QPixmap

application = QApplication([])


class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.resize(1080, 800)
        self.setWindowTitle("Dingy Skippers")

        main_layout = QGridLayout()
        self.setAutoFillBackground(True)

        background = QColor.fromRgb(248, 246, 238)

        title_font = QFont("Georgia", 25)

        p = self.palette()
        p.setColor(self.backgroundRole(), background)
        self.setPalette(p)

        h = self.height()
        w = self.width()

        top_left = QWidget()
        top_right = QWidget()
        bottom_left = QWidget()
        bottom_right = QStackedWidget()

        #################################################
        # The top left corner
        l = QLabel(top_left)
        l.setText("Put some butterfly here")
        # l.move(50, 50)
        # top_left.resize(w * 0.25, h * 0.1)
        main_layout.addWidget(top_left, 0, 0)
        #################################################
        '''
        trying to add an image but it's not showing up - not sure why 
        '''
        bFlyImage = QLabel(top_left)
        bFlyImage.setGeometry(10, 10, 60, 60)
        bFlyImage.setPixmap(QPixmap("../suzieScratchSpace/caterpillar.png"))

        # bFlyImage.move(50, 50)
        # top_left).resize(w * 0.25, h * 0.1)

        #################################################
        # The top right corner
        l = QLabel(top_right)
        l.setText("Butterfly Logbook Scanner")
        # l.move(w * 0.25, 50)
        l.setFont(title_font)
        l.setStyleSheet('color:#6D214F')

        # top_right.resize(w * 0.75, h * 0.1)
        # top_right.move(w * 0.25, 0)
        main_layout.addWidget(top_right, 0, 1)


        #################################################
        # The bottom right corner
        #################################################
        br_label = QLabel("Initial Page")
        br_label.setStyleSheet('color:#6D214F')
        br_label.move(100, 100)
        br_label.resize(500, 500)

        # Upload page
        upload_page = QWidget()
        upload_page_layout = QVBoxLayout()

        upload_top_text = QLabel("Welcome to the scanner\n bla bla bla...")
        upload_page_layout.addWidget(upload_top_text)
        upload_page_layout.setAlignment(upload_top_text, Qt.AlignCenter)

        drag_n_drop = QWidget()

        upload_page_layout.addWidget(drag_n_drop)
        upload_page_layout.setAlignment(drag_n_drop, Qt.AlignCenter)

        upload_bottom_text = QLabel("Or click ...")
        upload_page_layout.addWidget(upload_bottom_text)

        upload_button = QPushButton("Read Page")
        upload_button.setFixedSize(200, 50)
        upload_page_layout.addWidget(upload_button)
        upload_page_layout.setAlignment(upload_button, Qt.AlignCenter)

        upload_page_layout.addWidget(QLabel())

        upload_page.setLayout(upload_page_layout)

        # Data page
        data_page = QWidget()
        QPushButton("data", data_page)

        # Tutorial page
        tutorial_page = QWidget()
        QPushButton("tutorial", tutorial_page)

        bottom_right.addWidget(upload_page)
        bottom_right.addWidget(data_page)
        bottom_right.addWidget(tutorial_page)
        bottom_right.addWidget(br_label)
        main_layout.addWidget(bottom_right, 1, 1)
        #################################################

        #################################################
        # The bottom left corner
        bottom_leftLayout = QVBoxLayout()
        buttons = [QPushButton() for _ in range(6)]

        # function for changing all buttons back to default when a new one is clicked
        def reset_buttons_color():
            for b in buttons:
                b.setStyleSheet('background-color:rgb(248,154,121); color:black')

        for b in buttons:
            b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            bottom_leftLayout.addWidget(b)

        # Upload page -- button 0
        def button0_signal():
            print("button 0 pressed")
            bottom_right.setCurrentIndex(0)

        reset_buttons_color()

        def button0_signal():
            print("button 0 pressed")
            reset_buttons_color()
            buttons[0].setStyleSheet("background-color: rgb(248,246,238); color:#6D214F")
            bottom_right.setCurrentIndex(0)
            # update("Upload PDF page")

        buttons[0].setText("Upload PDF")
        buttons[0].clicked.connect(button0_signal)

        # Data page -- button 1
        def button1_signal():
            print("button 1 pressed")
            bottom_right.setCurrentIndex(1)
            reset_buttons_color()
            buttons[1].setStyleSheet("background-color: rgb(248,246,238); color:#6D214F")
            bottom_right.setCurrentIndex(1)
            # update("Access data page")

        buttons[1].setText("Access Data")
        buttons[1].clicked.connect(button1_signal)

        # Tutorial page -- button 2
        def button2_signal():
            print("button 2 pressed")
            bottom_right.setCurrentIndex(2)
            reset_buttons_color()
            buttons[2].setStyleSheet("background-color: rgb(248,246,238); color:#6D214F")
            bottom_right.setCurrentIndex(2)
            # update("Tutorial page")

        buttons[2].setText("How to Use?")
        buttons[2].clicked.connect(button2_signal)

        bottom_left.setLayout(bottom_leftLayout)
        bottom_left.move(0, h * 0.1)
        main_layout.addWidget(bottom_left, 1, 0)

        #################################################
        # Things about the main layout
        #################################################
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 3)
        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(1, 9)
        bottom_right.setCurrentIndex(3)
        self.setLayout(main_layout)
        application.setStyle('Windows')

    def run(self):
        self.show()
        application.exec_()

    # def dragEnterEvent(self, QDragEnterEvent):


if __name__ == "__main__":
    app = Window()
    app.run()
