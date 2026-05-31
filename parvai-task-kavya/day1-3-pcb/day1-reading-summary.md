# **Day 1 Reading Summary**



1. **I2C Protocol – How does it differ from the optical communication in your Li-Fi project? What are SDA and SCL lines? Why are pull-up resistors needed on I2C?**



In this project, the ESP32 communicates with the MPU6050 sensor using the I2C protocol. I2C is a digital communication protocol that uses only two lines: SDA (Serial Data Line) and SCL (Serial Clock Line). SDA is used for data transfer, while SCL provides the clock signal for synchronization between devices.

In this communication, the ESP32 acts as the master device and the MPU6050 acts as the slave device. The master initiates communication by sending the slave address, followed by read or write operations.

Pull-up resistors are required on the SDA and SCL lines because I2C devices can actively pull the lines low but cannot drive them high. The pull-up resistors maintain the lines at a logic HIGH level when no communication is taking place, ensuring reliable data transfer.

In my Li-Fi project, communication was achieved using an LED and LDR along with analog circuitry such as the LM358. In contrast, I2C is a fully digital communication method that allows direct communication between the ESP32 and MPU6050 without requiring external signal conditioning circuits.

I was already somewhat familiar with I2C communication because I am currently working on a self-balancing robot project that also uses the MPU6050 for angle and motion sensing.



2. **MPU6050 Datasheet – Typical Application Circuit and Recommended Decoupling Capacitors**



After reading the MPU6050 datasheet, I understood how the sensor is connected for stable operation with a microcontroller. The sensor communicates through the I2C protocol using the SDA and SCL pins.

The datasheet recommends a 100nF capacitor between VDD and GND to reduce power supply noise and stabilize the voltage. Another 100nF capacitor is connected to the REGOUT pin for internal voltage stabilization. In addition, a 2.2nF capacitor is connected to the CPOUT pin, which is required for the proper operation of the sensor’s internal circuitry.

These capacitors help reduce noise, improve power stability, and ensure reliable operation of the MPU6050.



3. **TP4056 Datasheet – How is the Charge Current Set Using the PROG Resistor?**



The TP4056 is a dedicated charging IC used for charging a single-cell lithium-ion or lithium-polymer battery. The charging current is determined by the resistor connected to the PROG pin.

By changing the value of this resistor, the charging current can be adjusted according to the battery requirements. In this design, a 2kΩ resistor was selected, resulting in an approximate charging current of 580mA. This charging current is suitable for a small wearable LiPo battery and helps reduce heat generation during charging.

The circuit also uses capacitors near the input supply and battery terminal to improve voltage stability. The CHRG and STDBY pins can be connected to LEDs to indicate charging and standby status.



4. **What does an LDO Voltage Regulator do? Why does an ESP32 wearable need 3.3V instead of 5V?**



An LDO (Low Dropout Regulator) is used to provide a stable output voltage from a higher input voltage source. In this project, the AMS1117-3.3 LDO converts the battery voltage into a regulated 3.3V supply required by the ESP32 and MPU6050.

In my Li-Fi project, components such as the NE555 timer and LM358 op-amp operated from a 5V supply. However, the ESP32 is designed to operate at 3.3V, and applying 5V directly to its logic pins may damage the device.

The LDO regulator also helps reduce voltage fluctuations from the battery and provides a cleaner power supply for reliable operation of the wearable system.



**My Learnings :** 



Through this activity, I gained a better understanding of the I2C protocol and how communication takes place between a microcontroller and a sensor. Although I had prior exposure to I2C through my self-balancing robot project, reading the datasheets helped me understand the protocol in greater detail.

I also learned the importance of decoupling capacitors and how they contribute to stable circuit operation by reducing noise and voltage fluctuations. Another important learning was the role of LDO regulators in providing a clean and stable power supply for microcontrollers and sensors.

Overall, this exercise encouraged me to study datasheets more carefully and understand not only how components are connected, but also why specific design decisions are made in a circuit.

