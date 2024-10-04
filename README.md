
# AI Exam Proctoring System

This project aims to build an **AI-driven exam proctoring system** to ensure fairness and integrity during exams. It is divided into two main components: the **server** (for backend management and monitoring) and the **device app** (for monitoring student behavior during exams).

## Project Structure
```bash
AI-Exam-Proctoring-System/
├── server/
│   ├── app/
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── database/
│   └── tests/
├── device_app/
│   ├── src/
│   ├── utils/
│   ├── data/
├── lib/
└── docs/
```

## Features
- **Student Identity Verification**: Uses facial recognition to authenticate students.
- **Behavior Monitoring**: Tracks student posture, head movements, and gaze direction to detect suspicious behavior.
- **Alert System**: Sends real-time alerts to the server in case of suspicious actions.
- **Reports**: Generates detailed reports for supervisors.

## Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/abdulrahmanRadan/AI-Exam-Proctoring-System.git
cd AI-Exam-Proctoring-System
```

### 2. Install Dependencies

#### Backend (Server)
```bash
cd server
# Install required Python packages
pip install -r requirements.txt
```

#### Device App
You may need to install dependencies for the device-side application. Navigate to `device_app/` and follow the appropriate installation process, such as for a Python or other language setup.

## Running the Application

### Backend (Server)
1. Navigate to the `server/` folder:
   ```bash
   cd server
   ```
2. Run the application:
   ```bash
   python app.py
   ```

### Device App
1. Navigate to `device_app/`:
   ```bash
   cd device_app
   ```
2. Run the application:
   ```bash
   python src/main.py
   ```

## Documentation
Refer to the `docs/` folder for detailed API documentation, usage instructions, and more.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### `server/README.md`:

```markdown
# AI Exam Proctoring System - Server

This folder contains the backend components of the AI-driven exam proctoring system. It manages student registration, authentication, monitoring, and alert handling.

## Directory Structure

```bash
server/
├── app/
│   ├── controllers/
│   ├── models/
│   ├── services/
│   ├── routes/
├── database/
│   ├── migrations/
│   ├── seeders/
├── tests/
└── app.py
```

## How to Set Up

1. Navigate to the `server` folder:
   ```bash
   cd server
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database (e.g., using SQLite or PostgreSQL). Run migrations and seeders:
   ```bash
   python manage.py db migrate
   python manage.py db seed
   ```

4. Start the server:
   ```bash
   python app.py
   ```

## API Endpoints

### Student Authentication
- **POST** `/api/authenticate`: Authenticates a student via facial recognition.

### Behavior Monitoring
- **POST** `/api/monitor`: Sends real-time monitoring data from the student’s device.

### Alerts
- **GET** `/api/alerts`: Retrieves all alerts triggered during the exam session.

For more detailed API documentation, refer to the `docs/` folder.

## Testing

To run tests:
```bash
pytest
```

```

### `device_app/README.md`:

```markdown
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

