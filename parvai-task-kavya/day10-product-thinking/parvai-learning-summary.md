### **Product Thinking Document**

#### 



##### **1. PCB Design — Then and Now**





The most important thing I learned during Days 1–3 was how to design a PCB in a much more structured way. Earlier, I mainly focused on building a circuit that worked. If I got the required output, I considered the design complete. Through this task, I realized that PCB design involves much more than just connecting components together.



I learned how to organize a circuit into proper sections, keep the schematic clean, use power flags correctly, and perform ERC checks to identify potential design issues before moving further. I also became more comfortable reading datasheets and understanding why certain components are recommended instead of simply copying reference circuits.



Another important learning was understanding the purpose of supporting components such as pull-up resistors, decoupling capacitors, and voltage regulation circuits. Earlier, I often used these components only if I saw them in an example circuit. Now I understand how they contribute to stable and reliable operation and why they should be included in the design.



Overall, the biggest change was that I moved beyond the mindset of simply making a circuit work. I now pay more attention to reliability, stability, proper design practices, and the reasoning behind every component used in the schematic. This has given me much more confidence in designing PCBs from datasheets rather than relying only on existing reference designs.





If I had to redesign my Li-Fi PCB today, I would approach it very differently. The original project was intentionally built using mostly analog components such as the LM358, NE555, Darlington transistor, LDR, and LM3914 because I wanted to learn how the complete signal chain worked at the hardware level rather than relying on a microcontroller for everything. It was a great learning experience, but it also exposed several challenges.



While building the project, I often faced difficulties during debugging and circuit assembly because the schematic had more than 20+ components and multiple signal-conditioning stages. At that time, my primary focus was getting the circuit to work, so I relied heavily on trial-and-error testing, measuring voltages with a multimeter, and making adjustments until the circuit behaved as expected. I did not always pay enough attention to component biasing, power stability, or datasheet recommendations.



After completing these tasks, I now realize that I would spend much more time on the design stage itself. I would create a cleaner and more structured schematic, organize the circuit into functional blocks, and use datasheets more extensively to determine component values instead of depending mainly on experimentation. I now have a much better understanding of supporting components such as pull-up resistors, decoupling capacitors, and proper power supply design, which would help improve the stability and reliability of the circuit.



Another important difference is that I would be much more confident working with the ICs used in the project. Earlier, it was common for an IC stage to not work correctly on the first attempt, requiring multiple rounds of debugging. Now I have a better understanding of how to interpret datasheets, verify operating conditions, and design supporting circuitry correctly, which would significantly reduce development time.



From a product perspective, I could also redesign the project using a more digital approach with a microcontroller handling signal processing and decision-making. However, I still believe that building the original analog version was valuable because it helped me understand the fundamentals of sensing, amplification, filtering, timing circuits, and output control at a much deeper level.



The biggest difference is that earlier I focused on making the circuit work. Today, I would focus on making it work reliably, predictably, and in a way that is easier to debug and maintain.







##### **2. FIRMWARE — WHAT CHANGED**





One of the biggest changes in my firmware development approach was moving from using delay() to using millis() for timing. In my previous projects, I often used delay() because it was simple to implement. However, this task helped me understand why it is not suitable for a real product that must run continuously for long periods.



When delay() is used, the microcontroller stops performing other tasks during the waiting period. In a wearable device, this could lead to missed sensor readings or delayed responses. Using millis() allows multiple tasks such as sensor sampling, fall detection, and data logging to run without blocking each other.



The biggest learning for me was that product firmware should remain responsive at all times rather than pausing execution while waiting for a delay to finish.







The hardest part of the two-phase fall detection logic was choosing the right sensor interval and logging interval. During testing, I noticed that if the sensor interval was too large, the impact event could easily be missed because the impact spike lasts for only a very short time. In some cases, the system would detect the free-fall phase but miss the impact phase, while in other cases the opposite could happen.



Another challenge was making sure that a fall was detected only when a free-fall event was followed by an impact event within a reasonable time window. Detecting a low acceleration value or a high acceleration spike individually was not very difficult, but combining them into a reliable sequence required a lot of testing and tuning.



This was an interesting learning experience because it showed me that detection accuracy depends not only on thresholds, but also on selecting appropriate sensor sampling and logging intervals so that important events are not missed.









##### **3. AI ON CPU — WHAT SURPRISED YOU**





What surprised me the most was how much the FPS dropped as the image size increased. Using YOLOv8n, I achieved around 32 FPS at an image size of 320, but the FPS reduced significantly at higher resolutions. This showed me that image size has a major impact on processing speed and real-time performance.







For a wearable device, around 32 FPS is a reasonably good result because it allows the system to respond smoothly in real time while keeping computational requirements relatively low.







In my antenna project, RF performance was measured using metrics such as VSWR and S-parameters. Similarly, AI models are evaluated using metrics such as Precision, Recall, mAP, IoU, and FPS. In this project, the main metric I measured directly was FPS to compare performance at different image sizes and understand the trade-off between image resolution and processing speed.











##### **4. YOUR WIFI SENSING PROJECT — BRIDGE TO PARVAI**





Based on my project experience, I do not think the WiFi sensing approach I implemented would significantly improve fall detection. My WiFi sensing system was mainly designed to detect human presence and movement through signal variations, whereas the wearable device directly measures body motion, free-fall conditions, and impact events.



Because of this, I believe the wearable sensor should remain the primary decision-making system. A more practical use of WiFi in this context would be communication. For example, after a fall is detected by the wearable device, WiFi could be used to transmit alerts, logs, or status information to a mobile application or cloud platform for monitoring.



At a more advanced level, WiFi sensing technologies may be able to estimate human activity and body state without requiring sensors on the body. However, based on the level of WiFi sensing used in my project, I believe its strongest contribution would be communication and connectivity rather than fall detection itself.







One feature I would add to Parvai Insight is cloud-based alert and monitoring support. If a fall is detected, the wearable device could automatically send an alert to a mobile application or cloud platform using WiFi connectivity. The alert could include the time of the event, sensor readings, and the current status of the user.





##### **5.WHAT WOULD YOU BUILD NEXT**





If I had 30 more days and access to hardware, I would build a self-balancing robot with WiFi connectivity and AI-based computer vision capabilities. The goal would be to create a robot that can maintain balance autonomously, monitor its surroundings, and communicate wirelessly with a user interface.







The robot would use an **ESP32** as the main microcontroller responsible for sensor processing, control algorithms, and communication. An **MPU6050** accelerometer and gyroscope sensor would continuously measure the robot's tilt angle and orientation through the **I2C protocol**. This sensor data would be processed by the ESP32, which would run a **PID (Proportional-Integral-Derivative)** control algorithm. The PID controller would continuously calculate the error between the robot's current tilt angle and the desired upright position and adjust the motor speed accordingly to keep the robot balanced. Tuning the PID parameters would be an important part of the project because they directly affect the stability and responsiveness of the robot.







For movement, I would use **BO motors** driven through a motor driver module. The ESP32 would generate PWM (Pulse Width Modulation) signals to control motor speed and direction. Based on the tilt angle calculated from the MPU6050 data, the controller would continuously adjust the motor output in real time to maintain balance.







To add **Ai-computer vision** capabilities, I would use an **ESP32-CAM module**. The camera would capture images of the surrounding environment and perform basic object or obstacle detection. Communication between the ESP32 and ESP32-CAM could be achieved through UART serial communication, allowing visual information to be shared with the main controller for navigation decisions.







**WiFi** would be used for wireless monitoring and communication. The ESP32 could transmit telemetry data such as tilt angle, battery status, motor speed, and system health to a mobile application or cloud dashboard. This would allow remote monitoring of the robot's performance and provide a platform for future IoT-based features.







By combining the ESP32, MPU6050, PID-based control, motor control, ESP32-CAM, WiFi communication, and computer vision, the robot would be able to balance itself, detect obstacles, monitor its surroundings, and make basic navigation decisions. This project would integrate embedded systems, control systems, wireless communication, sensors, and AI into a single intelligent robotic platform.









Another idea that I find interesting is AI-based smart glasses. The glasses could use a camera and computer vision to identify nearby objects and provide voice-based feedback to the user. An MPU6050 sensor could also be integrated for fall detection, while WiFi or Bluetooth connectivity could be used to send emergency alerts and connect with a mobile application.



I find this concept interesting because it combines AI, sensors, wireless communication, and wearable technology into a practical real-world product.





