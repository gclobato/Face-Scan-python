import cv2

# Função para detecção de rostos em uma imagem
def detect_faces(image_path):
    # Carregar o classificador pré-treinado para detecção de rostos
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Carregar a imagem
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detectar rostos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return faces

# Função para exibir a imagem com os rostos detectados e permitir que o usuário associe nomes
def annotate_faces(image_path):
    # Carregar a imagem
    image = cv2.imread(image_path)
    faces = detect_faces(image_path)

    # Loop sobre os rostos detectados
    for (x, y, w, h) in faces:
        # Desenhar um retângulo ao redor do rosto
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Exibir um campo de texto para o usuário inserir o nome associado ao rosto
        name = input("Digite o nome associado a este rosto: ")
        cv2.putText(image, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Exibir a imagem com os rostos detectados e os nomes associados
    cv2.imshow("Faces Annotadas", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Caminho para a imagem a ser processada
image_path = "caminho/para/sua/imagem.jpg"

# Chamar a função para detectar rostos e associar nomes
annotate_faces(image_path)
