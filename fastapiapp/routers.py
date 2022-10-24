from typing import List

from fastapi import APIRouter

from fastapiapp.schemas import PostRead, IdType, PostCreate

router = APIRouter()


@router.get('', response_model=List[PostRead])
async def get_posts():
    pass


@router.get('/{id}', response_model=PostRead)
async def get_post(id: IdType):
    pass


@router.post('/create', response_model=PostRead)
async def create_post(post: PostCreate):
    pass