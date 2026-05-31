#include <Wire.h>
#include <MPU6050_tockn.h>

MPU6050 mpu6050(Wire);

unsigned long sensorMillis = 0, logMillis = 0;

int freeFallCounter = 0, impactCounter = 0;

bool phase1 = false, fall = false;

void setup() {

Serial.begin(115200);

Wire.begin();

mpu6050.begin();

mpu6050.calcGyroOffsets(true);

Serial.println("ESP32 Fall Detection Started");
}

void loop() {

unsigned long currentMillis = millis();

if (currentMillis - sensorMillis >= 20) {


sensorMillis = currentMillis;

mpu6050.update();

float ax = mpu6050.getAccX();
float ay = mpu6050.getAccY();
float az = mpu6050.getAccZ();

float magnitude = sqrt(ax * ax + ay * ay + az * az);

// ===== FREE FALL DETECTION =====

if (magnitude < 0.5) {

  freeFallCounter++;

} else {

  freeFallCounter = 0;
}

if (freeFallCounter == 10) {

  phase1 = true;

  impactCounter = 0;

  Serial.println("FREE FALL DETECTED");
}

// ===== IMPACT DETECTION =====

if (phase1) {

  impactCounter++;

  if (magnitude > 3.0) {

    Serial.print("IMPACT DETECTED : ");
    Serial.println(magnitude);

    fall = true;

    Serial.print("FALL DETECTED at ");
    Serial.print(currentMillis);
    Serial.println(" ms");

    phase1 = false;

    freeFallCounter = 0;

    impactCounter = 0;
  }

  if (impactCounter > 50) {

    phase1 = false;

    freeFallCounter = 0;

    impactCounter = 0;
  }
}

// ===== CSV LOGGING =====

if (currentMillis - logMillis >= 70) {

  logMillis = currentMillis;

  Serial.print(currentMillis);
  Serial.print(",");

  Serial.print(ax);
  Serial.print(",");

  Serial.print(ay);
  Serial.print(",");

  Serial.print(az);
  Serial.print(",");

  Serial.print(magnitude);
  Serial.print(",");

  Serial.print(phase1);
  Serial.print(",");

  Serial.println(fall);

  fall = false;
}


}
}
