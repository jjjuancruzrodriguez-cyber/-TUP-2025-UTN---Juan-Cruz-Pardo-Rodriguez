import sys
import mysql.connector
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QLabel, QPushButton, QMainWindow
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class VentanaAlumnos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Lista de Alumnos")
        self.resize(700, 600)

        self.filas_por_pagina = 10
        self.pagina_actual = 0

        contenedor = QWidget()
        layout = QVBoxLayout()

        # ESTILOS 
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f7fa;
            }

            QLabel#titulo {
                font-size: 20px;
                font-weight: bold;
                color: #333;
                margin-bottom: 10px;
            }

            QTableWidget {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
            }

            QHeaderView::section {
                background-color: #3f51b5;
                color: white;
                font-weight: bold;
                padding: 5px;
            }

            QPushButton {
                background-color: #3f51b5;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #5c6bc0;
            }

            QPushButton:disabled {
                background-color: #aaa;
                color: #eee;
            }
        """)

        # TÍTULO 
        self.titulo = QLabel("Alumnos registrados en la base de datos")
        self.titulo.setObjectName("titulo")
        self.titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.titulo)

        # TABLA 
        self.tabla = QTableWidget()
        layout.addWidget(self.tabla)

        # BOTONES 
        botones_layout = QHBoxLayout()
        botones_layout.addStretch()

        self.boton_anterior = QPushButton("Anterior")
        self.boton_siguiente = QPushButton("Siguiente")
        self.boton_anterior.clicked.connect(self.anterior_pagina)
        self.boton_siguiente.clicked.connect(self.siguiente_pagina)

        botones_layout.addWidget(self.boton_anterior)
        botones_layout.addSpacing(25)
        botones_layout.addWidget(self.boton_siguiente)

        layout.addLayout(botones_layout)

        # CONTENEDOR 
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        self.cargar_datos()

    def cargar_datos(self):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="maitena34",
                database="escuela"
            )

            cursor = conexion.cursor()

            cursor.execute("SELECT COUNT(*) FROM alumnos")
            total_filas = cursor.fetchone()[0]
            self.total_paginas = (total_filas + self.filas_por_pagina - 1) // self.filas_por_pagina

            offset = self.pagina_actual * self.filas_por_pagina
            cursor.execute("SELECT nombre, apellido, telefono, dni FROM alumnos LIMIT %s OFFSET %s",
                           (self.filas_por_pagina, offset))
            resultados = cursor.fetchall()

            self.tabla.setRowCount(len(resultados))
            self.tabla.setColumnCount(4)
            self.tabla.setHorizontalHeaderLabels(["Nombre", "Apellido", "Teléfono", "DNI"])

            for fila_idx, fila in enumerate(resultados):
                for col_idx, valor in enumerate(fila):
                    item = QTableWidgetItem(str(valor))
                    item.setFlags(Qt.ItemIsEnabled)  # Solo lectura
                    self.tabla.setItem(fila_idx, col_idx, item)

            cursor.close()
            conexion.close()

            # Actualizar botones
            self.boton_anterior.setEnabled(self.pagina_actual > 0)
            self.boton_siguiente.setEnabled(self.pagina_actual < self.total_paginas - 1)

            # Actualizar tulo con página actual
            self.titulo.setText(f" Página {self.pagina_actual + 1} de {self.total_paginas}")

        except mysql.connector.Error as err:
            self.titulo.setText(f" Error al conectar con la base de datos: {err}")

    def siguiente_pagina(self):
        if self.pagina_actual < self.total_paginas - 1:
            self.pagina_actual += 1
            self.cargar_datos()

    def anterior_pagina(self):
        if self.pagina_actual > 0:
            self.pagina_actual -= 1
            self.cargar_datos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaAlumnos()
    ventana.show()
    sys.exit(app.exec_())
