from telethon.sync import TelegramClient
import requests  # Для відправки в Google Apps Script

# Введи свої API-ключі
API_ID = 24020819
API_HASH = "ed8b3ab91235c4cedff2589fea6d0728"
PHONE_NUMBER = "+79996976430"  # Введи свій номер у Telegram

# Вебхук Google Apps Script (твій URL)
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbxi5W0tNwK1gzIDp5V78DdW8V2DQwvl1F7WrGIC866ordiX_i2T6-xjzWiEAMofJyv5xA/exec"

# Підключаємося до акаунта
client = TelegramClient("session_name", API_ID, API_HASH)

with client:
    dialogs = client.get_dialogs()  # Отримуємо всі чати, де ти підписаний

    for dialog in dialogs:
        if dialog.is_channel:  # Перевіряємо, чи це канал
            print(f"\n📢 Отримуємо повідомлення з: {dialog.title} | @{dialog.entity.username}")
            
            messages = client.get_messages(dialog, limit=5)  # Отримуємо 5 останніх повідомлень

            for message in messages:
                print("\n📩 Відправляємо в Google Таблицю:")
                print(f"🕒 Дата: {message.date}")
                print(f"📄 Текст: {message.text}")
                print(f"📝 Редаговано: {'Так' if message.edit_date else 'Ні'}")
                if message.reply_to_msg_id:
                    print(f"↩️ Це відповідь на повідомлення ID {message.reply_to_msg_id}")

                # Формуємо дані для відправки в Google Apps Script
                data = {
                    "channel": dialog.title,
                    "text": message.text or "",
                    "date": str(message.date),
                    "edited": "Так" if message.edit_date else "Ні",
                    "reply_to_msg_id": message.reply_to_msg_id or ""
                }

                # Відправляємо дані в Google Таблицю
                response = requests.post(WEBHOOK_URL, json=data)
                print(f"📤 Відповідь сервера: {response.text}")
