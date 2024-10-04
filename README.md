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

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to avoid conflicts between libraries. Here's how to create and activate a virtual environment:

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

All the necessary libraries are listed in the `requirements.txt` file. You can install them by running the following command:

```bash
pip install -r requirements.txt
```

This will automatically install the required libraries such as:
- **TensorFlow**
- **OpenCV**
- **MediaPipe**
- **Dlib**
- **Torch**
- **Face Recognition**

### 4. Running the Application

#### Backend (Server)
1. Navigate to the `server/` folder:
   ```bash
   cd server
   ```
2. Run the server application:
   ```bash
   python app.py
   ```

#### Device App
1. Navigate to `device_app/`:
   ```bash
   cd device_app
   ```
2. Run the device-side application:
   ```bash
   python src/main.py
   ```

### 5. Update `requirements.txt`

If you add new libraries during development, you can update the `requirements.txt` file using the following command:

```bash
pip freeze > requirements.txt
```

This will regenerate the `requirements.txt` file with the currently installed libraries and their versions.

---

## Documentation
Refer to the `docs/` folder for detailed API documentation, usage instructions, and more.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
