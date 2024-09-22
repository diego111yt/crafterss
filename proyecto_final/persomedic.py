from pymongo import MongoClient
import customtkinter as ctk
from tkinter import messagebox, ttk

# Conectar a la base de datos
client = MongoClient('mongodb://localhost:27017/')
db = client['pacientes']
collection = db['registro_doctor']

# Lista de opciones para los menús desplegables

ESPECIALIDAD= ['Oncología Pediátrica', 'Cardiología Pediátrica', 'Dermatología Pediátrica', 'Gastroenterología Pediátrica', 'Neurología Pediátrica', 'Pediatría del Desarrollo', 'Oftalmología Pediátrica', 'Psiquiatría Infantil', 'Traumatología Pediátrica', 'Endocrinología Pediátrica']

class Persomedic(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.registro()
        self.botones()
        
    def registro(self):

            self.title("Registro Personal Medico")
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=1)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=1)
            self.rowconfigure(2, weight=1)
            self.rowconfigure(3, weight=1)
            self.rowconfigure(4, weight=1)
            self.rowconfigure(5, weight=1)
            self.rowconfigure(6, weight=1)


            self.labeldocmed = ctk.CTkLabel(self, text="Documento Medico", font=("Arial", 16))
            self.labeldocmed.grid(row=0, column=0, padx=10, pady=5)
            self.entry_docmed = ctk.CTkEntry(self)
            self.entry_docmed.grid(row=0, column=1, padx=10, pady=5)


            self.label = ctk.CTkLabel(self, text="Nombre", font=("Arial", 16))
            self.label.grid(row=1, column=0, padx=10, pady=5)
            self.entry_nombre = ctk.CTkEntry(self)
            self.entry_nombre.grid(row=1, column=1, padx=10, pady=5)
            

            self.apellido_entry = ctk.CTkLabel(self, text="Apelidos", font=("Arial", 16))
            self.apellido_entry.grid(row=2, column=0, padx=10, pady=5)
            self.entry_apellido = ctk.CTkEntry(self)
            self.entry_apellido.grid(row=2, column=1, padx=10, pady=5)
            
            self.labelesp = ctk.CTkLabel(self, text="Especialidad", font=("Arial", 16))
            self.labelesp.grid(row=3, column=0)
            self.combo_especialidad = ttk.Combobox(self, values=ESPECIALIDAD, state="readonly")
            self.combo_especialidad.grid(row=3, column=1, padx=10, pady=5)


            self.labeltel = ctk.CTkLabel(self, text="Telefono", font=("Arial", 16))
            self.labeltel.grid(row=4, column=0, padx=10, pady=5)
            self.entry_tel = ctk.CTkEntry(self)
            self.entry_tel.grid(row=4, column=1, padx=10, pady=5)
            


            self.labelemail = ctk.CTkLabel(self, text="Correo", font=("Arial", 16))
            self.labelemail.grid(row=5, column=0, padx=10, pady=5)
            self.entry_email = ctk.CTkEntry(self)
            self.entry_email.grid(row=5, column=1, padx=10, pady=5)
            
            
        
        
    def guardar_datos(self):
        
        doctor_data = {
            'documento': self.entry_docmed.get(),
            'nombre': self.entry_nombre.get(),
            'apellido': self.entry_apellido.get(),
            'especialidad': self.combo_especialidad.get(),
            'telefono': self.entry_tel.get(),
            'email': self.entry_email.get(),
        }
        # Guardar los datos en MongoDB
        collection.insert_one(doctor_data)
        print('Datos del doctor guardados correctamente')
     

    def botones(self):
        self.guardar_btn = ctk.CTkButton(self, text="Guardar", command=self.guardar_datos)
        self.guardar_btn.grid(row=6, column=0, padx=10, pady=5, columnspan=2)
