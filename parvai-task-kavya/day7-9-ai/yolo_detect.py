from ultralytics import YOLO
import cv2, time

#Load YOLOv8 Model

model = YOLO('yolov8n.pt')  
cap = cv2.VideoCapture(0)                                       # 0 = laptop webcam

#List to store FPS values

fps_list = []
while True:
    ret, frame = cap.read()                                     # Read frame from the Webcam
    if not ret: break                                           # Exit if frame is not captured 
    start = time.time()                                         # Start timer for FPS measurement
    results = model(frame, imgsz=320, conf=0.5, verbose=False)  # Perform object detection
    fps = 1 / (time.time() - start)                             # Calculate FPS
    fps_list.append(fps)
    annotated = results[0].plot()                               # Draw bounding boxes and labels
    cv2.putText(annotated, f'FPS: {fps:.1f}', (10,30),          # Display FPS on output frame
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow('Parvai Detection', annotated)                   # Show detection window
    if cv2.waitKey(1) & 0xFF == ord('q'): break                 # Exit when 'q' key is pressed 

cap.release()                                                   # Release webcam resources
cv2.destroyAllWindows()   

# Print FPS Stats

print(f'Avg FPS: {sum(fps_list)/len(fps_list):.2f}')
print(f'Min: {min(fps_list):.2f}  Max: {max(fps_list):.2f}')
