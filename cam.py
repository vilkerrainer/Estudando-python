import cv2
import numpy as np

# Inicializa a webcam
cap = cv2.VideoCapture(0)

# Variáveis para controle de movimento
background = None
contador_movimento = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Pré-processamento do frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Inicializa o fundo (primeiro frame)
    if background is None:
        background = gray
        continue

    # Calcula a diferença entre o frame atual e o fundo
    diff = cv2.absdiff(background, gray)
    threshold = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    threshold = cv2.dilate(threshold, None, iterations=2)

    # Encontra contornos nas áreas de movimento
    contours, _ = cv2.findContours(
        threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    movimento_detectado = False
    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Filtra contornos pequenos
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            movimento_detectado = True

    # Incrementa o contador se houve movimento
    if movimento_detectado:
        contador_movimento += 1

    # Exibe o contador e o frame
    cv2.putText(
        frame,
        f"Movimentos: {contador_movimento}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2,
    )
    cv2.imshow("Webcam com Deteccao de Movimento", frame)

    # Atualiza o fundo para o próximo frame
    background = gray

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()