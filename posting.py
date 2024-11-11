from telethon import TelegramClient, errors
from telethon.sessions import StringSession  # Add this import
import asyncio
import os

# Get credentials from environment variables
api_id = int(os.getenv("API_ID"))  # Your API ID from Telegram
api_hash = os.getenv("API_HASH")  # Your API Hash from Telegram
session_string = os.getenv("SESSION_STRING")  # Your session string for the personal account

# Message content and list of groups with Chat IDs
message_content = """اَللهُمَّ صَلِّ عَلَى سَيِّدِنَا مُحَمَّدٍ وَعَلَى آلِ سَيِّدِنَا مُحَمَّدٍ
Allahumma salli 'ala Sayyidina Muhammad wa 'ala ali Sayyidina Muhammad"""
groups = [
    -1001161916810, -1001897381179, -1002056756757, -1001656152814, -1001641889050, 
    -1002032128619, -1001513360832, -1002083219543, -1001338686972, -1002080497857, 
    -1001194015232, -1002080593272, -1001473865431, -1002065798504, -1002329458039,
    -1002379900836, -1001192339217, -1001875616025, -1001938068566, -1001626914578, 
    -1002174886965, -1001965994500
]

# Function to send a message to a target chat
async def send_message(client, target_chat_id):
    try:
        # Attempt to send the message to each group
        await client.send_message(target_chat_id, message_content)
        print(f"Message sent to {target_chat_id}")
    except errors.PeerIdInvalidError:
        # Catch PeerIdInvalid error for invalid or inaccessible group IDs
        print(f"Error: Peer id invalid for group {target_chat_id}")
    except errors.ChatWriteForbiddenError:
        # Catch if the bot doesn't have permission to send messages to the group
        print(f"Error: No write access to group {target_chat_id}")
    except errors.FloodWaitError as e:
        # Handle Telegram's rate limit error
        print(f"Rate limited by Telegram. Waiting for {e.seconds} seconds.")
        await asyncio.sleep(e.seconds)  # Wait for the specified time
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An error occurred for group {target_chat_id}: {e}")

# Main async function to setup client and start posting
async def main():
    # Initialize Telethon client with the session string
    client = TelegramClient(StringSession(session_string), api_id, api_hash)
    async with client:
        # Create a list of tasks to send messages to all groups
        tasks = [send_message(client, group_id) for group_id in groups]
        await asyncio.gather(*tasks)  # Wait for all tasks to finish

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())  # Start the program
