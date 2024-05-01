import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
pyautogui.FAILSAFE = False
# Define the resolution and physical dimensions of the screen
screen_resolution = (1920, 1080)  # Example resolution (replace with your actual resolution)
screen_size_inches = 14  # Example screen size in inches

# Calculate pixels per inch (PPI)
ppi = screen_resolution[0] / screen_size_inches

# Adjust this sensitivity factor based on your preference
sensitivity_factor = 1.0899

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                # Calculate the scaled screen coordinates
                screen_x = pyautogui.size().width * landmark.x * sensitivity_factor
                screen_y = pyautogui.size().height * landmark.y * sensitivity_factor
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)
