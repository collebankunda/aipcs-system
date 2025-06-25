
import datetime

activity_logs = []

def log_activity(user: str, action: str):
    activity_logs.append({
        "user": user,
        "action": action,
        "timestamp": datetime.datetime.now().isoformat()
    })

def get_logs():
    return activity_logs
