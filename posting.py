from pyrogram import Client, errors
import asyncio

# Hardcoded credentials and session string
api_id = 20240995
api_hash = "a6cb8eb76c7e91215e483416a29dc0e0"
session_string = "BQE02mMAEQ83KHZ0hOUyHrS6nCpZSurJ6-xonZklz3Naht9WNBUEwbLSYMZ90aRd6xT0t9gpg5EvGyI2bGx0WiE23S4GREm_jwRKntRj_pM3megHDtyp9gAux_il7GyFZ5dR5lgG-1Z5xVVaGhX2wl3808Q8J2MMFumu8frRmglqDgW8jQ7HPiSzYZb2BvY3nFyEJuXUAEY70J084iQGGYUp1Mr6FyZWy-hQxNc6U8fny7URmfAQxwypyoUQpZqJ62ADgY3fIMRX-Z40AivqYXLw2X-wcml8Lih1ziDTiM0bjTo_p3mQuFKKM5jmB7btei5qHio3tVNSFys7C_C7j5P7GnBcsQAAAAAfcSmPAA"

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
    async with Client(session_string, api_id=api_id, api_hash=api_hash) as app:
        tasks = [send_message(app, group_id) for group_id in groups]
        await asyncio.gather(*tasks)

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())
