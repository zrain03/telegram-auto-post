from pyrogram import Client, errors
import asyncio
import os
from datetime import datetime

# Get credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")

# Message content and list of groups with Chat IDs (updated list)
message_content = "https://t.me/mpgoviralgrowthtools (admin share 3 kali MP goviral setiap hari)"
groups = [
    -1002288720559, -1001161916810, -1001656152814, -1001513360832,
    -1001338686972, -1002083219543, -1002080593272, -1001641889050,
    -1002032128619, -1001473865431, -1002080497857, -1001194015232,
    -1002200241778, -1002247030893, -1002452835138, -1002056756757,
    -1001778610644  # New group added
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

# Check if the current time is within the 30-minute time window (e.g., 8:30 PM to 8:59 PM)
def check_if_in_time_window():
    current_time = datetime.now()
    # Allow posting between the 30th minute of the hour and 59th second (e.g., 8:30 PM to 8:59 PM)
    return current_time.minute == 30  # Only post during the 30th minute of each hour

# Main async function to setup client and start posting
async def main():
    # If manually triggered, allow posting regardless of the time window
    if check_if_in_time_window() or True:  # Force posting for manual runs
        async with Client("my_session", api_id=api_id, api_hash=api_hash, session_string=session_string) as app:
            tasks = [send_message(app, group_id) for group_id in groups]
            await asyncio.gather(*tasks)
    else:
        print("Not posting now, waiting for the right time.")

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())
