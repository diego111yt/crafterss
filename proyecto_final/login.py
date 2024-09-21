from tkinter import messagebox
from pymongo import MongoClient

class coneccion_con_mongo:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client["prueba"]  # Asegúrate de poner el nombre correcto aquí

    def comprobar_usuario(self, username, password):
        collection = self.db["prueba"]  # Asegúrate de que esta colección exista
        user = collection.find_one({"usuario": username, "contraseña": password})
        return user is not None

    def iniciar_sesion(self, username, password):
        if self.comprobar_usuario(username, password):
            messagebox.showinfo("Éxito", "Iniciaste correctamente.")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
