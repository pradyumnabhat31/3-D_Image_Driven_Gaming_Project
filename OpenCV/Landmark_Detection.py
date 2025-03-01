import cv2
import mediapipe as mp

# Adjustable confidence threshold
DETECTION_CONFIDENCE = 0.7
TRACKING_CONFIDENCE = 0.7

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Set up webcam
cap = cv2.VideoCapture(0)

# Initialize Hands model
with mp_hands.Hands(max_num_hands=1, min_detection_confidence=DETECTION_CONFIDENCE, min_tracking_confidence=TRACKING_CONFIDENCE) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame for hand landmarks
        results = hands.process(rgb_frame)

        # Draw landmarks and connections if detected
        if results.multi_hand_landmarks:
            print(f"Hand detected at confidence: {DETECTION_CONFIDENCE}")

            for hand_landmarks in results.multi_hand_landmarks:
                # Draw keypoints and connections
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

                # Display keypoint indices (optional)
                for idx, landmark in enumerate(hand_landmarks.landmark):
                    h, w, _ = frame.shape
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    cv2.putText(frame, str(idx), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX,
                                0.4, (0, 0, 255), 1)

        else:
            print(f"No hand detected at confidence: {DETECTION_CONFIDENCE}")

        # Display output
        cv2.imshow(f'Hand Detection (Confidence: {DETECTION_CONFIDENCE})', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

cap.release()
cv2.destroyAllWindows()
