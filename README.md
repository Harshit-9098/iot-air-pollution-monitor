# iot-air-pollution-monitor
# 🌍 IoT-Based Air Pollution Detection and Prediction System

An end-to-end IoT micro-project built using an ESP32 microcontroller, MQ135 gas sensor, DHT11 temperature/humidity sensor, Python logging script, Flask backend, and a dynamic Chart.js web dashboard.

---

## 📊 Live Dashboard Preview
[![Dashboard Preview](Screenshot%202026-10-28%20215732.png)](Screenshot%202026-10-28%20215732.png)

---

## 🛠️ System Architecture & Workflow
1. **Hardware Layer:** ESP32 reads analog pollutant data from the MQ135 sensor and digital temperature/humidity data from the DHT11 sensor.
2. **Data Logging:** A Python serial script (`data_logger.py`) listens to port `COM8` at 115200 baud and logs live records into `air_pollution_data.csv`.
3. **Backend & Analytics:** A Flask server (`app.py`) parses the CSV, monitors connection health, and computes AQI levels along with short-term machine learning trend predictions.
4. **Frontend Visualization:** A responsive Chart.js web interface renders live metric cards and dynamic graphs.

---

## 🚀 Quick Start / How to Run
1. Clone or download this repository to your local machine.
2. Connect your ESP32 hardware to your PC via USB (ensure it maps to `COM8`).
3. Double-click the **`run.bat`** file to automatically start the Python data logger, initialize the Flask server, and launch the web dashboard in your browser!
4. Open your browser and navigate to: `http://127.0.0.1:5000`
