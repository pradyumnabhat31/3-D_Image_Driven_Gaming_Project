import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read frame
    success, frame = cap.read()
    if not success:
        continue

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand detection
    result = hands.process(rgb_frame)

    # If hand landmarks are detected
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw hand skeleton
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmark positions of index and thumb
            h, w, _ = frame.shape
            index_tip = hand_landmarks.landmark[8]  # Index finger tip
            thumb_tip = hand_landmarks.landmark[4]  # Thumb tip

            # Convert normalized coordinates of index and thumb to pixel values
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)

            # Draw a red circl at the index fingertip
            cv2.circle(frame, (index_x, index_y), 10, (0, 0, 255), -1)

            # Calculate distance between thumb tip and index tip
            distance = np.linalg.norm([thumb_x - index_x, thumb_y - index_y])

            # Print Pinching or Not Pinching
            if distance < 40:
                print("Pinching")
            else:
                print("Not Pinching")

    # Display the frame
    cv2.imshow("Hand Detection", frame)

    # Exit when q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
