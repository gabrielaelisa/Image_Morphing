
## Supuestos
- las imágenes son reescaladas a un formato 256*256, con el propósito de
de que la ejecución no demore tanto
- por este motivo las líneas de correspondencia deben estar en el dominio x,y -> 256,256
## Información útil
- todas los archivos de líneas son provistos

## Cómo Correr
- situarse en la carpeta root del proyecto "T3"

- ejecutar los siguientes comandos:  

caso1
      ``
    python3 main.py caso1/red_apple.jpg caso1/dragon_fruit.jpg caso1/lines.txt N
    ``
caso2:
  ``
    python3 main.py caso2/orange.jpg caso2/pineapple.jpg caso2/lines.txt N
    ``
    
caso3:
  ``
    python3 main.py caso3/dog.jpg caso3/lion.jpg caso3/lines.txt N
    ``
donde N es el número de imágenes intermedias deseadas