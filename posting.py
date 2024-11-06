from pyrogram import Client, errors
import asyncio
import os

# Get credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")

# Message content and list of groups with Chat IDs
message_content = "https://t.me/mpgoviralgrowthtools (admin share 3 kali MP goviral setiap hari)"
groups = [
    -1001513360832, -1001656152814, -1002032128619, -1002065798504,
    -1002083219543, -1001473865431, -1001194015232, -1002080497857,
    -1001641889050, -1001338686972, -1002080593272, -1001778610644
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

# Main async function to setup client and start posting
async def main():
    async with Client("my_session", api_id=api_id, api_hash=api_hash, session_string=session_string) as app:
        tasks = [send_message(app, group_id) for group_id in groups]
        await asyncio.gather(*tasks)

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())
