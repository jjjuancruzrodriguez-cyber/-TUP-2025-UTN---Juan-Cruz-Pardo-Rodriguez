import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout,QPushButton
from PyQt5.QtCore import Qt
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        self.label_email = QLabel("Email:")
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Ingrese su email")
        
        self.label_pass = QLabel("Contraseña:")
        self.input_pass = QLineEdit()
        self.input_pass.setPlaceholderText("Ingrese su contraseña")
        self.input_pass.setEchoMode(QLineEdit.Password)

        self.boton_login = QPushButton("Ingresar")
        self.boton_login.clicked.connect(self.login)

        layout.addWidget(self.label_email,0, 0, alignment=Qt.AlignLeft)
        layout.addWidget(self.input_email,0, 1)

        layout.addWidget(self.label_pass, 1, 0, alignment = Qt.AlignRight)
        layout.addWidget(self.input_pass, 1, 1)

        layout.addWidget(self.boton_login, 2, 0, 1, 2, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def login(self):
        email = self.input_email.text()
        password = self.input_pass.text()
        print(f"email: {email}, Password: {password}")
        self.label_email.setText(f"Bienvenido: {email}")


app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec_())