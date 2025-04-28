import cv2
import mediapipe as mp
import numpy as np
from collections import deque

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Store previous hand landmarks for movement detection
prev_landmarks = None
movement_threshold = 0.02  # Adjust this value based on sensitivity
history_length = 5
position_history = deque(maxlen=history_length)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue
        
    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)
    
    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get wrist landmark (landmark 0)
            wrist = hand_landmarks.landmark[0]
            h, w, c = frame.shape
            cx, cy = int(wrist.x * w), int(wrist.y * h)
            
            # Store current position
            position_history.append((cx, cy))
            
            # Draw movement trail
            for i in range(1, len(position_history)):
                if position_history[i-1] is None or position_history[i] is None:
                    continue
                cv2.line(frame, position_history[i-1], position_history[i], (0, 255, 0), 2)
            
            # Calculate movement if we have previous landmarks
            if prev_landmarks is not None:
                movement = 0
                for i in range(21):  # All 21 hand landmarks
                    dx = hand_landmarks.landmark[i].x - prev_landmarks.landmark[i].x
                    dy = hand_landmarks.landmark[i].y - prev_landmarks.landmark[i].y
                    movement += (dx**2 + dy**2)
                
                movement = np.sqrt(movement / 21)  # Average movement
                
                if movement > movement_threshold:
                    cv2.putText(frame, "Hand Moving!", (50, 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            # Update previous landmarks
            prev_landmarks = hand_landmarks
    
    # Show the frame
    cv2.imshow('Hand Movement Detection', frame)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()