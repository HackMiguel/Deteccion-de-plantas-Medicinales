import numpy as np
import time
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras.initializers import glorot_uniform
from keras.utils import CustomObjectScope
import sys
import os

longitud, altura = 150, 150
modelo = '/home/angel/Escritorio/ProyectoFinal/modelo/modelo.h5'
pesos_modelo = '/home/angel/Escritorio/ProyectoFinal/modelo/pesos.h5'

with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        cnn = load_model(modelo)
#cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)
def met(anwer, py):
	os.system('python3 /home/angel/Escritorio/ProyectoFinal/Audio/'+py)
	f = open('hola.txt','w')
	letra = str(anwer)
	f.write(letra)
	f.close()
	sys.exit()


	#os.system('python3 /home/aaa/Escritorio/ProyectoFinal/camara.py')
def predict(file):
	x = load_img(file, target_size=(longitud, altura))
	x = img_to_array(x)
	x = np.expand_dims(x, axis=0)
	array = cnn.predict(x)
	result = array[0]
	answer = np.argmax(result)
	if answer == 0:
		planta = ""
		info = ""
		print("prediccion: Commelina")
		print(array[0])
	if answer == 1:
		planta = ""
		info = ""
		print("prediccion: 2")
		print(array[0])
	elif answer == 2:
		planta = "Arnica"
		info = "Estimula el sistema nervioso \n Es util en lesiones externas por golpes(alivia el dolor y favorece la curacion) \n puede usarse para mejorar la circulacion coronaria y funcion  cardiaca"
		print("prediccion: Arnica")
		print(array[0])
	elif answer == 3:
		planta = "Bugambilia"
		info = "Acelera la cicatrizacion \n Disminuyte la tos seca \n Ayuda a bajar la fiebre \n Mejora el sistema respiratorio \n Favorece le cuidado de la piel"
		print("prediccion: Bugambilia")
		print(array[0])
	elif answer == 4:
		planta = ""
		info = ""
		print("prediccion: 5")
		print(array[0])
	elif answer == 5:
		planta = "Flor de Calabaza"
		info = "Fortalece el sistema inmunologico y evita el resfriado comun \n Mejora los niveles de colesterol \n Mejora la presion arterial \n Disminuye el riesgo de enfermedades cardiovasculares \n Ayuda a matener los huesos y dientes fuertes y sanos"
		print("prediccion: Flor de calabaza")
		print(array[0])
	elif answer == 6:
		planta = "Nopal"
		info = "Recomendado para las personas que sufren diabetes pues reduce los niveles de azucar en la sangre \n Ayuda al proceso digestivo\n Previene del cancer"
		print("prediccion: Nopal")
		print(array[0])
	elif answer == 7:
		planta = "Diente de Leon"
		info = "Se conoce como pis-en-lit, en alusion a sus propiedades diureticas \n Se utiliza para transtornos digestivos leves \n Aumenta la cantidad de orina y limpia las vias urinarias"
		print("prediccion: Diente de leon")
		print(array[0])
	elif answer == 8:
		planta = ""
		info = "El jugo de las hojas, sirve para curar enfermedades del higado y el bazo \n Ayuda en la prevencion de enfermedades como el cancer y tratar cicatrizaciones. \n Purificara el aire, debido a que transforma el dioxido de carbono (CO2) en Oxigeno (O2)"
		print("prediccion: Lengua de Suegra")
		print(array[0])
	elif answer == 9:
		planta = "Malva"
		info = "Las malvas tienen propiedades antiinflamatorias, laxantes,\n cicatrizantes, calmantes, digestivas y expectorantes"
		print("prediccion: Malva")
		print(array[0])
	elif answer == 10:
		planta = "Manzanilla"
		info = "Tata los problemas digestivos como vomito,gastritis,indigestion,colicos,bilis e infeccion del estomago. \n Es un remedio para eliminar el acne,la deshidratacion,el reumatismo,aclarar el cabello y lavar heridas superficiales"
		print("prediccion: Manzanilla") #sabila nopal2
		print(array[0])
	elif answer == 11:
		planta = ""
		info = ""
		print("prediccion: 12")
		print(array[0])
	elif answer == 12:
		planta = "Ruda"
		info = "Alivia el dolor de oido \n Es utilizado para limpiar ulceras,para le lavado bucal \n Se emplea como locion para masajear el cuero cabelludo"
		print("prediccion: Ruda")
		print(array[0])
	elif answer == 13:
		planta = "Sabila"
		info = "El aloe vera es una planta medicinal muy popular que se usa en las industrias cosmetica, farmaceutica y alimentaria. Sus hojas estan llenas de un gel que contiene numerosos compuestos beneficiosos."
		print("prediccion: Sabila")
		print(array[0])
	elif answer == 14:
		planta = "Zanahoria"
		info = "A nivel cardiovascular : Las semillas son utilizadas como complementario de tratamientos para la hipertension. \n Para la digestion : Es recomendada la infusion de las semillas para aliviar los dolores estomacales causados por una mala digestion o inclusive para la flatulencia."
		print("prediccion: Zanahoria")
		print(array[0])
	return (planta,info)
#predict('pruebas/sabila56.jpg')
		
#diente de leon -> por hierba buena
#hierba de sapo -> a Ajenjo
#sabila por diente de leon