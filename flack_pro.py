import os
import sys
import random
import winreg
import pygame
from pynput import keyboard
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSlider, QSystemTrayIcon, QMenu, QAction, QCheckBox
from PyQt5.QtGui import QIcon, QPixmap, QColor, QPainter
from PyQt5.QtCore import Qt

# Sıfır gecikmeli ses motorunu başlat
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()

# Çalışma dizinini bul
if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))

SESLER_DIR = os.path.join(app_path, "sesler")

normal_down, normal_up = [], []
heavy_down, heavy_up = None, None
current_volume = 1.0
pressed_keys = set()

HEAVY_KEYS = {
    keyboard.Key.space, keyboard.Key.enter, keyboard.Key.backspace, 
    keyboard.Key.shift, keyboard.Key.shift_r, keyboard.Key.tab, keyboard.Key.caps_lock
}

# --- WINDOWS BAŞLANGIÇ AYARLARI ---
REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"
APP_NAME = "FlackPro"

def is_autostart_enabled():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ)
        winreg.QueryValueEx(key, APP_NAME)
        winreg.CloseKey(key)
        return True
    except WindowsError:
        return False

def set_autostart(enable):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_SET_VALUE)
        if enable:
            exe_path = f'"{sys.executable}"' if getattr(sys, 'frozen', False) else f'"{os.path.abspath(__file__)}"'
            winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, exe_path)
        else:
            try:
                winreg.DeleteValue(key, APP_NAME)
            except OSError:
                pass
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Kayıt defteri hatası: {e}")
# -----------------------------------

def load_switch(switch_folder):
    global normal_down, normal_up, heavy_down, heavy_up
    normal_down.clear()
    normal_up.clear()
    heavy_down = None
    heavy_up = None
    
    target_dir = os.path.join(SESLER_DIR, switch_folder)
    if not os.path.exists(target_dir): return
        
    for file in os.listdir(target_dir):
        if not file.endswith(".wav"): continue
        path = os.path.join(target_dir, file)
        sound = pygame.mixer.Sound(path)
        sound.set_volume(current_volume)
        
        if "3675-down" in file: heavy_down = sound
        elif "3675-up" in file: heavy_up = sound
        elif "down.wav" in file: normal_down.append(sound)
        elif "up.wav" in file: normal_up.append(sound)
        
    if not heavy_down and normal_down: heavy_down = normal_down[0]
    if not heavy_up and normal_up: heavy_up = normal_up[0]

def on_press(key):
    if key not in pressed_keys:
        pressed_keys.add(key)
        if key in HEAVY_KEYS and heavy_down: heavy_down.play()
        elif normal_down: random.choice(normal_down).play()

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)
    if key in HEAVY_KEYS and heavy_up: heavy_up.play()
    elif normal_up: random.choice(normal_up).play()

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Minimal E İkonu
icon_pixmap = QPixmap(64, 64)
icon_pixmap.fill(Qt.transparent)
painter = QPainter(icon_pixmap)
painter.setRenderHint(QPainter.Antialiasing)
painter.setBrush(QColor(25, 25, 25))
painter.drawRoundedRect(2, 2, 60, 60, 16, 16)
painter.setPen(QColor(255, 255, 255))
font = painter.font()
font.setPointSize(28)
font.setBold(True)
painter.setFont(font)
painter.drawText(icon_pixmap.rect(), Qt.AlignCenter, "F")
painter.end()
app_icon = QIcon(icon_pixmap)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flack Pro")
        self.setFixedSize(320, 500)
        self.setWindowIcon(app_icon)
        self.setStyleSheet("background-color: #1c1c1e; color: white; font-family: 'Segoe UI';")
        
        layout = QVBoxLayout()
        
        title = QLabel("Switch Seçimi")
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin: 5px;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        self.buttons = []
        switch_folders = []
        if os.path.exists(SESLER_DIR):
            switch_folders = [d for d in os.listdir(SESLER_DIR) if os.path.isdir(os.path.join(SESLER_DIR, d))]
            
        for sf in switch_folders:
            display_name = sf.replace("-", " ").title()
            btn = QPushButton(display_name)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setCheckable(True)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2c2c2e; border-radius: 10px; padding: 12px; font-size: 14px; margin-bottom: 5px;
                }
                QPushButton:hover { background-color: #3a3a3c; }
                QPushButton:checked { background-color: #e5a93d; color: black; font-weight: bold; }
            """)
            btn.clicked.connect(lambda checked, folder=sf, button=btn: self.change_switch(folder, button))
            layout.addWidget(btn)
            self.buttons.append(btn)
            
        layout.addStretch()
        
        # Ses Seviyesi
        self.vol_label = QLabel("Ses Seviyesi: %100")
        self.vol_label.setAlignment(Qt.AlignCenter)
        self.vol_label.setStyleSheet("margin-top: 10px;")
        layout.addWidget(self.vol_label)
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(100)
        self.slider.setStyleSheet("""
            QSlider::groove:horizontal { height: 6px; background: #3a3a3c; border-radius: 3px; }
            QSlider::handle:horizontal { background: #e5a93d; width: 14px; margin: -4px 0; border-radius: 7px; }
        """)
        self.slider.valueChanged.connect(self.update_vol)
        layout.addWidget(self.slider)

        # Başlangıçta Çalıştır Checkbox'ı
        self.startup_cb = QCheckBox("Bilgisayar açıldığında otomatik başlat")
        self.startup_cb.setStyleSheet("""
            QCheckBox { margin-top: 15px; margin-bottom: 10px; font-size: 13px; color: #aaa; }
            QCheckBox::indicator { width: 18px; height: 18px; background-color: #2c2c2e; border-radius: 4px; }
            QCheckBox::indicator:checked { background-color: #e5a93d; border: 2px solid #e5a93d; image: url(); }
        """)
        self.startup_cb.setChecked(is_autostart_enabled())
        self.startup_cb.stateChanged.connect(self.toggle_startup)
        layout.addWidget(self.startup_cb, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
        
        if switch_folders and self.buttons:
            self.change_switch(switch_folders[0], self.buttons[0])

    def change_switch(self, folder, active_btn):
        for btn in self.buttons:
            if btn != active_btn:
                btn.setChecked(False)
        active_btn.setChecked(True)
        load_switch(folder)
        
    def update_vol(self, val):
        global current_volume
        self.vol_label.setText(f"Ses Seviyesi: %{val}")
        current_volume = val / 100.0
        for s in normal_down + normal_up: s.set_volume(current_volume)
        if heavy_down: heavy_down.set_volume(current_volume)
        if heavy_up: heavy_up.set_volume(current_volume)

    def toggle_startup(self, state):
        set_autostart(state == Qt.Checked)

window = MainWindow()

tray = QSystemTrayIcon(app_icon, app)
tray.setToolTip("Flack Pro")
menu = QMenu()
menu.setStyleSheet("QMenu { background-color: #2c2c2e; color: white; border: 1px solid #444; } QMenu::item:selected { background-color: #3a3a3c; }")

action_show = QAction("Arayüzü Göster")
action_show.triggered.connect(window.showNormal)
action_show.triggered.connect(window.activateWindow)
menu.addAction(action_show)

menu.addSeparator()

action_quit = QAction("Çıkış")
action_quit.triggered.connect(app.quit)
menu.addAction(action_quit)

tray.setContextMenu(menu)
tray.show()
window.show()

sys.exit(app.exec_())