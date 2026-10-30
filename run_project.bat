@echo off
echo Starting AirGuard IoT Project...

:: 1. Background mein data logger start karein
start cmd /k "python data_logger.py"

:: 2. 2 seconds ka wait karein taaki Flask server ready ho jaye, phir browser khol dein
timeout /t 2 /nobreak >nul
start http://127.0.0.1:5000

:: 3. Flask server start karein (main window)
python app.py

pause