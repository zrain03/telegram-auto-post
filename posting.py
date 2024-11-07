from pyrogram import Client, errors
import asyncio
import os
from datetime import datetime

# Get credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")

# Message content and list of groups with Chat IDs
message_content = "https://t.me/mpgoviralgrowthtools (admin share 3 kali MP goviral setiap hari)"
groups = [
    -1002288720559, -1001161916810, -1001656152814, -1001513360832,
    -1001338686972, -1002083219543, -1002080593272, -1001641889050,
    -1002032128619, -1001473865431, -1002080497857, -1001194015232,
    -1002200241778, -1002247030893, -1002452835138, -1002056756757
]

# Function to send a message to a target chat
async def send_message(app, target_chat_id):
    try:
        await app.send_message(target_chat_id, message_content)
        print(f"Mesej dihantar ke {target_chat_id}")
    except errors.FloodWait as e:
        print(f"Rate limited by Telegram. Waiting for {e.x} seconds.")
        await asyncio.sleep(e.x)
    except Exception as e:
        print(f"An error occurred: {e}")

# Check if the current time is between 7:59:00 PM and 8:01:00 PM (Malaysia Time)
def check_if_in_time_window():
    current_time = datetime.now()
    # Allow posting between the last minute of the hour and the first minute of the next hour
    return current_time.minute == 59 or current_time.minute == 0  # 7:59 PM to 8:01 PM

# Main async function to setup client and start posting
async def main():
    if check_if_in_time_window():  # Run posting process between 7:59 PM and 8:01 PM
        async with Client("my_session", api_id=api_id, api_hash=api_hash, session_string=session_string) as app:
            tasks = [send_message(app, group_id) for group_id in groups]
            await asyncio.gather(*tasks)
    else:
        print("Not posting now, waiting for the right time.")

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())
