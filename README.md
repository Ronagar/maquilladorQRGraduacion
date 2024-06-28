# Script de creación de tickets para la graduación

Este script sirve para añadir los códigos QR de las entradas a tickets más estéticos. 

## Funcionamiento 

Cuenta con dos imágenes base para crear los tickets: `EntradaTipo1.png` y `EntradaTipo2.png`. Para utilizar una u otra comentar y descomentar las líneas correspondientes a la declaración de la variable `entrada` (líneas 8 y 9). 

El script busca dentro de la ruta proporcionada en la variable `ruta_graduados` (por defecto la ruta actual del script) subdirectorios asociados a los graduados que contienen los códigos QR utilizados para validar las entradas. Crea los tickets de salida en una carpeta `Entradas` situada en el directorio anterior al actual. 
Los tickets se agruparán en directorios con el mismo nombre que cada directorio que contenga los QR que servirá también de identificador para incluir el graduado en el ticket. 

Para ejecutar el script, se debe ajustar la ruta al directorio de los graduados o incluir los archivos del proyecto en el directorio en cuestión. Comando en terminal:

`python ticketGenerator.py`
