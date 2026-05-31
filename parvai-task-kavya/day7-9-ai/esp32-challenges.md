### **## Challenges of Running the YOLO Project on an ESP32-S3 with 8MB RAM**



If this project had to run on an ESP32-S3 with 8MB RAM, the biggest challenge would be handling the object detection model itself. During my testing on a laptop with significantly higher processing power and memory, I observed that the FPS reduced noticeably as the image size increased. This shows that object detection requires a considerable amount of computation, especially when processing video frames continuously in real time.



The second challenge would be memory usage. The system must store the object detection model, camera frames, and intermediate data generated during inference. Compared to a laptop, the ESP32-S3 has much more limited memory resources, making memory management a critical factor.



The third challenge would be maintaining real-time performance. During testing, I achieved approximately 10 FPS at an image size of 640 and over 30 FPS at an image size of 320 using a laptop CPU. Since the ESP32-S3 has significantly lower processing capability, achieving similar performance would be difficult. Running object detection on the microcontroller would likely require a smaller model, lower image resolution, or additional optimization techniques to obtain usable performance.



Another challenge would be handling camera frames efficiently. Before object detection can take place, the ESP32-S3 must continuously capture, store, and process image frames from the camera. This itself requires memory and processing resources, especially when working with higher image resolutions.



Power consumption would also be an important consideration. Wearable and battery-powered devices are expected to operate for long durations, and continuously running an object detection model can increase power usage and reduce battery life. Therefore, efficiency becomes just as important as detection performance.



While researching how object detection models can be deployed on ESP32 platforms, I found examples of object detection running on ESP32-CAM boards. However, these implementations typically use highly optimized lightweight models rather than a standard YOLOv8 setup. They operate under much tighter resource constraints and often trade detection accuracy for lower memory usage and faster execution.



Overall, my testing showed that object detection performance is strongly affected by image resolution and available processing power. Based on these observations, running a standard YOLOv8 model directly on an ESP32-S3 would be challenging. A practical implementation would require lightweight models, lower image resolutions, and careful optimization to achieve acceptable real-time performance.



