from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Função para detecção de rostos em um frame de vídeo
def detect_faces(frame):
    # Carregar o classificador pré-treinado para detecção de rostos
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Converter o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return faces

# Função para gerar os frames do vídeo com os rostos detectados
def generate_frames():
    # Inicializar o objeto de captura de vídeo
    cap = cv2.VideoCapture(0)

    while True:
        # Capturar um frame da webcam
        ret, frame = cap.read()

        # Detectar rostos no frame
        faces = detect_faces(frame)

        # Loop sobre os rostos detectados
        for (x, y, w, h) in faces:
            # Desenhar um retângulo ao redor do rosto
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Converter o frame em um formato que possa ser enviado como resposta HTTP
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Liberar o objeto de captura de vídeo
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
