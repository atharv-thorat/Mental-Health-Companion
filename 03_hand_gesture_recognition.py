import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty frame.")
        continue

    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    gesture = ""

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            tips_ids = [4, 8, 12, 16, 20]
            pip_ids = [3, 6, 10, 14, 18]

            fingers_status = []
            for tip_id, pip_id in zip(tips_ids, pip_ids):
                tip_y = hand_landmarks.landmark[tip_id].y
                pip_y = hand_landmarks.landmark[pip_id].y
                fingers_status.append(tip_y < pip_y)

            if all(fingers_status):
                gesture = "Open Palm"
            elif not any(fingers_status):
                gesture = "Fist"
            elif fingers_status[1] and fingers_status[2] and not any(fingers_status[0:2] + fingers_status[3:]):
                gesture = "Peace Sign"

            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.putText(image, gesture, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
    cv2.imshow("Gesture Recognition", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

