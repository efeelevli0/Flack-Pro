import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap, QColor, QPainter
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

# Yüksek çözünürlüklü (256x256) ikon tuvali
icon_pixmap = QPixmap(256, 256)
icon_pixmap.fill(Qt.transparent)

painter = QPainter(icon_pixmap)
painter.setRenderHint(QPainter.Antialiasing)

# Arka plan ve yuvarlak köşeler
painter.setBrush(QColor(25, 25, 25))
painter.drawRoundedRect(10, 10, 236, 236, 50, 50)

# "F" Harfi
painter.setPen(QColor(255, 255, 255))
font = painter.font()
font.setPointSize(120)
font.setBold(True)
painter.setFont(font)
painter.drawText(icon_pixmap.rect(), Qt.AlignCenter, "F")
painter.end()

# ICO olarak kaydet
icon_pixmap.save("flack_logo.ico")
print("Masaüstü ve Setup için flack_logo.ico dosyası başarıyla oluşturuldu!")