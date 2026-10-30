# import re
# from flask import Flask, jsonify, render_template
# import pandas as pd

# app = Flask(__name__)


# @app.route("/")
# def home():
#   return render_template("index.html")


# @app.route("/get_data")
# def get_data():
#   try:
#     df = pd.read_csv("air_pollution_data.csv", header=None)
#     if df.empty:
#       return jsonify({
#           "temperature": "28.0 °C",
#           "humidity": "60.0 %",
#           "mq135": "400",
#           "aqi": "40",
#           "status": "Normal",
#           "trend_labels": [
#               "12 AM",
#               "3 AM",
#               "6 AM",
#               "9 AM",
#               "12 PM",
#               "3 PM",
#               "6 PM",
#               "9 PM",
#           ],
#           "trend_values": [30, 35, 40, 45, 50, 48, 55, 42],
#           "pred_labels": ["Now", "+1h", "+2h", "+3h", "+4h", "+5h", "+6h"],
#           "pred_values": [42, 45, 50, 58, 65, 72, 80],
#       })

#     last_row = df.iloc[-1]
#     row_str = " ".join(str(val) for val in last_row.values)

#     temp_match = re.search(r"Temperature:\s*([\d\.]+)", row_str)
#     hum_match = re.search(r"Humidity:\s*([\d\.]+)", row_str)
#     mq_match = re.search(
#         r"(?:Raw Value|MQ135):\s*(\d+)", row_str, re.IGNORECASE
#     )

#     temp = temp_match.group(1) + " °C" if temp_match else "28.0 °C"
#     hum = hum_match.group(1) + " %" if hum_match else "60.0 %"
#     mq_val = int(mq_match.group(1)) if mq_match else 400

#     aqi_val = int(mq_val / 10)
#     status = (
#         "Normal"
#         if aqi_val <= 50
#         else ("Moderate" if aqi_val <= 100 else "Unhealthy")
#     )

#     # Dynamic trend and prediction points based on current AQI
#     trend_vals = [
#         int(aqi_val * 0.8),
#         int(aqi_val * 0.85),
#         int(aqi_val * 0.9),
#         int(aqi_val * 0.95),
#         aqi_val,
#         int(aqi_val * 1.05),
#     ]
#     pred_vals = [
#         aqi_val,
#         int(aqi_val * 1.08),
#         int(aqi_val * 1.15),
#         int(aqi_val * 1.22),
#         int(aqi_val * 1.3),
#         int(aqi_val * 1.38),
#         int(aqi_val * 1.45),
#     ]

#     return jsonify({
#         "temperature": temp,
#         "humidity": hum,
#         "mq135": str(mq_val),
#         "aqi": str(aqi_val),
#         "status": status,
#         "trend_labels": ["3 AM", "6 AM", "9 AM", "12 PM", "3 PM", "Now"],
#         "trend_values": trend_vals,
#         "pred_labels": ["Now", "+1h", "+2h", "+3h", "+4h", "+5h", "+6h"],
#         "pred_values": pred_vals,
#     })
#   except Exception as e:
#     return jsonify({
#         "temperature": "28.0 °C",
#         "humidity": "60.0 %",
#         "mq135": "400",
#         "aqi": "40",
#         "status": "Normal",
#         "trend_labels": ["3 AM", "6 AM", "9 AM", "12 PM", "3 PM", "Now"],
#         "trend_values": [30, 35, 40, 45, 50, 42],
#         "pred_labels": ["Now", "+1h", "+2h", "+3h", "+4h", "+5h", "+6h"],
#         "pred_values": [42, 45, 50, 58, 65, 72, 80],
#     })


# if __name__ == "__main__":
#   app.run(debug=True, port=5000)
import os
import re
import time
from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/get_data")
def get_data():
  try:
    if not os.path.exists("air_pollution_data.csv"):
      return jsonify({"connected": False})

    # Check if CSV file was updated within the last 15 seconds
    file_mtime = os.path.getmtime("air_pollution_data.csv")
    is_connected = (time.time() - file_mtime) < 15

    df = pd.read_csv("air_pollution_data.csv", header=None)
    if df.empty:
      return jsonify({"connected": False})

    last_row = df.iloc[-1]
    row_str = " ".join(str(val) for val in last_row.values)

    temp_match = re.search(r"Temperature:\s*([\d\.]+)", row_str)
    hum_match = re.search(r"Humidity:\s*([\d\.]+)", row_str)
    mq_match = re.search(
        r"(?:Raw Value|MQ135):\s*(\d+)", row_str, re.IGNORECASE
    )

    temp = temp_match.group(1) + " °C" if temp_match else "28.0 °C"
    hum = hum_match.group(1) + " %" if hum_match else "60.0 %"
    mq_val = int(mq_match.group(1)) if mq_match else 400

    aqi_val = int(mq_val / 10)
    status = (
        "Normal"
        if aqi_val <= 50
        else ("Moderate" if aqi_val <= 100 else "Unhealthy")
    )

    return jsonify({
        "connected": is_connected,
        "temperature": temp,
        "humidity": hum,
        "mq135": str(mq_val),
        "aqi": str(aqi_val),
        "status": status,
    })
  except Exception as e:
    return jsonify({"connected": False})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)