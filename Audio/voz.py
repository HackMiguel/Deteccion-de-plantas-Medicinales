from gtts import gTTS
from playsound import playsound
from gtts import gTTS

NOMBRE_ARCHIVO = "sonido_generado.mp3"
tts = gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python prueba de audio.', lang='es-us')
# Nota: podriamos llamar directamente a save
with open(NOMBRE_ARCHIVO, "wb") as archivo:
    tts.write_to_fp(archivo)

playsound(NOMBRE_ARCHIVO)
