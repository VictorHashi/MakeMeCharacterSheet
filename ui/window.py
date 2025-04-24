from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import sys

def charDisplay(character):
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle(f"Make me {character.name}")
    layout = QGridLayout()

    def create_stat_box(title, value):
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: #1e1e1e;
                border: 2px solid #9d4edd;
                border-radius: 10px;
                padding: 8px;
            }
            QLabel {
                color: white;
            }
        """)
        inner = QVBoxLayout()
        label_title = QLabel(title)
        label_title.setFont(QFont("Arial", 10))
        label_title.setAlignment(Qt.AlignCenter)
        label_value = QLabel(str(value))
        label_value.setFont(QFont("Arial", 22, QFont.Bold))
        label_value.setAlignment(Qt.AlignCenter)
        inner.addWidget(label_title)
        inner.addWidget(label_value)
        frame.setLayout(inner)
        return frame

    layout.addWidget(create_stat_box("FOR", f"{character.str} ({character.strMod})"), 0, 0)
    layout.addWidget(create_stat_box("DES", f"{character.dex} ({character.dexMod})"), 0, 1)
    layout.addWidget(create_stat_box("CON", f"{character.con} ({character.conMod})"), 0, 2)
    layout.addWidget(create_stat_box("INT", f"{character.int} ({character.intMod})"), 0, 3)
    layout.addWidget(create_stat_box("SAB", f"{character.wis} ({character.wisMod})"), 0, 4)
    layout.addWidget(create_stat_box("CAR", f"{character.cha} ({character.chaMod})"), 0, 5)

    layout.addWidget(create_stat_box("HP Máximo", character.maxhp), 2, 0)
    layout.addWidget(create_stat_box("CA", character.ac), 2, 1)
    layout.addWidget(create_stat_box("Deslocamento", f"{character.move} ft {character.move/5} Squares"), 2, 2)

    window.setLayout(layout)
    window.setStyleSheet("background-color: #121212;")
    window.resize(800, 600)
    window.show()

    window.append(window)

    if not QApplication.instance():
        app.exec()
