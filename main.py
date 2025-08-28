# Importa el módulo os para interactuar con el sistema de archivos
import os

# Obtiene la lista de archivos en el directorio actual
archivos = os.listdir(".") 
i = 0 

# Bucle para recorrer todos los archivos de la carpeta actual
print("LISTA DE ARCHIVOS MARKDOWN")
print("-------------------------")
while i < len(archivos):
    # Obtiene el nombre del archivo actual
    archivo = archivos[i]
    # Comprueba si el archivo tiene extensión '.md'
    if archivo.endswith(".md"):
        print(archivo)
    i += 1