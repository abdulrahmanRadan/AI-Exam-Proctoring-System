# AI Exam Proctoring System - Device App

This folder contains the client-side application that monitors students' behavior during the exam. It uses techniques like head pose estimation, eye gaze tracking, and posture analysis to detect suspicious actions.

## Directory Structure

```bash
device_app/
├── src/
│   ├── face_recognition.py
│   ├── head_pose_estimator.py
│   ├── eye_gaze_tracker.py
│   ├── posture_analyzer.py
│   └── alert_manager.py
├── utils/
├── data/
```

## Installation

1. Navigate to the `device_app` folder:
   ```bash
   cd device_app
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

To start the device-side application:
```bash
python src/main.py
```

## Features

- **Facial Recognition**: Verifies the student using face recognition technology.
- **Head Pose Estimation**: Detects and monitors head orientation to track focus.
- **Eye Gaze Tracking**: Analyzes where the student is looking to detect possible cheating attempts.
- **Posture Analysis**: Monitors body posture for unusual movements.

## Configuration

Ensure the configuration files in the `utils/` folder are set up correctly for device-specific parameters like camera input.
```

