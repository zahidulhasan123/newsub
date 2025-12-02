from locust import HttpUser, task, between
import json

# Example payload
payload = {
    "q1": "q1",
    "q2A": "q2A",
    "q2B": "q2B",
    "q2C": "q2C",
    "q3": "q3",
    "q4A": "q4A",
    "q4B": "q4B",
    "q4C": "q4C",
    "q4D": "q4D",
    "q4E": "q4E",
    "q4F": "q4F",
    "q4G": "q4G",
    "q5A": "q5A",
    "q5B": "q5B",
    "q5C": "q5C",
    "q6": "q6",
    "qE1": "qE1",
    "qE2": "qE2",
    "qE3": "qE3",
    "qE4": "qE4",
    "qE5": "qE5",
    "qE6": "qE6",
    "qE7": "qE7",
    "qE8": "qE8",
    "qE9": "qE9",
    "qE10": "qE10"
}

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxNDY1MzUzLCJpYXQiOjE3NjE0NjE3NTMsImp0aSI6ImUwNmM4ZWY5Nzc5MTQxMDA5NTAyN2FhNDJlNzUwYjZiIiwidXNlcl9pZCI6IjIifQ.XqwDQkTmkaWox2c98lWiFsSW9lJPAdYb-WlAhggjycg",
    "Accept-Encoding": "gzip"
}

class FormUser(HttpUser):
    wait_time = between(1, 3)  # seconds between tasks

    @task
    def submit_form(self):
        self.client.post(
            "/api/v1/institutes/",
            data=json.dumps(payload),
            headers=HEADERS
        )
