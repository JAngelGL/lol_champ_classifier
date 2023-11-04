import cv2
import os

# Directorio donde se encuentran los videos
directorio_videos = "C:/Users/drago/Videos/Champ Clips"

# Obtén la lista de archivos en el directorio
archivos_videos = os.listdir(directorio_videos)

# Itera sobre cada archivo de video
for archivo_video in archivos_videos:
    # Obtén el nombre del video sin la extensión
    nombre_sin_extension = os.path.splitext(archivo_video)[0]
    
    # Crea una subcarpeta con el mismo nombre que el archivo de video
    subcarpeta = os.path.join(directorio_videos, nombre_sin_extension)
    os.makedirs(subcarpeta, exist_ok=True)
    print("La capeta ",nombre_sin_extension, " ha sido creada")
    
    # Abre el archivo de video
    video = cv2.VideoCapture(os.path.join(directorio_videos, archivo_video))
    
    # Obtén la frecuencia de cuadros por segundo (FPS) del video
    fps = int(video.get(cv2.CAP_PROP_FPS))
    
    # Itera sobre cada cuadro del video
    frame_count = 0
    while True:
        ret, frame = video.read()
        
        # Si no se puede leer más cuadros, sal del bucle
        if not ret:
            break
        
        # Si el número del cuadro es múltiplo de 10, guárdalo en la subcarpeta
        if frame_count % 1 == 0:
            frame_filename = os.path.join(subcarpeta, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
        
        frame_count += 1
    
    # Cierra el archivo de video
    video.release()

print("Proceso completado.")
