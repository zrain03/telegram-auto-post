from pyrogram import Client, errors
import asyncio
import os

# Get credentials from environment variables
api_id = int(os.getenv("API_ID"))  # Your API ID from Telegram
api_hash = os.getenv("API_HASH")  # Your API Hash from Telegram
session_string = os.getenv("SESSION_STRING")  # Your session string for the personal account

# Message content and list of groups with Chat IDs
message_content = "https://t.me/mpgoviralgrowthtools (admin share 3 kali MP goviral setiap hari)"
groups = [
    -1001161916810, -1001897381179, -1002056756757, -1001656152814, -1001641889050, 
    -1002032128619, -1001513360832, -1002083219543, -1001338686972, -1002080497857, 
    -1001194015232, -1002080593272, -1001473865431, -1001778610644, -1002065798504, 
    -1002379900836, -1001192339217, -1001875616025, -1001938068566, -1001626914578, -1002174886965, -1001965994500
]

# Function to send a message to a target chat
async def send_message(app, target_chat_id):
    try:
        # Attempt to send the message to each group
        await app.send_message(target_chat_id, message_content)
        print(f"Mesej dihantar ke {target_chat_id}")
    except errors.PeerIdInvalid:
        # Catch PeerIdInvalid error for invalid or inaccessible group IDs
        print(f"Error: Peer id invalid for group {target_chat_id}")
    except errors.ChatWriteForbidden:
        # Catch if the bot doesn't have permission to send messages to the group
        print(f"Error: No write access to group {target_chat_id}")
    except errors.FloodWait as e:
        # Handle Telegram's rate limit error
        print(f"Rate limited by Telegram. Waiting for {e.x} seconds.")
        await asyncio.sleep(e.x)  # Wait for the specified time
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An error occurred for group {target_chat_id}: {e}")

# Main async function to setup client and start posting
async def main():
    # Use the personal account session string and login credentials
    async with Client("my_session", api_id=api_id, api_hash=api_hash, session_string=session_string) as app:
        # Create a list of tasks to send messages to all groups
        tasks = [send_message(app, group_id) for group_id in groups]
        await asyncio.gather(*tasks)  # Wait for all tasks to finish

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())  # Start the program
