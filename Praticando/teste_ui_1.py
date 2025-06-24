import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QLabel, QPushButton, QTextEdit, QHBoxLayout,
                             QLineEdit, QStatusBar)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configurações básicas da janela
        self.setWindowTitle("Aplicativo PyQt6 Bonito")
        self.setWindowIcon(QIcon("icon.png"))  # Coloque seu ícone aqui
        self.setGeometry(100, 100, 600, 400)
        
        # Widget central e layout principal
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        layout_principal = QVBoxLayout(widget_central)
        
        # Estilo global
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                color: #333333;
                font-size: 16px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QTextEdit {
                background-color: black;
                border: 2px solid #cccccc;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
        """)
        
        # Cabeçalho
        cabecalho = QLabel("Bem-vindo ao Meu Aplicativo!")
        cabecalho.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        cabecalho.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cabecalho.setStyleSheet("color: #2c3e50; margin: 20px 0;")
        
        # Área de texto
        self.texto_edit = QTextEdit()
        self.texto_edit.setPlaceholderText("Digite algo aqui...")
        
        # Botões
        botoes_layout = QHBoxLayout()
        
        btn_estilo = """
            QPushButton {
                padding: 12px 24px;
                border-radius: 8px;
                font-weight: bold;
                min-width: 120px;
            }
        """
        
        btn_salvar = QPushButton("Salvar")
        btn_salvar.setStyleSheet(btn_estilo + """
            QPushButton {
                background-color: #3498db;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        
        btn_limpar = QPushButton("Limpar")
        btn_limpar.setStyleSheet(btn_estilo + """
            QPushButton {
                background-color: #e74c3c;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        
        btn_sair = QPushButton("Sair")
        btn_sair.setStyleSheet(btn_estilo + """
            QPushButton {
                background-color: #2ecc71;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        
        botoes_layout.addWidget(btn_salvar)
        botoes_layout.addWidget(btn_limpar)
        botoes_layout.addWidget(btn_sair)
        
        # Campo de entrada
        self.entrada = QLineEdit()
        self.entrada.setPlaceholderText("Digite e pressione Enter...")
        self.entrada.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                font-size: 14px;
            }
        """)
        
        # Barra de status
        self.barra_status = QStatusBar()
        self.setStatusBar(self.barra_status)
        self.barra_status.showMessage("Pronto", 3000)
        
        # Adicionar widgets ao layout principal
        layout_principal.addWidget(cabecalho)
        layout_principal.addWidget(self.texto_edit)
        layout_principal.addLayout(botoes_layout)
        layout_principal.addWidget(self.entrada)
        layout_principal.addStretch()
        
        # Conectar sinais
        btn_limpar.clicked.connect(self.limpar_texto)
        btn_sair.clicked.connect(self.close)
        self.entrada.returnPressed.connect(self.mostrar_texto)
        
    def limpar_texto(self):
        self.texto_edit.clear()
        self.barra_status.showMessage("Texto limpo com sucesso!", 2000)
        
    def mostrar_texto(self):
        texto = self.entrada.text()
        self.texto_edit.append(f"Você digitou: {texto}")
        self.entrada.clear()
        self.barra_status.showMessage("Texto adicionado!", 2000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())