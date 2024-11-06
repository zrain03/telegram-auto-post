from pyrogram import Client, errors
import asyncio
import os

# Fetch API credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

# Message content with clickable link
message_content = "https://t.me/mpgoviralgrowthtools (admin share 3 kali MP goviral setiap hari)"

# List of groups with Chat IDs
groups_2_minutes = {
    "CONTEST 4: CERPEN chat": -1002189035002,
    "sarahh": -1002452835138,
}

groups_1_hour = {
    "mpgoviralgrowthtools": -1001513360832,
    "Group 2": -1001656152814,
    "Group 3": -1002032128619,
    "Group 4": -1002065798504,
    "Group 5": -1002083219543,
    "Group 6": -1001473865431,
    "Group 7": -1001194015232,
    "Group 8": -1002080497857,
    "Group 9": -1001641889050,
    "Group 10": -1001338686972,
    "Group 11": -1002080593272,
    "GROUP BUAT DUIT TANPA MODAL 2022 💰💰": -1001778610644,
    "Group 13": -1001161916810,
    "Group 14": -1002056756757,
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

# Loop for sending messages every 2 minutes to specific groups
async def post_to_2_minutes_groups(app):
    while True:
        tasks = [send_message(app, group_id) for group_id in groups_2_minutes.values()]
        await asyncio.gather(*tasks)
        await asyncio.sleep(120)  # Wait 2 minutes

# Loop for sending messages every 1 hour to other groups
async def post_to_1_hour_groups(app):
    while True:
        tasks = [send_message(app, group_id) for group_id in groups_1_hour.values()]
        await asyncio.gather(*tasks)
        await asyncio.sleep(3600)  # Wait 1 hour

# Main async function to setup client and start posting
async def main():
    async with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
        await asyncio.gather(
            post_to_2_minutes_groups(app),
            post_to_1_hour_groups(app)
        )

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())
