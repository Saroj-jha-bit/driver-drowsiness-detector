🚗 Driver Sleepiness Detector 😴
This project is a real-time driver drowsiness detection system that uses a webcam to monitor the driver's eye aspect ratio (EAR) and alert the driver if signs of sleepiness or fatigue are detected. It uses MediaPipe for face and eye landmark detection, and Pygame to play an alarm sound when the driver appears drowsy.

🔧 Features
Real-time video processing using OpenCV

Eye Aspect Ratio (EAR) calculation to detect eye closure

Drowsiness alert using sound (alarm.mp3)

Uses Mediapipe FaceMesh for accurate eye landmark detection

EAR Threshold and frame limit configurable

🧠 How It Works
Captures video from webcam.

Detects facial landmarks using MediaPipe's FaceMesh.

Tracks eye landmarks to calculate the EAR.

If EAR drops below a defined threshold for a certain number of frames, it triggers a drowsiness alert.

📸 Demo

A live view from the webcam with EAR displayed and alert message shown when drowsiness is detected.

⚙️ Installation
bash
Copy
Edit
git clone https://github.com/your-username/driver-sleepiness-detector.git
cd driver-sleepiness-detector
pip install -r requirements.txt
Dependencies:

OpenCV

Mediapipe

NumPy

Pygame

You can install them manually too:

bash
Copy
Edit
pip install opencv-python mediapipe numpy pygame
📁 Usage
Replace alert.mp3 with your preferred alarm sound in the same directory.

Run the script:

bash
Copy
Edit
python drowsiness_detector.py
Press q to quit the application.

🧪 Configuration
EAR_THRESHOLD: Controls how low the eye aspect ratio must go before drowsiness is suspected. Default is 0.22.

DROWSY_THRESHOLD: Number of consecutive frames with low EAR before an alert is raised. Default is 50.

alert_cooldown: Cooldown (in seconds) between alarm sounds. Default is 5.

📦 Folder Structure
bash
Copy
Edit
driver-sleepiness-detector/
│
├── drowsiness_detector.py
├── alert.mp3
├── README.md
💡 Improvements You Can Add
Add Yawn Detection using lip landmarks

Connect it to car speaker or display system

Add GUI for settings (Tkinter/PyQt)

Export drowsiness logs for monitoring

📜 License
This project is for educational purposes and provided under the MIT License.

🙋‍♂️ Author
Saroj Jha
A B.Tech CSE student exploring the world of AI, CV, and real-time safety systems.
