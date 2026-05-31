# **DESIGN RATIONALE**



## **Project Overview**



The objective of this design was to create a wearable sensor node based on the ESP32-WROOM-32 and MPU6050. The system is powered by a single-cell LiPo battery, includes onboard charging through USB-C, and generates a regulated 3.3V supply for the microcontroller and sensor. The design focuses on simplicity, low component count, and reliable operation.



#### **USB-C Power Input**



A USB-C connector was selected as the charging input because it is widely available and commonly used in modern portable electronics.



Two 5.1kΩ resistors were connected to the CC1 and CC2 pins. These resistors allow the USB power source to correctly identify the circuit as a power sink and safely provide 5V on the VBUS line.



Since the USB connection is used only for charging, only the VBUS and GND lines are utilized in this design, while the USB data lines remain unused.



#### **TP4056 LiPo Charging Circuit**



The TP4056 was selected because it is a dedicated charging IC for single-cell lithium-ion and lithium-polymer batteries. It provides a simple and reliable charging solution with minimal external components.



The charging current is controlled using the resistor connected to the PROG pin. A 2kΩ resistor was selected, resulting in an approximate charging current of 580mA. This value was chosen because it provides a safer charging current for small wearable batteries while reducing heat generation and improving battery longevity.



Two 10µF capacitors were included around the battery connection of the TP4056 charging circuit.These act as bulk capacitors, one capacitor helps provide local energy storage near the charging IC, while the second capacitor helps stabilize the battery rail during charging and sudden load variations. Together, they reduce voltage fluctuations and improve the overall stability of the charging system.

#### 

#### **AMS1117-3.3 Voltage Regulator**



The ESP32 and MPU6050 operate at 3.3V and therefore cannot be powered directly from the LiPo battery.



An AMS1117-3.3 LDO regulator was used to generate a stable 3.3V supply from the battery voltage. Compared to switching converters, LDO regulators introduce significantly less electrical noise, making them suitable for sensor-based applications.



A 10µF capacitor was placed at the regulator input to reduce input voltage fluctuations, while a 100nF capacitor was added at the output for high-frequency noise filtering and output stabilization.



#### **ESP32-WROOM-32 Module**



The ESP32-WROOM-32 was selected because it provides sufficient processing capability, integrated WiFi and Bluetooth connectivity, and a large ecosystem of software support.



A 10kΩ pull-up resistor was connected to the EN pin to ensure that the microcontroller remains enabled during normal operation.



A 10µF decoupling capacitor was placed near the ESP32 power pins to improve supply stability and reduce noise caused by rapid current changes during wireless communication and processing.



An LED with a 330Ω current-limiting resistor was included as a simple status indicator.

#### 

#### **MPU6050 Motion Sensor**



The MPU6050 was selected because it combines a 3-axis accelerometer and a 3-axis gyroscope in a single package, making it suitable for motion sensing and fall detection applications.



Communication between the ESP32 and MPU6050 is performed through the I2C protocol using the SDA and SCL lines.



Two 4.7kΩ pull-up resistors were added to the SDA and SCL lines because I2C devices can only actively pull the bus low. The pull-up resistors maintain the bus in a logic-high state when communication is not taking place.



A 100nF decoupling capacitor was connected close to the VDD pin to reduce power supply noise.



Additional capacitors were included according to the MPU6050 datasheet recommendations:



100nF capacitor connected to REGOUT for internal voltage stabilization.

2.2nF capacitor connected to CPOUT for proper operation of the sensor's internal circuitry.



Including these recommended components improves measurement stability and ensures reliable sensor operation.



##### **Key Design Decisions :**



The design emphasizes reliability, simplicity, and good engineering practice. Particular attention was given to:



Proper USB-C power negotiation using CC resistors.

Safe LiPo battery charging using the TP4056.

Stable 3.3V regulation through an LDO regulator.

Correct I2C implementation with pull-up resistors.

Proper use of decoupling and bulk capacitors.

Following MPU6050 datasheet recommendations, including the REGOUT and CPOUT capacitors.



These decisions help improve system stability, reduce noise, and increase the overall reliability of the wearable device.





**Q\&A Section :** 



1. **What is the fundamental difference between the NE555 timer used in the Li-Fi PCB and the ESP32 used in this wearable sensor PCB?**

**Answer:** In my Li-Fi project the NE555 timer IC was used to generate PWM signals for controlling the speed of the motor. The output from the LM358 IC was connected to pin 5 of the NE555 IC which helped vary the duty cycle and control the motor speed through the Li-Fi system . The NE555 IC mainly worked as hardware based timer and signal generator using analog components like resistors and capacitors internally.

In this wearable sensor PCB, the ESP32 is used as a programmable microcontroller. Instead of generating only signals, the ESP32 can read data from the MPU 6050 sensor through I2C communication, process the data in software, and make decisions such as detecting a fall. It also supports advanced features like WI Fi and Bluetooth communication.
So the main difference between these two is that any 555 performs a fixed hardware timing function while the ESP32 is a flexible and intelligent controller capable of sensing processing communicating and taking real time decision.



2. **In your Li-Fi circuit, you used a LM358 op-amp for signal amplification. Why is no amplifier needed in this I2C circuit?**

**Answer:** In my Li-fi project, I used LM 358 IC between LDR receiver and the and NE555 timer IC even though the received signal was working properly, I added the amplifier stage to make the system more reliable and compatible with weaker optical signals in the future, it also helped in improving signal conditioning before the signal was used for PWM Motor control.

In this wearable sensor PCB, an amplifier if not needed because the MPU 6050 communicates digitally with the ESP 32 using I2C protocol. The sensor directly transfers digital data through the SDA and SCL lines, so there is no weak analog signal that requires amplification. Since the communication takes place over short PCB connections, the ESP32 can read the sensor data directly and reliably without using an external op amp circuit.



3. **The TP4056 PROG pin sets the charge current. What resistor value did you use and what current does that give ?**

Answer: In this design, I used a 1.2 K resistor on the PROG pin of the TP 4056 charging IC. According to the TP 4056 data sheet, this resistor value set the charging current to approximately 1 ampere. I selected this value because it provides reasonably fast charging and a safer option for a small lipo battery while keeping the circuit simple for the prototype design .



4. **If this PCB had to fit 35X25mm - Which component takes the most space, and how would you reduce it?**

Answer: If the PCB size had to be reduced to 35X25 MM, the ESP 32 WROOM module would take the most space on the board. This is mainly because the module contains the ESP32 chip, flash memory and built in Wi fi antenna, which also requires a keep out area around the antenna section for proper wireless performance. To reduce the overall size I tried using SMD components like 0603 resistors and capacitors. I would also try to place the power management section more compactly and reduce unnecessary spacing between the components while maintaining proper grounding and signal integrity.
Although, the Lipo battery would also take a significant amount of space on the PCB.



5. **Your Li Fi PCB was a single layer. Would you make this PCB single layer or double layer. Why?**

Answer: At the initial prototyping stage, I would prefer designing this PCB as a single layer board. Since I already have experience working on a single layer PCB I feel more comfortable starting with that approach I think this design can still be managed on a single layer PCB for testing and development.
If the prototype works properly and the design needs to be made smaller and more compact, then I would move to a double layer PCB. A double layer design would make routing easier improve grounding and help reduce the overall PCB size especially around the ESP32 and power management section.

