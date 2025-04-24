from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog
)
import sys
from models.character import Character
from ui.window import charDisplay

def newChar(current_window):
    character = Character()
    current_window.close()
    charDisplay(character)

def importChar():
    file_path, _ = QFileDialog.getOpenFileName(None, "Importar Personagem", "", "Arquivos JSON (*.json)")
    if file_path:
        character = Character.load_from_file(file_path)
        charDisplay(character)

def main_menu():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Menu de Personagem")

    layout = QVBoxLayout()

    btn_new = QPushButton("Novo Personagem")
    btn_import = QPushButton("Importar Personagem")

    btn_new.clicked.connect(lambda: newChar(window))
    btn_import.clicked.connect(lambda: importChar(window))

    layout.addWidget(btn_new)
    layout.addWidget(btn_import)

    window.setLayout(layout)
    window.resize(300, 150)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main_menu()