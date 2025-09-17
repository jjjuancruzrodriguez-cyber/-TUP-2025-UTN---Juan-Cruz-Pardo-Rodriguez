import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QLabel, QLineEdit, 
                             QPushButton, QTextEdit, QComboBox, QMessageBox,
                             QFileDialog, QGroupBox, QListWidget, QSplitter, QListWidgetItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class SistemaDocentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión de Docentes")
        self.setGeometry(780, 320 , 1000, 800)
        
        
        self.archivo_datos = "docentes.txt"
        
        
        self.configurar_interfaz()
        self.cargar_datos_iniciales()
        
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                margin: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 10px 0 10px;
                color: #495057;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #004085;
            }
            QLineEdit, QComboBox {
                padding: 8px;
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
            QLineEdit:focus, QComboBox:focus {
                border-color: #007bff;
            }
            QListWidget {
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
            QTextEdit {
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
        """)

    def configurar_interfaz(self):
        """Configurar la interfaz principal"""
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)
        
        
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        
        
        panel_izquierdo = self.crear_panel_formulario()
        splitter.addWidget(panel_izquierdo)
        
       
        panel_derecho = self.crear_panel_lista()
        splitter.addWidget(panel_derecho)
        
        
        splitter.setSizes([400, 600])

    def crear_panel_formulario(self):
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # COMPLETAR: Crear grupo de formulario
        grupo_form = QGroupBox("Datos del Docente")
        form_layout = QGridLayout()
        
        # COMPLETAR: Crear campos del formulario
        self.legajo_edit = QLineEdit()
        self.legajo_edit.setPlaceholderText("Ingrese su legajo aqui")
        form_layout.addWidget(QLabel("Legajo:"), 0, 0)
        form_layout.addWidget(self.legajo_edit, 0, 1)

        self.nombre = QLineEdit()
        self.nombre.setPlaceholderText("Ingrese tu nombre aqui")
        form_layout.addWidget(QLabel("Nombre:"), 1, 0)
        form_layout.addWidget(self.nombre, 1, 1)

        self.apellido = QLineEdit()
        self.apellido.setPlaceholderText("Ingrese su apellido aqui")
        form_layout.addWidget(QLabel("Apellido:"), 2, 0)
        form_layout.addWidget(self.apellido, 2, 1)

        self.DNI = QLineEdit()
        self.DNI.setPlaceholderText("Ingrese su DNI aqui")
        form_layout.addWidget(QLabel("DNI:"), 3, 0)
        form_layout.addWidget(self.DNI, 3, 1)

        self.email = QLineEdit()
        self.email.setPlaceholderText("Ingrese su email aqui")
        form_layout.addWidget(QLabel("Email:"), 4, 0)
        form_layout.addWidget(self.email, 4, 1)

        self.telefono = QLineEdit()
        self.telefono.setPlaceholderText("Ingrese su telefono aqui")
        form_layout.addWidget(QLabel("Telefono:"), 5, 0)
        form_layout.addWidget(self.telefono, 5, 1)
        
        self.materia = QLineEdit()
        self.materia.setPlaceholderText("Ingrese la materia aqui")
        form_layout.addWidget(QLabel("Materia:"), 6, 0)
        form_layout.addWidget(self.materia, 6, 1)
        
        
        
        self.lista_desplegable = QComboBox()
        self.lista_desplegable.addItems(["Titular", "Asociado", "Adjunto", "Auxiliar", "Interino"])
        form_layout.addWidget(QLabel("Categoría:"), 7, 0)
        form_layout.addWidget(self.lista_desplegable, 7, 1)
        
        grupo_form.setLayout(form_layout)
        layout.addWidget(grupo_form)
        
        grupo_botones = QGroupBox("Acciones")
        botones_layout = QVBoxLayout()
        
        self.btn_agregar = QPushButton("Agregar Docente")
        self.btn_agregar.clicked.connect(self.agregar_docente)
        botones_layout.addWidget(self.btn_agregar)

        self.btn_buscar = QPushButton("Buscar Docente")
        self.btn_buscar.clicked.connect(self.buscar_docente)
        botones_layout.addWidget(self.btn_buscar)

        self.btn_modificar = QPushButton("Modificar Docente")
        self.btn_modificar.clicked.connect(self.modificar_docente)
        botones_layout.addWidget(self.btn_modificar)

        self.btn_eliminar = QPushButton("Eliminar Docente")
        self.btn_eliminar.clicked.connect(self.eliminar_docente)
        botones_layout.addWidget(self.btn_eliminar)

        self.btn_limpiar = QPushButton("Limpiar")
        self.btn_limpiar.clicked.connect(self.limpiar)
        form_layout.addWidget(self.btn_limpiar)
        
    
        grupo_botones.setLayout(botones_layout)
        layout.addWidget(grupo_botones)
        
        widget.setLayout(layout)
        return widget

    def nombre_input():
        return input("Ingrese el nombre: ")
    
    def apellido_input():
        return input("Ingrese el apellido")

    def agregar_docente(self):
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        categoria = self.categoria_combo.currentText()

        if not nombre or not apellido or categoria == "Seleccione...":
            QMessageBox.warning(self, "Pifeaste", "Completa todos los campos pa.")
            return

        self.docentes.append({"nombre": nombre, "apellido": apellido, "categoria": categoria})
        QMessageBox.information(self, "Joya", "Agregaste al docente mi rey.")
        self.limpiar_formulario()

    def buscar_docente(self):
        apellido = self.apellido_input.text()
        if not apellido:
            QMessageBox.warning(self, "Erraste", "Ingresa un apellido para buscar.")
            return

        for docente in self.docentes:
            if docente["apellido"].lower() == apellido.lower():
                self.nombre_input_text.setText(docente["nombre"])
                self.apellido_input.setText(docente["apellido"])
                index = self.categoria_combo.findText(docente["categoria"])
                if index != -1:
                    self.categoria_combo.setCurrentIndex(index)
                QMessageBox.information(self, "Encontrado", "Docente encontrado y cargado en el formulario.")
                return

        QMessageBox.warning(self, "No se encontro pa", "Ingresa un docente que tengamos registrado mostri.")

    def modificar_docente(self):
        apellido = self.apellido_input.text()
        for docente in self.docentes:
            if docente["apellido"].lower() == apellido.lower():
                docente["nombre"] = self.nombre_input.text()
                docente["categoria"] = self.categoria_combo.currentText()
                QMessageBox.information(self, "Felicidades pa", "Docente modificado correctamente.")
                return
        QMessageBox.warning(self, "Troleaste", "Ese docente no esta registrado, cono.")

    def eliminar_docente(self):
        apellido = self.apellido_input.text()
        for docente in self.docentes:
            if docente["apellido"].lower() == apellido.lower():
                self.docentes.remove(docente)
                QMessageBox.information(self, f"De cheto", "Eliminamos al insoportable de {apellido}.")
                self.limpiar_formulario()
                return
        QMessageBox.warning(self, "Erraste", "No se encontró el docente para eliminar.")

    def limpiar(self):
        self.nombre_input.clear()
        self.apellido_input.clear()
        self.categoria_combo.setCurrentIndex(0)
    
    def crear_panel_lista(self):
        widget = QWidget()
        layout = QVBoxLayout()

        buscar = QHBoxLayout()
        buscar.addWidget(QLabel("Buscar:"))
        self.busqueda_edit = QLineEdit()
        self.busqueda_edit.setPlaceholderText("Buscar por apellido, nombre o legajo...")
        self.busqueda_edit.textChanged.connect(self.filtrar_lista)
        buscar.addWidget(self.busqueda_edit)
        layout.addLayout(buscar)

        self.lista_docentes = QListWidget()
        self.lista_docentes.itemClicked.connect(self.mostrar_detalles)
        layout.addWidget(self.lista_docentes)

        grupo_detalles = QGroupBox("Detalles del Docente Seleccionado")
        self.detalles_text = QTextEdit()
        self.detalles_text.setReadOnly(True)
        self.detalles_text.setMaximumHeight(200)
        detalles_layout = QVBoxLayout()
        detalles_layout.addWidget(self.detalles_text)
        grupo_detalles.setLayout(detalles_layout)
        layout.addWidget(grupo_detalles)
        
        widget.setLayout(layout)
        return widget
    
    
    def cargar_datos_iniciales(self):
        if not os.path.exists(self.archivo_datos):
            self.crear_datos_ejemplo()
            return
        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:  
                        datos = linea.split('|')
                        if len(datos) == 8:  
                            self.agregar_a_lista(datos)
                        else:
                            print(f"Línea con formato incorrecto: {linea}")
            
            print(f"Se cargaron {self.lista_docentes.count()} docentes")
        
        except Exception as e:
            QMessageBox.critical(self, 'Error al cargar', 
                               f'No se pudieron cargar los datos:\n{str(e)}')
    
    
    def guardar_todos_los_datos(self):
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as archivo:
                for i in range(self.lista_docentes.count()):
                    item = self.lista_docentes.item(i)
                    datos = item.data(Qt.UserRole)
                    linea = '|'.join(datos) + '\n'
                    archivo.write(linea)
            print("Datos guardados correctamente")
        except Exception as e:
            QMessageBox.critical(self, 'Error al guardar',
                               f'No se pudieron guardar los datos:\n{str(e)}')

    
    
    def crear_datos_ejemplo(self):
        """Crear archivo con datos de ejemplo"""
        datos_ejemplo = [
            "DOC001|Juan|Pérez|12345678|juan.perez@universidad.edu|123456789|Matemática|Titular",
            "DOC002|María|González|87654321|maria.gonzalez@universidad.edu|987654321|Física|Adjunto",
            "DOC003|Carlos|Rodríguez|11223344|carlos.rodriguez@universidad.edu|456789123|Química|Asociado",
            "DOC004|Ana|López|55667788|ana.lopez@universidad.edu|789123456|Historia|Auxiliar",
            "DOC005|Pedro|Martínez|99887766|pedro.martinez@universidad.edu|321654987|Inglés|Interino"]
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as archivo:
                for linea in datos_ejemplo:
                    archivo.write(linea + '\n')
            
            for linea in datos_ejemplo:
                datos = linea.split('|')
                self.agregar_a_lista(datos)
            
            QMessageBox.information(self, 'Datos de ejemplo', 
                                  'Se crearon datos de ejemplo para empezar')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'No se pudo crear el archivo:\n{str(e)}')

    def agregar_docente(self):
        if not self.legajo_edit.text().strip():
            QMessageBox.warning(self, 'Error', 'El legajo es obligatorio')
            self.legajo_edit.setFocus()
            return
        
        if not self.nombre_edit.text().strip():
            QMessageBox.warning(self, 'Error', 'El nombre es obligatorio')
            self.nombre_edit.setFocus()
            return
        
        if not self.apellido_edit.text().strip():
            QMessageBox.warning(self, 'Error', 'El apellido es obligatorio')
            self.apellido_edit.setFocus()
            return
        
        
        legajo = self.legajo_edit.text().strip().upper()
        if self.buscar_por_legajo(legajo):
            QMessageBox.warning(self, 'Error', 
                              f'Ya existe un docente con el legajo {legajo}')
            return
        
        
        email = self.email_edit.text().strip()
        if email and '@' not in email:
            QMessageBox.warning(self, 'Error', 'Escribi bien el email hermano')
            return
        
        
        datos = [
            legajo,
            self.nombre_edit.text().strip(),
            self.apellido_edit.text().strip(),
            self.dni_edit.text().strip(),
            email,
            self.telefono_edit.text().strip(),
            self.materia_edit.text().strip(),
            self.categoria_combo.currentText()
        ]
        
        
        self.agregar_a_lista(datos)
        self.guardar_todos_los_datos()
        self.limpiar_formulario()
        QMessageBox.information(self, 'Éxito', 
                              f'Docente {datos[1]} {datos[2]} se agregaron piola')
    
    def buscar_por_legajo(self, legajo):
        """Buscar si existe un legajo en la lista"""
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            if datos[0].upper() == legajo.upper():
                return item
        return None
    
    def buscar_docente(self):
        """Buscar y seleccionar docente por legajo"""
        legajo = self.legajo_edit.text().strip()
        if not legajo:
            QMessageBox.warning(self, 'Error', 'Ingresa un legajo para buscar bobo')
            return
        
        item = self.buscar_por_legajo(legajo)
        if item:
            self.lista_docentes.setCurrentItem(item)
            self.mostrar_detalles(item)
            self.lista_docentes.scrollToItem(item)
        else:
            QMessageBox.information(self, 'No se encontro bro', 
                                  f'No se encontró docente con legajo: {legajo}')
    
    def modificar_docente(self):
        """Modificar el docente seleccionado"""
        item_actual = self.lista_docentes.currentItem()
        if not item_actual:
            QMessageBox.warning(self, 'Error', 
                              'Seleccione un docente de la lista para modificar')
            return
        
        # Cargar datos en el formulario
        datos = item_actual.data(Qt.UserRole)
        self.legajo_edit.setText(datos[0])
        self.nombre_edit.setText(datos[1])
        self.apellido_edit.setText(datos[2])
        self.dni_edit.setText(datos[3])
        self.email_edit.setText(datos[4])
        self.telefono_edit.setText(datos[5])
        self.materia_edit.setText(datos[6])
        
        # Seleccionar categoría en el combo
        index = self.categoria_combo.findText(datos[7])
        if index >= 0:
            self.categoria_combo.setCurrentIndex(index)
        
        # Cambiar el botón para actualizar
        self.btn_agregar.setText("Actualizar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(lambda: self.actualizar_docente(item_actual))
        
        QMessageBox.information(self, 'Modo edición', 
                              'Modifique los datos y presione "Actualizar Docente"')
    
    def actualizar_docente(self, item):
        """Actualizar los datos del docente"""
        # Validar igual que en agregar
        if not self.nombre_edit.text().strip() or not self.apellido_edit.text().strip():
            QMessageBox.warning(self, 'Error', 'Nombre y apellido son obligatorios')
            return
        
        # Obtener datos actualizados
        nuevos_datos = [
            self.legajo_edit.text().strip().upper(),
            self.nombre_edit.text().strip(),
            self.apellido_edit.text().strip(),
            self.dni_edit.text().strip(),
            self.email_edit.text().strip(),
            self.telefono_edit.text().strip(),
            self.materia_edit.text().strip(),
            self.categoria_combo.currentText()
        ]
        
        # Actualizar el item
        item.setData(Qt.UserRole, nuevos_datos)
        item.setText(f"{nuevos_datos[2]}, {nuevos_datos[1]} ({nuevos_datos[0]})")
        
        # Guardar cambios
        self.guardar_todos_los_datos()
        
        # Restaurar botón agregar
        self.btn_agregar.setText("Agregar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(self.agregar_docente)
        
        self.limpiar_formulario()
        QMessageBox.information(self, 'Éxito', 'Docente actualizado correctamente')
    
    def eliminar_docente(self):
        """Eliminar el docente seleccionado"""
        item_actual = self.lista_docentes.currentItem()
        if not item_actual:
            QMessageBox.warning(self, 'Error', 
                              'Seleccione un docente de la lista para eliminar')
            return
        
        
        datos = item_actual.data(Qt.UserRole)
        respuesta = QMessageBox.question(
            self, 'Confirmar eliminación',
            f'¿Está seguro de eliminar a {datos[1]} {datos[2]} (Legajo: {datos[0]})?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            
            row = self.lista_docentes.row(item_actual)
            self.lista_docentes.takeItem(row)
            
            
            self.guardar_todos_los_datos()
            
            
            self.detalles_text.clear()
            self.limpiar_formulario()
            
            QMessageBox.information(self, 'Éxito', 'Docente eliminado correctamente')



    def agregar_a_lista(self, datos):
        """Agregar un docente a la lista visual"""
        
        texto_item = f"{datos[2]}, {datos[1]}, ({datos[0]})"
        
        
        item = QListWidgetItem(texto_item)
        item.setData(Qt.UserRole, datos)  
        
        
        self.lista_docentes.addItem(item)
    
    def filtrar_lista(self):
        """Filtrar la lista según el texto de búsqueda"""
        texto_busqueda = self.busqueda_edit.text().lower()
        
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            
            
            coincide = (texto_busqueda in datos[0].lower() or  # legajo
                       texto_busqueda in datos[1].lower() or   # nombre
                       texto_busqueda in datos[2].lower())     # apellido
            
            
            item.setHidden(not coincide)
    
    def mostrar_detalles(self, item):
        """Mostrar detalles del docente seleccionado"""
        datos = item.data(Qt.UserRole)
        
        detalles = f"""INFORMACIÓN DEL DOCENTE
{'='*40}

Legajo:     {datos[0]}
Nombre:     {datos[1]}
Apellido:   {datos[2]}
DNI:        {datos[3]}
Email:      {datos[4]}
Teléfono:   {datos[5]}
Materia:    {datos[6]}
Categoría:  {datos[7]}

{'='*40}
Seleccione "Modificar" o "Eliminar" para editar este registro."""
        
        self.detalles_text.setPlainText(detalles)
    
    def limpiar_formulario(self):
       
        self.legajo_edit.clear()
        self.nombre_edit.clear()
        self.apellido_edit.clear()
        self.dni_edit.clear()
        self.email_edit.clear()
        self.telefono_edit.clear()
        self.materia_edit.clear()
        self.categoria_combo.setCurrentIndex(0)
        
        
        self.btn_agregar.setText("Agregar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(self.agregar_docente)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    sistema = SistemaDocentes()
    sistema.show()
    sys.exit(app.exec_())

    
        












