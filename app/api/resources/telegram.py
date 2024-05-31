from fastapi import APIRouter

from app.utils import login_tg_client, get_messages, send_message, check_login
from app.api.schemas import MessageData

router = APIRouter()


@router.get('/login')
async def login():
    qr_link_url = await login_tg_client()
    return {'qr_link_url': qr_link_url}


@router.get('/check/login')
async def check_client_login(phone: str):
    authorized = await check_login()
    return {f'client {phone} login status': authorized}


@router.get('/messages')
async def messages(phone: str, uname: str):
    try:
        result = await get_messages(user=uname)
        if result:
            return {'messages': result}
        return {'message': 'client is not authorized'}
    except Exception:
        result = await get_messages(user=phone)
        if result:
            return {'messages': result}
        return {'message': 'client is not authorized'}


@router.post('/messages')
async def messages_send(message: MessageData):
    try:
        res = await send_message(user=message.username, message=message.message_text)
        return {'status':  res}
    except Exception:
        await send_message(user=message.from_phone, message=message.message_text)
        return {'status': 'ok'}

