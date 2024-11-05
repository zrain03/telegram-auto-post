from pyrogram import Client
import os
import time

# Use environment variables for API ID, API Hash, and phone number
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")

# Create a session name (can be anything, but must be consistent)
session_name = "my_account"

app = Client(session_name, api_id=api_id, api_hash=api_hash)

target_chat_id = -1002452835138  # Replace with your actual target chat ID
message_content = "Ini adalah mesej automatik dihantar setiap 2 minit."

def send_message():
    with app:
        app.send_message(target_chat_id, message_content)
        print(f"Mesej dihantar ke {target_chat_id}")

def auto_post_every_2_minutes():
    while True:
        send_message()
        time.sleep(120)  # Delay for 120 seconds (2 minutes)

if __name__ == "__main__":
    auto_post_every_2_minutes()
