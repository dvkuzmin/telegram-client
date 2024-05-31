from telethon import TelegramClient

from .qr_code_image import display_url_as_qr
from app.config import config


client = TelegramClient('client_session', api_id=config.API_ID, api_hash=config.API_HASH)


async def login_tg_client():
    """Получение QR кода от телеграм, отрисовка  и возвращение url для авторизации"""
    if not client.is_connected():
        await client.connect()
    qr_login = await client.qr_login()
    flag = False
    login_url = qr_login.url
    display_url_as_qr(login_url)

    while not flag:
        try:
            flag = await qr_login.wait(10)
        except:
            pass

    return login_url


async def get_messages(user: str):
    """Получение 50 сообщений от указанного пользователя"""
    if not client.is_connected():
        await client.connect()
    if await client.is_user_authorized():
        chat_result = []
        me = await client.get_me()
        my_id = me.id

        async for message in client.iter_messages(user, limit=50):
            sender = await message.get_sender()
            sender_name = f'{sender.first_name} {sender.last_name}' if sender else 'Unknown'
            chat_result.append({'username': sender_name,
                                'is_self': message.sender_id == my_id,
                                'message_text': message.text})
        return chat_result


async def send_message(user: str, message: str):
    """Отправка сообщения указанному пользователю"""
    if not client.is_connected():
        await client.connect()
    if await client.is_user_authorized():
        await client.send_message(user, message)
        return 'ok'
    return 'client is not authorized'


async def check_login():
    """Проверка авторизации клиента"""
    if not client.is_connected():
        await client.connect()
    return await client.is_user_authorized()
