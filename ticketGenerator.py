import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Configuración
ruta_graduados = '.'  # Ruta a la carpeta principal de graduados
nombre_evento = 'Graduación ETSI Informática 2024'
#entrada = './EntradaTipo1.png'
entrada = './EntradaTipo2.png'
fuente = 'arial.ttf'  
tamaño_fuente = 20

# Función para generar ticket
def generar_ticket(nombre_alumno, ruta_qr, numero, nombre_archivo):
    # Abrir la imagen base y preparar para dibujar
    imagen = Image.open(entrada) 
    imagen = imagen.resize((800, 300))
    draw = ImageDraw.Draw(imagen)
    

    # Cargar y colocar el código QR
    qr = Image.open(ruta_qr)
    qr = qr.resize((190, 190))  
    imagen.paste(qr, (570, 55))
    
    # Agregar texto
    fuente_obj = ImageFont.truetype(fuente, tamaño_fuente)
    draw.text((115, 145), f'{nombre_alumno}', fill='white', font=fuente_obj) # graduado
    #draw.text((93, 186), f'{nombre_archivo}', fill='white', font=fuente_obj) # nombre invitado
    draw.text((93, 185), f'{numero}', fill='white', font=fuente_obj) # numero invitado
    
    # Guardar la imagen
    nombre_archivo = f'../Entradas/{nombre_alumno}/{nombre_alumno}_ticket{numero}.png'
    imagen.save(nombre_archivo)
    print(f'Ticket guardado como {nombre_archivo}')

# Recorrer los directorios de graduados
for nombre_alumno in os.listdir(ruta_graduados):
    ruta_alumno = os.path.join(ruta_graduados, nombre_alumno)
    if os.path.isdir(ruta_alumno):
        #Creacion de la ruta de salida de las entradas
        Path('../Entradas/'+nombre_alumno).mkdir(parents=True, exist_ok=True)

        contador = 1
        for archivo in os.listdir(ruta_alumno):
            if archivo.endswith('.png'):
                ruta_qr = os.path.join(ruta_alumno, archivo)
                generar_ticket(nombre_alumno, ruta_qr, contador, archivo[0:-4])
                contador += 1
            
                
