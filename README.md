
## Supuestos
- las imágenes son reescaladas a un formato 256*256, con el propósito de
 que la ejecución no demore tanto
- por este motivo las líneas de correspondencia deben estar en el dominio x,y -> 256,256
## Información útil
- todas los archivos de líneas son provistos, el formato es x1, y1, x2, y2, x1', y1' ,x2', y2'  
donde x corresponde a columna, e y a fila en los ejes matriciales.  
 Además no se numeran las líneas en el archivo. 
- por cada imagen intermedia el algoritmo toma alrededor de 2 minutos
- mientras más imágenes intermedias deseadas, más demora el código

## Cómo Correr
- situarse en la carpeta root del proyecto "T3"

- ejecutar los siguientes comandos: 

``
    python3 <path to src_image> <path to dest image> <path to lines file> <Number of steps>
    `` 

#### caso1

     
  ``
    python3 main.py caso1/red_apple.jpg caso1/dragon_fruit.jpg caso1/lines.txt 3
    ``
#### caso2:
  ``
    python3 main.py caso2/orange.jpg caso2/pineapple.jpg caso2/lines.txt 3
    ``
    
#### caso3:
  ``
    python3 main.py caso3/dog.jpg caso3/lion.jpg caso3/lines.txt 3
    ``
#### caso4:
   ``
    python3 main.py caso4/peluche.jpg caso4/perro.jpg caso4/lines.txt 3
    ``
- donde N es el número de imágenes intermedias deseadas

## Resultados:
 los resultados aparecerán en el directorio results