import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

detectaMao = mp.solutions.hands
maos = detectaMao.Hands()
mpDesenho = mp.solutions.drawing_utils

while True:
    ok, imagem = cam.read()
    
    if not ok:
        print("Hove uma falha :(")
        break

    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    resultado = maos.process(imagem)

    if resultado.multi_hand_landmarks:
        for hand_landmarks in resultado.multi_hand_landmarks:
            mpDesenho.draw_landmarks(imagem, hand_landmarks, detectaMao.HAND_CONNECTIONS)

    if resultado.multi_hand_landmarks:
        for hand_landmarks in resultado.multi_hand_landmarks:

            polegar = hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y
            indicador = hand_landmarks.landmark [8].y > hand_landmarks.landmark [6].y
            medio = hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y
            anelar = hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y
            mindinho = hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y

            if polegar and indicador and medio and anelar and mindinho:
                pyautogui.press("space")
                print("ta funcionando")


    cv2.imshow("Câmera", imagem)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break