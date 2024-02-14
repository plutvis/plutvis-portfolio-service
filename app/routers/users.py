from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/api/v1/users',
    tags=['users']
)


class SignUpRequestBody(BaseModel):
    email: str
    password: str
    referralId: str


@router.post("/")
async def signup(req: SignUpRequestBody):
    return req

