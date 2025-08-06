import cv2
import mediapipe as mp
import numpy as np
import math
import threading
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Play alert only if it's not already playing
def play_alert():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("alert.mp3")
        pygame.mixer.music.play()

def calculate_EAR(eye):
    A = math.dist(eye[1], eye[5])
    B = math.dist(eye[2], eye[4])
    C = math.dist(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

LEFT_EYE_IDX = [362, 385, 387, 263, 373, 380]
RIGHT_EYE_IDX = [33, 160, 158, 133, 153, 144]

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

cap = cv2.VideoCapture(0)

eye_closed_frames = 0
DROWSY_THRESHOLD = 50
EAR_THRESHOLD = 0.22

# Cooldown system to prevent repeated alert sound
last_alert_time = 0
alert_cooldown = 5  # seconds

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]
        h, w, _ = frame.shape

        left_eye = []
        right_eye = []

        for idx in LEFT_EYE_IDX:
            x = int(face_landmarks.landmark[idx].x * w)
            y = int(face_landmarks.landmark[idx].y * h)
            left_eye.append((x, y))
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        for idx in RIGHT_EYE_IDX:
            x = int(face_landmarks.landmark[idx].x * w)
            y = int(face_landmarks.landmark[idx].y * h)
            right_eye.append((x, y))
            cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

        left_ear = calculate_EAR(left_eye)
        right_ear = calculate_EAR(right_eye)
        avg_ear = (left_ear + right_ear) / 2.0

        cv2.putText(frame, f'EAR: {avg_ear:.2f}', (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

        if avg_ear < EAR_THRESHOLD:
            eye_closed_frames += 1

            if eye_closed_frames > DROWSY_THRESHOLD:
                cv2.putText(frame, "DROWSINESS ALERT!", (30, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 255), 3)

                current_time = time.time()
                if current_time - last_alert_time > alert_cooldown:
                    last_alert_time = current_time
                    threading.Thread(target=play_alert, daemon=True).start()
        else:
            eye_closed_frames = 0

    cv2.imshow("Driver Sleepiness Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
