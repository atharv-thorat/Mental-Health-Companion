import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hand s
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

#
#  State variables for controlling repeated actions
accelerating = False
braking = False
entering = False

# Start webcam
cap = cv2.VideoCapture(0)

print("Gesture Controller Ready.")
print("✊ Closed Fist = Accelerate (RIGHT key)")
print("✋ Open Palm = Brake (LEFT key)")
print("✌ Peace Sign = Press ENTER")
print("Press 'q' to quit.")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty frame.")
        continue

    # Flip image for mirror effect
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    gesture = ""

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get landmark positions
            def get_landmark_pos(id):
                return [hand_landmarks.landmark[id].x, hand_landmarks.landmark[id].y]
            
            # Finger tip and pip positions
            thumb_tip = get_landmark_pos(4)
            thumb_ip = get_landmark_pos(3)
            
            index_tip = get_landmark_pos(8)
            index_pip = get_landmark_pos(6)
            
            middle_tip = get_landmark_pos(12)
            middle_pip = get_landmark_pos(10)
            
            ring_tip = get_landmark_pos(16)
            ring_pip = get_landmark_pos(14)
            
            pinky_tip = get_landmark_pos(20)
            pinky_pip = get_landmark_pos(18)
            
            # Check if fingers are extended (tip above pip)
            fingers_up = []
            
            # Thumb (check x-coordinate for left/right hand)
            if thumb_tip[0] > thumb_ip[0]:  # Right hand
                fingers_up.append(thumb_tip[0] > thumb_ip[0])
            else:  # Left hand
                fingers_up.append(thumb_tip[0] < thumb_ip[0])
                
            # Other fingers (check y-coordinate)
            fingers_up.append(index_tip[1] < index_pip[1])
            fingers_up.append(middle_tip[1] < middle_pip[1])
            fingers_up.append(ring_tip[1] < ring_pip[1])
            fingers_up.append(pinky_tip[1] < pinky_pip[1])
            
            total_fingers = sum(fingers_up)
            
            # Gesture classification
            if total_fingers <= 1:
                gesture = "Fist"
            elif total_fingers >= 4:
                gesture = "Open Palm"
            elif fingers_up[1] and fingers_up[2] and not fingers_up[3] and not fingers_up[4]:
                gesture = "Peace Sign"
            else:
                gesture = ""
            
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # --- Gesture-to-Game Control Section ---
    # Accelerator Control (Fist)
    if gesture == "Fist":
        if not accelerating:
            pyautogui.keyDown("right")
            accelerating = True
            print("➡ Accelerating (Fist)")
    if gesture != "Fist" and accelerating:
        pyautogui.keyUp("right")
        accelerating = False
        print("🛑 Stop Accelerating")

    # Brake Control (Palm)
    if gesture == "Open Palm":
        if not braking:
            pyautogui.keyDown("left")
            braking = True
            print("⬅ Braking (Palm)")
    if gesture != "Open Palm" and braking:
        pyautogui.keyUp("left")
        braking = False
        print("🛑 Stop Braking")

    # Enter Control (Peace Sign)
    if gesture == "Peace Sign":
        if not entering:
            pyautogui.press("enter")
            entering = True
            print("↩ ENTER (Peace Sign)")
    if gesture != "Peace Sign":
        entering = False

    # HUD overlay
    status_text = ""
    if accelerating: status_text += "Accelerating (➡) "
    if braking: status_text += "Braking (⬅) "
    if gesture == "Peace Sign": status_text += "ENTER (↩) "
    
    cv2.putText(image, gesture, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
    cv2.putText(image, status_text, (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2, cv2.LINE_AA)
    cv2.imshow("Gesture Game Control", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
