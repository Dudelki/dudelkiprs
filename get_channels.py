from telethon.sync import TelegramClient

# Введи свої API-ключі
API_ID = 24020819
API_HASH = "ed8b3ab91235c4cedff2589fea6d0728"
PHONE_NUMBER = "+79996976430"  # Введи свій номер у Telegram

# Підключаємося до акаунта
client = TelegramClient("session_name", API_ID, API_HASH)

with client:
    dialogs = client.get_dialogs()  # Отримуємо список діалогів

    print("\n📌 Список каналів, де ти підписаний:\n")
    for dialog in dialogs:
        if dialog.is_channel:
            print(f"🔹 Назва: {dialog.title} | Username: {dialog.entity.username}")
