from typing import Annotated

from fastapi import APIRouter, Body

from app.utils import parse_page_html

router = APIRouter()


@router.post('/wild_goods')
async def get_wildberries_goods(wild: Annotated[str, Body(embed=True)]):
    print(wild)
    goods = parse_page_html(good=wild)
    return goods
