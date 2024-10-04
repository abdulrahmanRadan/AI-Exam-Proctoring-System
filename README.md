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