from pyrogram import Client
import time

api_id = 20240995  # ID API anda
api_hash = "a6cb8eb76c7e91215e483416a29dc0e0"
phone_number = "+60194848631"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

target_chat_id = -1002452835138  # ID grup yang disahkan
message_content = "Ini adalah mesej automatik dihantar setiap 2 minit."

def send_message():
    with app:
        app.send_message(target_chat_id, message_content)
        print(f"Mesej dihantar ke {target_chat_id}")

def auto_post_every_2_minutes():
    while True:
        send_message()
        time.sleep(120)  # Jeda selama 120 saat (2 minit)

if __name__ == "__main__":
    auto_post_every_2_minutes()
