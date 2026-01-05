import cv2

# Initialize webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Could not access camera.")
        break

    cv2.imshow("Webcam Feed", frame)

    # Press 'q' to quit the camera window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()