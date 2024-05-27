import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import torch
import cv2
import numpy as np
from capture_pyuic import Ui_MainWindow  # 변환된 UI 파일 임포트

class ObjectDetectionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('YOLOv5 Object Detection')
        self.setGeometry(100, 100, 1200, 600)  # 가로 크기를 넓힘
        self.initUI()
        self.model = torch.hub.load('./yolov5', model='custom', path='./pt/best.pt', source='local')

    def initUI(self):
        self.ui.upload_button.clicked.connect(self.load_image)
        self.ui.start_webcam_button.clicked.connect(self.start_webcam)

    def load_image(self):
        self.clear_labels()  # 화면 초기화

        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Images (*.png *.xpm *.jpg *.jpeg)', options=options)
        if fileName:
            image = cv2.imread(fileName)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # 원본 이미지를 왼쪽 화면에 표시
            self.display_image(image_rgb, self.ui.image_label)

            results = self.model(image)
            results.render()  # Draw boxes and labels on the image
            rendered_img = results.ims[0]  # 수정된 부분
            rendered_img_rgb = cv2.cvtColor(rendered_img, cv2.COLOR_BGR2RGB)

            # 감지 결과 이미지를 오른쪽 화면에 표시
            self.display_image(rendered_img_rgb, self.ui.result_label)

    def start_webcam(self):
        self.clear_labels()  # 화면 초기화

    def clear_labels(self):
        self.ui.image_label.clear()
        self.ui.result_label.clear()
        self.ui.image_label.setText("No Image")
        self.ui.result_label.setText("No Image")

    def display_image(self, image, label):
        if image is None or image.size == 0:
            return
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_img = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setText("")

def main():
    app = QApplication(sys.argv)
    window = ObjectDetectionApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


