from ultralytics import YOLO
import cv2
import pyttsx3
import time
import threading

# Load YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Prevent multiple speech threads from using the engine simultaneously
speech_lock = threading.Lock()

# Function to speak detected object information
def speak(text):
    with speech_lock:
        engine.say(text)
        engine.runAndWait()

# Open laptop webcam
cap = cv2.VideoCapture(0)

# Store last announced position and time for each object
last_position = {}
last_time = {}

# Cooldown period before repeating the same object announcement
COOLDOWN = 3

# Store FPS values for performance analysis
fps_list = []

print("Voice Detection Started")

# Main detection loop
while True:

    # Capture frame from webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Start timer for FPS calculation
    start = time.time()

    frame_width = frame.shape[1]
    frame_height = frame.shape[0]

    # Run YOLO object detection on current frame
    results = model(
        frame,
        imgsz=416,
        conf=0.5,
        verbose=False
    )

    # Draw bounding boxes and labels on frame
    annotated = results[0].plot()

    # Process each detected object
    for box in results[0].boxes:

        confidence = float(box.conf[0])

        # Ignore low-confidence detections
        if confidence < 0.5:
            continue

        # Get detected object class
        class_id = int(box.cls[0])
        label = model.names[class_id]

        # Extract bounding box coordinates
        x1, y1, x2, y2 = box.xyxy[0]

        # Calculate horizontal centre of object
        center_x = float((x1 + x2) / 2)

        # ===== POSITION ESTIMATION =====

        if center_x < frame_width / 3:
            position = "LEFT"

        elif center_x < 2 * frame_width / 3:
            position = "CENTRE"

        else:
            position = "RIGHT"

        # ===== DISTANCE ESTIMATION =====
        # Added based on feedback

        box_area = (x2 - x1) * (y2 - y1)

        frame_area = frame_width * frame_height

        ratio = box_area / frame_area

        if ratio > 0.15:
            distance = "CLOSE"

        elif ratio > 0.05:
            distance = "MID-DISTANCE"

        else:
            distance = "FAR"

        current_time = time.time()
        should_speak = False

        # Announce object if seen for the first time
        if label not in last_position:
            should_speak = True

        # Announce if object position has changed
        elif last_position[label] != position:
            should_speak = True

        # Announce again after cooldown period
        elif current_time - last_time[label] > COOLDOWN:
            should_speak = True

        # Generate voice alert
        if should_speak:

            message = f"{label} on the {position}, {distance}"

            print(message)

            threading.Thread(
                target=speak,
                args=(message,),
                daemon=True
            ).start()

            # Update memory with latest object state
            last_position[label] = position
            last_time[label] = current_time

    # Calculate FPS
    fps = 1 / (time.time() - start)
    fps_list.append(fps)

    # Display FPS on output frame
    cv2.putText(
        annotated,
        f"FPS: {fps:.1f}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show detection window
    cv2.imshow("Parvai Voice Detection", annotated)

    # Exit when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

# Print FPS statistics
print(f"Avg FPS: {sum(fps_list)/len(fps_list):.2f}")
print(f"Min FPS: {min(fps_list):.2f}")
print(f"Max FPS: {max(fps_list):.2f}")