from pymongo import MongoClient
import customtkinter as ctk
import tkinter as tk
from tkinter import*
 
ctk.set_appearance_mode("dark")  # Modo de apariencia
ctk.set_default_color_theme("blue")  # Tema de color

# Conectar a la base de datos
client = MongoClient('mongodb://localhost:27017/')
db = client['pacientes']
collection = db['pacientes']

class paciente(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill='both', expand=True)
        self.pestañas()
        self.etiquetas()
        self.cajas()
        self.botones()
        
    def pestañas(self):  
        # crea el ctkview principal
        self.tabview1 = ctk.CTkTabview(self, width=600, height=450)
        self.tabview1.pack(expand=True, fill='both')
        
        self.tabview1.add('Paciente')
        #añadir pestañas dentro de las pestañas principales
        #Pestañas de paciente
        self.paciente = ctk.CTkTabview(self.tabview1.tab('Paciente'), width=600, height=450)
        self.paciente.pack(expand=True, fill='both')
        self.paciente.add('Informacion del paciente')
        self.paciente.add('Historial Medico')
        self.paciente.add('Habitos/Estilo De Vida')
        
    def etiquetas(self):
        #PESTAÑA DE PACIENTE
        #Etiquetas de informacion del paciente
        self.nombres = ctk.CTkLabel(self.paciente.tab('Informacion del paciente'), text= 'Nombre(s)')
        self.nombres.place(x=20, y=40)
        self.apellidos = ctk.CTkLabel(self.paciente.tab('Informacion del paciente'), text= 'Apellido(s)')
        self.apellidos.place(x=20, y=80)
        self.FechaNacimiento = ctk.CTkLabel(self.paciente.tab('Informacion del paciente'), text= 'Fecha de nacimiento')
        self.FechaNacimiento.place(x=20, y=120)
        self.Genero = ctk.CTkLabel(self.paciente.tab('Informacion del paciente'), text= 'Genero')
        self.Genero.place(x=20, y=160)
        self.ocupacion = ctk.CTkLabel(self.paciente.tab('Informacion del paciente'), text= 'Ocupacion')
        self.ocupacion.place(x=20, y=200)
        self.Telefono = ctk.CTkLabel(self.paciente.tab('Informacion del paciente'), text= 'Telefono')
        self.Telefono.place(x=20, y=240)
        self.Email = ctk.CTkLabel(self.paciente.tab('Informacion del paciente'), text= 'Email')
        self.Email.place(x=20, y=280)
        self.Direccion = ctk.CTkLabel(self.paciente.tab('Informacion del paciente'), text= 'Direccion')
        self.Direccion.place(x=20, y=320)
        
        #Etiquetas de historial medico
        self.enfermedad=ctk.CTkLabel(self.paciente.tab('Historial Medico'), text= 'Enfermedad')
        self.enfermedad.place(x=20, y=40)
        self.Fecha_diagnostico=ctk.CTkLabel(self.paciente.tab('Historial Medico'), text= 'Fecha Diagnostico')
        self.Fecha_diagnostico.place(x=20, y=110)
        self.Tratamiento=ctk.CTkLabel(self.paciente.tab('Historial Medico'), text= 'Tratamiento')
        self.Tratamiento.place(x=20, y=180)
        self.Comentarios=ctk.CTkLabel(self.paciente.tab('Historial Medico',), text= 'Comentarios')
        self.Comentarios.place(x=20, y=250)
        
        #Etiquetas Habitos/Estilo de vida
        self.Habito=ctk.CTkLabel(self.paciente.tab('Habitos/Estilo De Vida'), text= 'Tipo de Habito')
        self.Habito.place(x=20, y=40)
        self.Frecuencia=ctk.CTkLabel(self.paciente.tab('Habitos/Estilo De Vida'), text= 'Frecuencia')
        self.Frecuencia.place(x=20, y=130)
        self.comentariosH=ctk.CTkLabel(self.paciente.tab('Habitos/Estilo De Vida'), text= 'Comentarios')
        self.comentariosH.place(x=20, y=220)
        
    def cajas(self):
        #Cajas de paciente
        self.txt_nombre=ctk.CTkEntry(self.paciente.tab('Informacion del paciente'), width=300, height=20)
        self.txt_nombre.place(x=180, y=40)
        self.txt_apellido=ctk.CTkEntry(self.paciente.tab('Informacion del paciente'), width=300, height=20)
        self.txt_apellido.place(x=180, y=80)
        self.cbx_Fecha_n=ctk.CTkEntry(self.paciente.tab('Informacion del paciente'), width=300, height=20)
        self.cbx_Fecha_n.place(x=180, y=120)
        self.cbx_genero=ctk.CTkEntry(self.paciente.tab('Informacion del paciente'), width=300, height=20)
        self.cbx_genero.place(x=180, y=160)
        self.txt_ocupacion=ctk.CTkEntry(self.paciente.tab('Informacion del paciente'), width=300, height=20)
        self.txt_ocupacion.place(x=180, y=200)
        self.txt_telefono=ctk.CTkEntry(self.paciente.tab('Informacion del paciente'), width=300, height=20)
        self.txt_telefono.place(x=180, y=240)
        self.txt_email=ctk.CTkEntry(self.paciente.tab('Informacion del paciente'), width=300, height=20)
        self.txt_email.place(x=180, y=280)
        self.txt_direccion=ctk.CTkEntry(self.paciente.tab('Informacion del paciente'), width=300, height=20)
        self.txt_direccion.place(x=180, y=320)
        
        #cajas de historial medico
        self.enfermedad_entry = ctk.CTkTextbox(self.paciente.tab('Historial Medico'), width=300, height=55)
        self.enfermedad_entry.place(x=150, y=40)
        self.Fecha_diagnostico_entry = ctk.CTkTextbox(self.paciente.tab('Historial Medico'), width=300, height=55)
        self.Fecha_diagnostico_entry.place(x=150, y=110)
        self.Tratamiento_entry = ctk.CTkTextbox(self.paciente.tab('Historial Medico'), width=300, height=55)
        self.Tratamiento_entry.place(x=150, y=180)
        self.Comentarios_entry = ctk.CTkTextbox(self.paciente.tab('Historial Medico'), width=300, height=55)
        self.Comentarios_entry.place(x=150, y=250)
        
        # cajas de texto habitos/estilo de vida
        self.Habito_entry = ctk.CTkTextbox(self.paciente.tab('Habitos/Estilo De Vida'), width=300, height=55)
        self.Habito_entry.place(x=150, y=40)
        self.Frecuencia_entry = ctk.CTkTextbox(self.paciente.tab('Habitos/Estilo De Vida'), width=300, height=55)
        self.Frecuencia_entry.place(x=150, y=130)
        self.comentariosH_entry = ctk.CTkTextbox(self.paciente.tab('Habitos/Estilo De Vida'), width=300, height=55)
        self.comentariosH_entry.place(x=150, y=220)
        
    def guardar_datos(self):
        # Recopilar datos desde las cajas de texto
        paciente_data = {
            'nombres': self.txt_nombre.get(),
            'apellidos': self.txt_apellido.get(),
            'fechaNacimiento': self.cbx_Fecha_n.get(),
            'genero': self.cbx_genero.get(),
            'ocupacion': self.txt_ocupacion.get(),
            'telefono': self.txt_telefono.get(),
            'email': self.txt_email.get(),
            'direccion': self.txt_direccion.get(),
            'historialMedico': {
                'enfermedad': self.enfermedad_entry.get('1.0', 'end').strip(),
                'fechaDiagnostico': self.Fecha_diagnostico_entry.get('1.0', 'end').strip(),
                'tratamiento': self.Tratamiento_entry.get('1.0', 'end').strip(),
                'comentarios': self.Comentarios_entry.get('1.0', 'end').strip(),
            },
            'habitosEstiloVida': {
                'habito': self.Habito_entry.get('1.0', 'end').strip(),
                'frecuencia': self.Frecuencia_entry.get('1.0', 'end').strip(),
                'comentarios': self.comentariosH_entry.get('1.0', 'end').strip(),
            }
        }
        
        # Guardar los datos en MongoDB
        collection.insert_one(paciente_data)
        print('Datos del paciente guardados con éxito')
    
    def botones(self):
        # Botón para guardar los datos
        self.btn_guardar = ctk.CTkButton(self.paciente, text='Guardar', fg_color='#99FF8B', text_color='black', command=self.guardar_datos)
        self.btn_guardar.place(x=220, y=400)
        
        # Botón para salir (por ejemplo, cerrar la ventana)
        self.btn_salir = ctk.CTkButton(self.paciente, text='Salir', fg_color='#FF464C', text_color='black', command=self.master.quit)
        self.btn_salir.place(x=420, y=400)

        
        


