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
