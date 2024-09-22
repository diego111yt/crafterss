from tkinter import messagebox
from pymongo import MongoClient

class coneccion_con_mongo:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client["prueba"]

    def comprobar_usuario(self, username, password):
        # Verificar en la colección "prueba"
        collection = self.db["prueba"]
        user = collection.find_one({"usuario": username, "contraseña": password})

        if user is not None:
            resultado="usuario"
            return resultado
        # Verificar en la colección "superUsuario"
        collection_super = self.db["superUsuario"]
        super_user = collection_super.find_one({"usuario": username, "contraseña": password})

        if super_user is not None:
            resultado="superUsuario"
            return resultado# Indica que es un super usuario

        return None  # Usuario no encontrado
    