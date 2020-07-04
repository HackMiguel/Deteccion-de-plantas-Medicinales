import sys
import cv2
import time

x=0;

"""while True:
	f = open('hola.txt','r')
	mensaje = f.read()
	f.close()
	if(mensaje=='1'):
		f = open('hola.txt','w')
		f.write('0')
		sys.exit()
		
	camara = 0
		
	fotogramas = 1
	
	camera = cv2.VideoCapture(camara)
		
	def get_image():
		retval, im = camera.read()
		return im
		
	for i in range(fotogramas):
		temp = get_image()
		
	print("Listo")
		
	camera_capture = get_image()
	file = "foto.jpg"
	
	cv2.imwrite(file, camera_capture)
	del(camera)
	time.sleep(3)"""

f = open('hola.txt','r')
mensaje = f.read()
f.close()
if(mensaje=='1'):
	f = open('hola.txt','w')
	f.write('0')
	sys.exit()
	
camara = 0
	
fotogramas = 1
	
camera = cv2.VideoCapture(camara)
		
def get_image():
	retval, im = camera.read()
	return im
		
for i in range(fotogramas):
	temp = get_image()
		
print("Listo")
		
camera_capture = get_image()
file = "image.jpg"
	
cv2.imwrite(file, camera_capture)
del(camera)
