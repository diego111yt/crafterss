import customtkinter as cs
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

        
        
        
    def botones(self):
        ##Boton iniciar sesion
        entrar = cs.CTkButton(self, text="Iniciar sesion",fg_color="#0056b3")
        entrar.configure(width=100,height=20)
        entrar.place(x=165,y=335)
        
        ##Boton para cambiar el ver o no ver la contraseña
        self.ver=cs.CTkButton(self, text="🔒",fg_color="#0056b3",text_color="white",command=self.ocultar_contraseña)
        self.ver.configure(width=10,height=1)
        self.ver.place(x=340,y=260)
        
        
    def ocultar_contraseña (self):
        ##variable para saber si esta oculto o no el texto
        
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
        cajausuario = cs.CTkEntry(self, placeholder_text="Ingrese su usuario", text_color="white", fg_color="#0056b3", font=("Arial", 14), width=200)
        cajausuario.place(x=120, y=200)

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

        linea1 = cs.CTkFrame(self, fg_color="#0056b3", width=500, height=2)
        linea1.place(x=10, y=380)
        
        

app=logeo()
app.mainloop()