import cv2
import mediapipe as mp
import time
from collections import deque

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Open two video streams
cap1 = cv2.VideoCapture(0)  # First camera (change to file path if needed)
cap2 = cv2.VideoCapture(1)  # Second camera (change to file path if needed)

# Buffers to store frames and timestamps
buffer1, buffer2 = deque(), deque()
thresh_ms = 30  # Max time difference in milliseconds for synchronization


# Function to get current timestamp in milliseconds
def current_milli_time():
    return int(time.time() * 1000)


# Function to detect and annotate hand landmarks
def process_frame(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    return frame


# Main loop
while cap1.isOpened() and cap2.isOpened():
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print("Failed to grab frames from both cameras.")
        break

    # Capture timestamps
    ts1, ts2 = current_milli_time(), current_milli_time()

    # Store frames in buffers
    buffer1.append((ts1, frame1))
    buffer2.append((ts2, frame2))

    # Synchronization Logic
    while buffer1 and buffer2:
        t1, f1 = buffer1[0]  # Oldest frame from cam1
        t2, f2 = buffer2[0]  # Oldest frame from cam2

        if abs(t1 - t2) <= thresh_ms:
            buffer1.popleft()
            buffer2.popleft()

            # Process synchronized frames
            f1 = process_frame(f1)
            f2 = process_frame(f2)

            # Display side by side
            combined_frame = cv2.hconcat([f1, f2])
            cv2.imshow("Synchronized Hand Tracking", combined_frame)

        elif t1 < t2:
            buffer1.popleft()  # Discard older frame
        else:
            buffer2.popleft()

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap1.release()
cap2.release()
cv2.destroyAllWindows()