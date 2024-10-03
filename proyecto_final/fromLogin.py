from fromTalentoHumano import*
from citas import *
import customtkinter as cs
from login import *
cs.set_default_color_theme("blue")
class logeo(cs.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x450")
        self.title("login")
        self.marco()
        self.etiquetas()
        self.botones()
        self.cajas()
        self.decoraciones()
        self.resizable(False, False)
        ## Conexión a la base de datos
        self.db_connection = coneccion_con_mongo("mongodb://localhost:27017")

    def botones(self):
        ##Boton iniciar sesion
        entrar = cs.CTkButton(self, text="Iniciar sesion",fg_color="#0056b3",command=self.guardar)
        entrar.configure(width=100,height=20)
        entrar.place(x=165,y=335)
        
        ##Boton para cambiar el ver o no ver la contraseña
        self.ver=cs.CTkButton(self, text="🔒",fg_color="#0056b3",text_color="white",command=self.ocultar_contraseña)
        self.ver.configure(width=10,height=1)
        self.ver.place(x=340,y=260)
        
    def guardar(self):
        usuario = self.cajausuario.get()
        contraseña = self.cajacontraseña.get()
        try:
            resultado = self.db_connection.comprobar_usuario(usuario, contraseña)

            
            if resultado == "usuario":
                ## Cierra la ventana de login
                self.destroy() 
                ## Crea una nueva ventana
                pacientes = cs.CTk()  
                ## ejecuta la ventana como ventana principal
                consulta = paciente(pacientes)  
                pacientes.mainloop()
                messagebox.showinfo("Éxito", "Iniciaste correctamente.")
            elif resultado == "superUsuario":
                
                self.destroy() 
                
                __name__ == "__main__"
                app = MainApp()
                app.mainloop()
                
                
                ##hola
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
        except Exception as e:
            print("Error:", e)

        
    def ocultar_contraseña (self):
        ##cget funciona para obtener el dato de show y saber si esta oculto o no
        
        if self.cajacontraseña.cget ("show")==("*"):
            self.cajacontraseña.configure(show="")
            self.ver.configure(text="🔓")
            
        else:
            self.cajacontraseña.configure(show="*")
            self.ver.configure(text="🔒")



    def etiquetas(self):
        ## Etiqueta usuario
        lblusuario = cs.CTkLabel(self, text="Usuario", font=("Arial", 14),fg_color="black",text_color="#0056b3")
        lblusuario.place(x=120, y=170)

        ## Etiqueta contraseña
        lblcontraseña = cs.CTkLabel(self, text="Contraseña", font=("Arial", 14),fg_color="black",text_color="#0056b3")
        lblcontraseña.place(x=120, y=230)
        ## Etiqueta bienvenido
        lblbienvenido= cs.CTkLabel(self, text="Bienvenido", font=("Arial", 30),fg_color="black",text_color="#0056b3")
        lblbienvenido.place(x=145, y=90)
        
    def cajas(self):
        # Caja para usuario
        self.cajausuario = cs.CTkEntry(self, placeholder_text="Ingrese su usuario", text_color="white", fg_color="#0056b3", font=("Arial", 14), width=200)
        self.cajausuario.place(x=120, y=200)

        ## Caja para contraseña
        self.cajacontraseña = cs.CTkEntry(self, placeholder_text="Ingrese su contraseña", text_color="white", fg_color="#0056b3", font=("Arial", 14), width=200,show="*")
        self.cajacontraseña.place(x=120, y=260)
        
    def marco(self):
        # Crear el marco con las dimensiones al inicio
        marco = cs.CTkFrame(self, fg_color="black", width=500, height=500)
        marco.configure(border_width=2,border_color="#0056b3")
        marco.place(x=0, y=0)
        
        
    def decoraciones(self):
        ##Primera linea horizontal    
        linea = cs.CTkFrame(self, fg_color="#0056b3", width=500, height=2)
        linea.place(x=10, y=60)
        ##Segundo linea horizontal
        linea1 = cs.CTkFrame(self, fg_color="#0056b3", width=500, height=2)
        linea1.place(x=10, y=380)
        
        

app=logeo()
app.mainloop()