#### **FPS Performance Results**



The YOLOv8n model was tested at different image sizes to observe the effect of image resolution on real-time performance.



Image Size	Average FPS  

640	        10.63

416        	24.12

320     	32.40





#### **Observation**



The results show that FPS increases as the image size decreases. Smaller images require less computation, allowing the model to process more frames per second. This demonstrates the trade-off between image resolution and real-time performance.



For wearable and resource-constrained systems, lower image resolutions can provide significantly better responsiveness while maintaining acceptable detection performance.

