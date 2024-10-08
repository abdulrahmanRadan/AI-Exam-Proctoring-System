import requests

def send_alert(student_id, alert_type, details):
    url = "http://server_address/send_alert"
    data = {
        "student_id": student_id,
        "alert_type": alert_type,
        "details": details
    }
    response = requests.post(url, json=data)
    return response.json()
