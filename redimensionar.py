#sirve para redimencionar le tamaño de una imagen de donde se encuentra este script
import PIL  # MODULO PARA PROCESAR IMAGENES
from PIL import Image
import os  # MODULO PARA HACER COSAS EN EL DIRECTORIO
import fnmatch  # MODULO PARA COMPARAR EXTENSIONES EN EL DIRECTORIO
import tarfile # MODULO PARA COMPRIMIR
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
current_dir = os.path.dirname(os.path.abspath(__file__)) # LEEMOS EL DIRECTORIO EN EL QUE ESTAMOS
lista_archivos = fnmatch.filter(os.listdir(current_dir), '*') 
lista_archivos_nopy = lista_archivos[:] # CLONAMOS LA LISTA ORIGINAL PARA ITERAR SOBRE ELLA
no_py = "redimensionar.py" 
for i in lista_archivos:
    if  no_py in i:
        lista_archivos_nopy.remove(i)
        
os.mkdir("nom_carpeta") #
os.chmod(current_dir + "/nom_carpeta", 0777) # LE DAMOS PERMISO DE ESCRITURA
tamano = input("Tamano: ") 
comprimir = raw_input("Desea comprimir las fotos?(si/no): ").lower()
 
for x in lista_archivos_nopy:
    img = Image.open(x)  
    width = img.size[0] # CHEQUEAMOS EL ANCHO
    heigh = img.size[1] # CHEQUEAMOS EL ALTO
    if width > heigh: # SI EL ANCHO ES MAYOR QUE EL ALTO (FOTO HORIZONTAL), LO TOMAMOS COMO REFERENCIA
        basewidth = tamano
        img = img.resize((basewidth, 400), PIL.Image.ANTIALIAS)
        img.save("nom_carpeta/" + x)  # SALVAMOS LA IMAGEN EN EL DIRECTORIO
        print x + " ---> OK!"  # IMPRIMIMOS UN . PARA QUE EL USUARIO NO SE DESESPERE Y QUE VEA EL PROCESO
 
    else: # SI EL ALTO ES MAYOR QUE EL ANCHO (FOTO VERTICAL) LO TOMAMOS COMO REFERENCIA
        baseheight = tamano
        img = img.resize((400, baseheight), PIL.Image.ANTIALIAS)
        img.save("nom_carpeta/" + x) # GUARDAMOS LA IMAGEN EN EL DIRECTORIO
        print x + " ---> OK!" # IMPRIMIMOS UN . PARA QUE EL USUARIO NO SE DESESPERE Y QUE VEA EL PROCESO
 
print ""
 
# COMPRIMIMOS LAS IMAGENES
if comprimir == "si" or comprimir == "s":
    os.chdir(current_dir + "/nom_carpeta") 
    lista_archivos_comprimir = fnmatch.filter(os.listdir(os.getcwd()), '*')
    tar = tarfile.open("images.tar.gz", "w:gz")
    for name in lista_archivos_comprimir:
        tar.add(name)
    tar.close()
    os.chmod("images.tar.gz", 0777)
    print "Fotos comprimidas"
 
 
print "FIN" 
