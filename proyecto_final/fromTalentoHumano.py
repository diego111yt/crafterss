import customtkinter as ctk
from persomedic import Persomedic
from paciente import Paciente 

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Registro")
        self.geometry("600x400")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

# Menú lateral a la izquierda
# self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
# self.sidebar_frame.grid(row=0, column=1, sticky="nsew", rowspan=2)

        # Botones del menú
        self.medico_button = ctk.CTkButton(self, text="Registro Médico", command=self.mostrar_persomedic)
        self.medico_button.grid(row=0, column=0)

        self.paciente_button = ctk.CTkButton(self, text="Registro Paciente", command=self.mostrar_paciente)
        self.paciente_button.grid(row=1, column=0)

        # Área de contenido para las ventanas
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=0, column=1, sticky="nsew", rowspan=2)

    def mostrar_persomedic(self):
        persomedic=Persomedic()
        persomedic.mainloop()

    def mostrar_paciente(self):
        paciente=Paciente()
        paciente.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
