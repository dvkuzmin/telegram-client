import uvicorn
from fastapi import FastAPI

from app.api.resources import telegram, parser

app = FastAPI()

app.include_router(telegram.router)
app.include_router(parser.router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app'
    )
