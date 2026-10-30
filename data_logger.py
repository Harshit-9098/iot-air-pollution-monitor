import csv
import time
import serial

# Apne ESP32 ka COM port aur baud rate yahan dalein
port = "COM8"
baud = 115200

ser = serial.Serial(port, baud)
print(f"Connected to {port}. Logging data to air_pollution_data.csv...")

# CSV file create karein aur headers likhein
with open("air_pollution_data.csv", mode="w", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  writer.writerow(["Timestamp", "Temperature", "Humidity", "MQ135_Raw_Value"])

  try:
    while True:
      line = ser.readline().decode("utf-8").strip()
      if line:
        print(line)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        # Yahan 'f' ki jagah 'writer' use hoga
        writer.writerow([timestamp, line])
        f.flush()
  except KeyboardInterrupt:
    print("Logging stopped by user. Data saved successfully!")