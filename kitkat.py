import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt
def on_click():
    print("Button clicked!")

def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            print("Escape key pressed")
            exit()

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 Example')
window.setGeometry(100, 100, 280, 80)

button = QPushButton('Click Me', window)
button.clicked.connect(on_click)
button.resize(200, 40)
button.move(40, 20)

window.show()
sys.exit(app.exec_())