import cv2
import sys
import numpy as np

# modos de ejecusion
#vc = 0 --> 48 captura de video
#fd = 1 --> 49 filtro desenonque
#fe = 2 --> 50 filtro detector de esquinas
#fb = 3 --> 51 filtro de bordes

# parametros para detectar esquinas
esquinas_param = dict(maxCorners = 500, #maximo de numero de esquinas a detectar
                      qualityLevel =0.2, #umbral minimo
                      minDistance =15, #Distancia entre esquinas
                      blockSize   =9)
# Modo
mood = 48

# Creamos la video captura
cap = cv2.VideoCapture(0)

#creamos un ciclo para ejecutar nuestros Frames
while True:
    # Leemos los fotogramas
    ret, frame = cap.read()

    # decidir mod
    # Normal
    if mood == 48:
        #mostrar frames
        resultado = frame

    # Desenfoque
    elif mood == 49:
        #modificar frames
        resultado = cv2.blur(frame,(13,13))

    elif mood == 51:
        resultado = cv2.Canny(frame, 135, 150)

    elif mood == 50:
        # Obtenemos los frames
        resultado = frame
        # Conversion a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Calculamos las caracteristicas de las esquinas
        esquinas = cv2.goodFeaturesToTrack(gray, **esquinas_param)

        # Preguntamos si detectamos esquinas con esas caracteristicas
        if esquinas is not None:
            # Iteramos
            for x, y in np.float32(esquinas).reshape(-1,2):
                #convertimos en enteros
                x,y = int(x), int(y)
                # Dibujamos la ubicacion de las esquinas
                cv2.circle(resultado,(x,y), 10, (0,0,255), 1)

    # Si presionamos otra tecla
    elif mood != 48 or mood != 49 or mood !=50 or mood != 51 or mood != -1:
        # No hacemos nada
        resultado = frame

        #imprimimos mensaje
        print("TECLA INCORRECTA")

    # Mostramos los Frames
    resultado = cv2.flip(resultado,1)
    cv2.imshow("VIDEO CAPTURA", resultado)

    # leyendouna tecla
    t = cv2.waitKey(1)
    if t == 27:
        break

    #Modificamos mood
    elif t != -1:
        mood = t

cap.release()
cv2.destroyAllWindows()