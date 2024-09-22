from pymongo import MongoClient
import customtkinter as ctk
from tkinter import messagebox, ttk

# Conectar a la base de datos
client = MongoClient('mongodb://localhost:27017/')
db = client['pacientes']
collection = db['registro_paciente']

# Lista de opciones para los menús desplegables
TIPOS_DOCUMENTO = ["CC", "CE", "PA", "RC", "TI", "AS", "MS"]
EPS_COLOMBIA = ["Sura", "Sanitas", "Coomeva", "Salud Total"]
TIPOS_SANGRE = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
GENEROS = ["Masculino", "Femenino", "Otro"]
ESTADO_CIVIL = ["Soltero", "Casado", "Union Libre", "Viudo", "Puto"]

class Paciente(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.registro()
        self.botones()

        
        
    def registro (self):
        
        self.title("Registro Paciente")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, weight=1)
        
        self.labeldoc = ctk.CTkLabel(self, text="Tipo Documento", font=("Arial", 16))
        self.labeldoc.grid(row=0, column=0)
        self.combo_tipo_doc = ttk.Combobox(self, values=TIPOS_DOCUMENTO, state="readonly")
        self.combo_tipo_doc.grid(row=0, column=1, padx=10, pady=5)


        self.labelnum = ctk.CTkLabel(self, text="Numero de Documento", font=("Arial", 16))
        self.labelnum.grid(row=0, column=2)
        self.entry_nro_doc = ctk.CTkEntry(self)
        self.entry_nro_doc.grid(row=0, column=3, padx=10, pady=5)

        self.labelnom1 = ctk.CTkLabel(self, text="Primer Nombre", font=("Arial", 16))
        self.labelnom1.grid(row=1, column=0)
        self.entry_nombre1 = ctk.CTkEntry(self)
        self.entry_nombre1.grid(row=1, column=1, padx=10, pady=5)


        self.labelnom2 = ctk.CTkLabel(self, text="Segundo Nombre", font=("Arial", 16))
        self.labelnom2.grid(row=1, column=2)
        self.entry_nombre2 = ctk.CTkEntry(self)
        self.entry_nombre2.grid(row=1, column=3, padx=10, pady=5)


        self.labelape1 = ctk.CTkLabel(self, text="Primer Apellido", font=("Arial", 16))
        self.labelape1.grid(row=2, column=0)
        self.entry_apellido1 = ctk.CTkEntry(self)
        self.entry_apellido1.grid(row=2, column=1, padx=10, pady=5)


        self.labelape2 = ctk.CTkLabel(self, text="Segundo Apellido", font=("Arial", 16))
        self.labelape2.grid(row=2, column=2)
        self.entry_apellido2 = ctk.CTkEntry(self)
        self.entry_apellido2.grid(row=2, column=3, padx=10, pady=5)


        self.labelfenac = ctk.CTkLabel(self, text="Fecha de Nacimiento", font=("Arial", 16))
        self.labelfenac.grid(row=3, column=0)
        self.entry_fecha_nacimiento = ctk.CTkEntry(self)
        self.entry_fecha_nacimiento.grid(row=3, column=1, padx=10, pady=5)


        label_genero = ctk.CTkLabel(self, text="Género:", font=("Arial", 16))
        label_genero.grid(row=3, column=2)
        self.combo_genero = ttk.Combobox(self, values=GENEROS, state="readonly")
        self.combo_genero.grid(row=3, column=3, padx=10, pady=5)

        self.labelrh = ctk.CTkLabel(self, text="Tipo de Sangre", font=("Arial", 16))
        self.labelrh.grid(row=4, column=0)
        self.combo_rh = ttk.Combobox(self, values=TIPOS_SANGRE, state="readonly")
        self.combo_rh.grid(row=4, column=1, padx=10, pady=5)


        self.labeldir = ctk.CTkLabel(self, text="Direccion", font=("Arial", 16))
        self.labeldir.grid(row=4, column=2)
        self.entry_dir = ctk.CTkEntry(self)
        self.entry_dir.grid(row=4, column=3, padx=10, pady=5)


        self.labelemail = ctk.CTkLabel(self, text="Correo Electronico", font=("Arial", 16))
        self.labelemail.grid(row=5, column=0)
        self.entry_email = ctk.CTkEntry(self)
        self.entry_email.grid(row=5, column=1, padx=10, pady=5)


        self.labeltel= ctk.CTkLabel(self, text="Telefono", font=("Arial", 16))
        self.labeltel.grid(row=5, column=2)
        self.entry_tel = ctk.CTkEntry(self)
        self.entry_tel.grid(row=5, column=3, padx=10, pady=5)


        self.labeleps = ctk.CTkLabel(self, text="EPS:", font=("Arial", 16))
        self.labeleps.grid(row=6, column=0)
        self.combo_eps = ttk.Combobox(self, values=EPS_COLOMBIA, state="readonly")
        self.combo_eps.grid(row=6, column=1, padx=10, pady=5)


        self.label527 = ctk.CTkLabel(self, text="Etnia", font=("Arial", 16))
        self.label527.grid(row=6, column=2)
        self.entry_527 = ctk.CTkEntry(self)
        self.entry_527.grid(row=6, column=3, padx=10, pady=5)

        self.labelpobres = ctk.CTkLabel(self, text="Poblacion Especial", font=("Arial", 16))
        self.labelpobres.grid(row=7, column=0)
        self.entry_pobres = ctk.CTkEntry(self)
        self.entry_pobres.grid(row=7, column=1, padx=10, pady=5)


        self.labelespecial = ctk.CTkLabel(self, text="Discapacidad", font=("Arial", 16))
        self.labelespecial.grid(row=7, column=2)
        self.entry_especial = ctk.CTkEntry(self)
        self.entry_especial.grid(row=7, column=3, padx=10, pady=5)


        self.labelocup = ctk.CTkLabel(self, text="Ocupacion", font=("Arial", 16))
        self.labelocup.grid(row=8, column=0)
        self.entry_ocup = ctk.CTkEntry(self)
        self.entry_ocup.grid(row=8, column=1, padx=10, pady=5)


        self.labelestcivil= ctk.CTkLabel(self, text="Estado Civil", font=("Arial", 16))
        self.labelestcivil.grid(row=8, column=2)
        self.combo_estcivil = ttk.Combobox(self, values=ESTADO_CIVIL, state="readonly")
        self.combo_estcivil.grid(row=8, column=3, padx=10, pady=5)
            

        

    def guardar_datos(self):
         
        paciente_data = {
            'Tipo Documento': self.combo_tipo_doc.get(),
            'Numero de Documento': self.entry_nro_doc.get(),
            'Primer Nombre': self.entry_nombre1.get(),
            'Segundo Nombre': self.entry_nombre2.get(),
            'Primer Apellido': self.entry_apellido1.get(),
            'Segundo Apellido': self.entry_apellido2.get(),
            'Fecha de Nacimiento': self.entry_fecha_nacimiento.get(),
            'Genero': self.combo_genero.get(),
            'Tipo de Sangre': self.combo_rh.get(),
            'Direccion': self.entry_dir.get(),
            'Correo Electronico': self.entry_email.get(),
            'Telefono': self.entry_tel.get(),
            'EPS': self.combo_eps.get(),
            'Etnia': self.entry_527.get(),
            'Poblacion Especial': self.entry_pobres.get(),
            'Discapacidad': self.entry_especial.get(),
            'Ocupacion':self.entry_ocup.get(),
            'Estado civil':self.combo_estcivil.get()
        }

        collection.insert_one(paciente_data)
        print('Los datos se guardaron con exito')
    
            # Campo de entrada para nombre del paciente
            #self.nombre_entry = ctk.CTkEntry(self, placeholder_text="Nombre")
        # self.nombre_entry.pack(pady=10)

            # Botón para mostrar en consola (simulación de guardado)
    #     self.guardar_btn = ctk.CTkButton(self, text="Guardar", command=self.guardar_nombre)
    #     self.guardar_btn.pack(pady=10)

    def botones(self):
        self.button_add_patient = ctk.CTkButton(self, text="Agregar Paciente", command=self.guardar_datos)
        self.button_add_patient.grid(row=9, column=0, columnspan=4, pady=10)


