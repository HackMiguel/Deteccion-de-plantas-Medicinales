import Tkinter 
import Tkinter, Tkconstants, tkFileDialog
from PIL import Image, ImageTk
import cv2
from predecir import *

dirImagen=''

root = Tkinter.Tk()
root.geometry("550x600")
root.resizable(width=True, height=True)
#Abrir la ubicacion de la imagen y colocarlo en le frame
def openfn():
    filename = tkFileDialog.askopenfilename(title='open')
    return filename
def open_img():
    x = openfn()
    global dirImagen
    img = Image.open(x)
    img = img.resize((350, 350), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Tkinter.Label(root, image=img)
    panel.image = img
    panel.place(x=100,y=60)
    dirImagen=x

#capturar foto por medio de video
def video():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('Tomar Foto',frame)#gray
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("foto.jpg", frame)
            open_foto()
            break
    cap.release()
    cv2.destroyAllWindows()
    pass
def open_foto():
    x = "foto.jpg"
    global dirImagen
    img = Image.open(x)
    img = img.resize((350, 350), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Tkinter.Label(root, image=img)
    panel.image = img
    panel.place(x=100,y=60)
    dirImagen=x
#obtener la informacion del objeto que se detecto y colocarlo en un label dentro del frame
def direcImagen():
    (planta,info)=predict(dirImagen)
    return (planta,info)
def analizarImg():
    planta=''
    (planta,info)=direcImagen()
    panel = Tkinter.Label(root, text=planta)
    panel.place(x=200,y=460)
    panel.config(bg="white") #Cambiar color de fondo
    panel.config(font=('Arial', 18)) #Cambiar tipo y tamano de fuente
    panel = Tkinter.Label(root, text=info)
    panel.place(x=80,y=510)

#Tkinter.Button(root, text='Abrir Imagen', command=open_img).grid(row=0, column=0)
Tkinter.Button(root, text='Abrir Imagen', command=open_img,bg="#3352ff", fg="#ffffff").place(x=110,y=5)
Tkinter.Button(root, text='Tomar Foto', command=video,bg="#3352ff", fg="#ffffff").place(x=240,y=5)
Tkinter.Button(root, text="Cerrar",command=root.quit,bg="#3352ff", fg="#ffffff").place(x=370,y=5)
Tkinter.Button(root, text="Analizar",command=analizarImg).place(x=230,y=420)
#texto
root.mainloop()