import cv2

# Função para detecção de rostos em um frame de vídeo
def detect_faces(frame, face_cascade):
    # Converter o frame para escala de cinza para otimizar o processo de detecção
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Função para exibir o vídeo com os rostos detectados e permitir que o usuário associe nomes
def annotate_faces():
    # Inicializar o objeto de captura de vídeo
    cap = cv2.VideoCapture(0)
    
    # Carregar o classificador pré-treinado para detecção de rostos uma vez
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Dicionário para armazenar associações de nomes e coordenadas de rostos
    face_names = {}
    
    print("Pressione 'q' para sair.")

    while True:
        # Capturar um frame da webcam
        ret, frame = cap.read()
        
        if not ret:
            print("Erro ao capturar o vídeo.")
            break

        # Detectar rostos no frame
        faces = detect_faces(frame, face_cascade)

        # Loop sobre os rostos detectados
        for i, (x, y, w, h) in enumerate(faces):
            # Desenhar um retângulo ao redor do rosto
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Verificar se o rosto já foi anotado
            if i not in face_names:
                # Solicitar que o usuário insira o nome associado ao rosto
                print(f"Digite o nome associado ao rosto {i+1} (Pressione Enter para manter vazio):")
                name = input().strip()
                face_names[i] = name if name else "Desconhecido"

            # Adicionar o nome associado ao rosto
            cv2.putText(frame, face_names[i], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Exibir o frame com os rostos detectados e os nomes associados
        cv2.imshow("Faces Anotadas", frame)

        # Aguardar a tecla 'q' ser pressionada para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar o objeto de captura de vídeo e fechar todas as janelas
    cap.release()
    cv2.destroyAllWindows()

# Chamar a função para detectar rostos e associar nomes
annotate_faces()
