import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class Worker(QThread):
    finished = pyqtSignal()  # Custom signal to notify the main thread when the task is finished

    def run(self):
        # This method is automatically called when the thread starts
        # Perform your time-consuming task here
        import time
        time.sleep(5)
        self.finished.emit()  # Emit the finished signal when the task is done


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("QThread Example")
        self.setGeometry(100, 100, 300, 100)

        self.label = QLabel("Click the button to start the task.", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(10, 10, 280, 30)

        self.button = QPushButton("Start Task", self)
        self.button.setGeometry(110, 50, 80, 30)
        self.button.clicked.connect(self.startTask)

    def startTask(self):
        self.button.setEnabled(False)
        self.label.setText("Task is running...")

        self.worker = Worker()
        self.worker.finished.connect(self.taskFinished)  # Connect the finished signal to the slot
        self.worker.start()  # Start the worker thread

    def taskFinished(self):
        self.label.setText("Task is finished.")
        self.button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
