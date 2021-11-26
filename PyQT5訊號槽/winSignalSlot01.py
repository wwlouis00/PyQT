from PyQt5.QtWidgets import QPushButton ,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
import sys

app = QApplication([])
widget = QWidget()

def showMsg():
    QMessageBox.information(widget,"訊號提示框","OK彈出測試訊息")
btn = QPushButton("測試舔及按鈕",widget)
btn.clicked.connect(showMsg)
widget.show()
sys.exit(app.exec_())