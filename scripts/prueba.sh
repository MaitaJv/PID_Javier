#!/bin/sh -e

# Ruta donde se ubican los archivos a eliminar por antiguedad
cd /home/user/Documentos/archivosDePrueba

# Aclaracion para el usuario
# informando que al ingresar <y> confirma la eliminacion de archivo encontrado
echo "  y   - para eliminar el archivo seleccionado"
echo "ENTER - para omitir archivo"

# filtrado de archivos por tiempo de modificacion con confirmacion
# | find |    |-type f|              |-mtime +20|     |   -ok   |
find -type f -mtime +30 -ok rm {} \;

#Comentar la linea superior y descomentar la inferior para dejar de esperar
#confirmacion por parte del usuario

#find -type f -mtime +30 -exec rm {} \;
