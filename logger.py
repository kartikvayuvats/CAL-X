from datetime import datetime


def log_activity(message):
    with open("activity.log", "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{time}] {message}\n")