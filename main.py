from os import path, makedirs, listdir
import shutil


'''-------------------Definiendo constantes-------------------'''
DOCUMENTOS_EXTENSIONES = [".pdf",".txt",".doc",".docx",".html",".xml",".odt",".xls",".xlsx",".ods",".ptt",".pptx",".tex"]
IMAGENES_EXTENSIONES = [".jpg",".jpeg",".png",".bmp",".ico",".svg",".webp"]
VIDEOS_EXTENSIONES = [".mp4",".mkv",".flv",".gif",".avi",".m4v",".mpeg",".svi",".webm"]
COMPRIMIDOS_EXTENSIONES = [".7z",".rar",".tar",".zip",".gz",".bz2",".deb",".apk"]

PATH = path.expanduser('~')
DESCARGAS_PATH = path.join(PATH,"Descargas")
DOCUMENTOS_PATH = path.join(PATH,"Documentos")
IMAGENES_PATH = path.join(PATH,"Imágenes")
VIDEOS_PATH = path.join(PATH,"Vídeos")
COMPRIMIDOS_PATH = path.join(DESCARGAS_PATH,"comprimidos")


'''-------------------      Algoritmo       -------------------'''
#chequeo que existe la ruta de archivos comprimidos y si no la creo
def organizar():
    if not path.exists(path.join(PATH,"Descargas/comprimidos")):
       makedirs(path.join(PATH,"Descargas/comprimidos"))

    #bisco los archivos en descargas
    ARCHIVOS = listdir(DESCARGAS_PATH)

    #uno por uno veo qué tipo de archivo son y los muevo a las carpetas corresponientes
    for archivo in ARCHIVOS:
        nombre, tipo = path.splitext(archivo)
        dir_actual = path.join(DESCARGAS_PATH,archivo)
        # archivo = "'"+archivo+"'"

        if tipo in DOCUMENTOS_EXTENSIONES:
            dir_destino = path.join(DOCUMENTOS_PATH,archivo)
            shutil.move(dir_actual,dir_destino)
        
        if tipo in IMAGENES_EXTENSIONES:
            dir_destino = path.join(IMAGENES_PATH,archivo)
            shutil.move(dir_actual,dir_destino)

        if tipo in VIDEOS_EXTENSIONES:
            dir_destino = path.join(VIDEOS_PATH,archivo)
            shutil.move(dir_actual,dir_destino)
        
        if tipo in COMPRIMIDOS_EXTENSIONES:
            dir_destino = path.join(COMPRIMIDOS_PATH,archivo)
            shutil.move(dir_actual,dir_destino)


#main file
if __name__ == "__main__":
    organizar()
