import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

detectaMao = mp.solutions.hands
maos = detectaMao.Hands(max_num_hands = 1)
mpDesenho = mp.solutions.drawing_utils
executou_pause = False
executou = False

while True:
    ok, imagem = cam.read()
    
    if not ok:
        print("Hove uma falha :(")
        break

    resultado = maos.process(imagem)

    if resultado.multi_hand_landmarks:
        for hand_landmarks in resultado.multi_hand_landmarks:
            mpDesenho.draw_landmarks(imagem, hand_landmarks, detectaMao.HAND_CONNECTIONS)

    if resultado.multi_hand_landmarks:
        for hand_landmarks in resultado.multi_hand_landmarks: 

            polegar_baixo = hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y
            indicador_baixo = hand_landmarks.landmark [8].y > hand_landmarks.landmark [6].y
            medio_baixo = hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y
            anelar_baixo = hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y
            mindinho_baixo = hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y
            indicador_alto = hand_landmarks.landmark [8].y < hand_landmarks.landmark [6].y
            polegar_alto = hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y
            
            mao_fechada = polegar_baixo and indicador_baixo and medio_baixo and anelar_baixo and mindinho_baixo
            tela_cheia = indicador_alto and polegar_alto and medio_baixo and anelar_baixo and mindinho_baixo
 
            if mao_fechada and executou_pause == False:
                pyautogui.press("space")
                print("ta funcionando")
                executou_pause = True
            
            elif executou_pause == True and not mao_fechada:
                executou_pause = False
            
            if tela_cheia and executou == False:
                pyautogui.press("f")
                print("tela cheia ta funcionando")
                executou = True
            
            elif executou == True and not tela_cheia:
                executou = False

    cv2.imshow("Câmera", imagem)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB) 

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break