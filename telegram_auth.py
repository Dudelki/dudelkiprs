from telethon.sync import TelegramClient

# Введи свої API-ключі (тільки не змінюй лапки!)
API_ID = 24020819
API_HASH = "ed8b3ab91235c4cedff2589fea6d0728"
PHONE_NUMBER = "+79996976430"  # Введи свій номер у Telegram

# Створюємо клієнт Telegram
client = TelegramClient("session_name", API_ID, API_HASH)

async def main():
    await client.send_message("me", "✅ Підключення успішне! 🎉")

with client:
    client.loop.run_until_complete(main())

print("✅ Підключення завершено! Перевір особисті повідомлення у Telegram.")
