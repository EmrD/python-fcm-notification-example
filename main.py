import firebase_admin
from firebase_admin import credentials, messaging
import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
import time

cred = credentials.Certificate("serviceAccountKey.json")

def send_notification():
    firebase_admin.initialize_app(cred)

    message = messaging.Message(
        notification=messaging.Notification(
            title="TITLE",
            body="CONTENT",
        ),
        topic="topic",
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)

def control_data():
    try:
        response = requests.get("YOUR URL TO CONTROL")
        if response.status_code == 200:
            send_notification()
        else:
            print("Sunucu çalışmıyor")
    except ConnectionError:
        print("Bağlantı hatası: Sunucuya ulaşılamıyor.")
    except Timeout:
        print("Zaman aşımı hatası: Sunucu yanıt vermiyor.")
    except RequestException as e:
        print(f"Bir hata oluştu: {e}")

check_interval_hours = 5

check_interval_seconds = check_interval_hours * 60 * 60

while True:
    control_data()
    time.sleep(check_interval_seconds)
