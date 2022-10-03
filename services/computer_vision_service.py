import cv2
import mediapipe as mp
from flask import redirect

# Realizamos la Videocaptura
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# Mostramos el video en RT


def malla_facial():
    # Creamos nuestra funcion de dibujo
    mpDibujo = mp.solutions.drawing_utils
    ConfDibu = mpDibujo.DrawingSpec(thickness=1, circle_radius=1)

    # Creamos un objeto donde almacenaremos la malla facial
    mpMallaFacial = mp.solutions.face_mesh
    MallaFacial = mpMallaFacial.FaceMesh(max_num_faces=1)

    # Empezamos
    while True:
        # Leemos la VideoCaptura
        ret, frame = cap.read()

        # Si tenemos un error
        if not ret:
            break

        else:

            # Correccion de color
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Observamos los resultados
            resultados = MallaFacial.process(frameRGB)

            # Si tenemos rostros
            if resultados.multi_face_landmarks:
                # Iteramos
                for rostros in resultados.multi_face_landmarks:
                    # Dibujamos
                    mpDibujo.draw_landmarks(
                        frame, rostros, mpMallaFacial.FACEMESH_TESSELATION, ConfDibu, ConfDibu)

            # Codificamos nuestro video en Bytes
            suc, encode = cv2.imencode('.jpg', frame)
            frame = encode.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# Detector de manos
def deteccion_manos():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    with mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5) as hands:
        while True:
            ret, frame = cap.read()

            if ret == False:
                break

            height, width, _ = frame.shape
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks is not None:
                for hand_landmarks in results.multi_hand_landmarks:

                    print(hand_landmarks)

                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(
                            color=(0, 255, 255), thickness=3, circle_radius=5),
                        mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=4, circle_radius=5))

            # Codificamos nuestro video en Bytes
            suc, encode = cv2.imencode('.jpg', frame)
            frame = encode.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            # yield ('console.log(1)')
            # yield '<script>document.location.href="http://www.google.com"</script>'
            # break

    #         cv2.imshow('Frame', frame)
    #         if cv2.waitKey(1) & 0xFF == 27:
    #             break
    # cap.release()
    # cv2.destroyAllWindows()
