# Controle de Vídeo com Gestos de Mão

Este projeto permite controlar **play/pause** e **tela cheia** de vídeos usando gestos da mão detectados pela câmera. Ele utiliza **MediaPipe** para detecção das mãos e **PyAutoGUI** para simular pressionamento de teclas.

---

## Funcionalidades

- **Play/Pause**: Fechando a mão, o vídeo pausa ou dá play.
- **Tela cheia**: Indicador e polegar levantados com os outros dedos abaixados ativam o modo tela cheia.
- Desenho dos landmarks da mão na tela usando MediaPipe para visualização.

---

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)

---

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/JulianneAires/controle-maos.git
   cd seu-repositorio
   ````
2. Instale as dependências:

   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

3. Execute o script:

   ```bash
   python controle_maos.py
   ```

4. Gestos:

   * Fechar a mão → Play/Pause
   * Indicador e polegar levantados, outros dedos abaixados → Tela cheia

5. Pressione `x` para sair do programa.

---

## Observações

* A detecção depende da iluminação e posicionamento da mão.
* O script funciona melhor com **uma mão** visível na câmera.


