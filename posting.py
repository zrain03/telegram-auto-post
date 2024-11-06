from pyrogram import Client, errors
import asyncio
import os

# Fetch API credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")

# Message content with clickable link
message_content = "https://t.me/mpgoviralgrowthtools (admin share 3 kali MP goviral setiap hari)"

# List of groups with Chat IDs
groups = {
    "Group 1": -1001513360832,
    "Group 2": -1001656152814,
    # Add more groups as needed
}

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

# Main async function to setup client and start posting
async def main():
    async with Client(session_string, api_id=api_id, api_hash=api_hash) as app:
        tasks = [send_message(app, group_id) for group_id in groups.values()]
        await asyncio.gather(*tasks)

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())
