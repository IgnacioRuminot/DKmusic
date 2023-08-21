#  En el entorno
#  pip install spotdl   
#  spotdl --download-ffmpeg
#  Las canciones se guardan dónde esté el archivo .py

import mysql.connector
from pathlib import Path
import subprocess   

#solo sirve con los enlaces de youtube_music y play list de yutube_music
#sirve con texto siendo especifico
#sirve para descargar de youtube una lista de reproducción creada en Spotify, usando el link de spotify

def descargar_lista_reproduccion(url_lista):
    ruta_escritorio = str(Path.home() / "Desktop")
    comando_spotdl = f'spotdl --playlist "{url_lista}" --output "{ruta_escritorio}"'
    subprocess.run(comando_spotdl, shell=True)

def descargar():
    if __name__ == "__main__":

        print('##solo sirve con los enlaces de youtube_music y play list de yutube_music#')
        print('##sirve con texto siendo especifico#')
        print('##sirve para descargar de youtube una lista de reproducción creada en Spotify, usando el link de spotify#')
        print(' ')
        link = input('Inserte link o nombre de la canción: ')
        url_lista_reproduccion = link    #Insertar enlace o texto aquí, entre las comillas
        descargar_lista_reproduccion(url_lista_reproduccion)
        print('')
        input("Presiona Enter para salir...")

descargar()

# # Configura la conexión a la base de datos
# db_connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="dkmusic"
# )

# # Crea un objeto cursor para ejecutar consultas
# cursor = db_connection.cursor()

# # Ejemplo de inserción de datos en la tabla de canciones
# song_data = ("Canción 1", "Artista 1", "Álbum 1", "Género", 2023)
# insert_query = "INSERT INTO canciones (titulo, artista, album, genero, anio) VALUES (%s, %s, %s, %s, %s)"
# cursor.execute(insert_query, song_data)

# # Confirma los cambios en la base de datos
# db_connection.commit()

# # Cierra el cursor y la conexión
# cursor.close()
# db_connection.close()

# descargar()

