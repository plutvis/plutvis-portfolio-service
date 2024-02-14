from fastapi import APIRouter

from src.users.schemas import SignUpRequestBody

router = APIRouter(
    prefix='/api/v1/users',
    tags=['users']
)


# Project layout best practices https://github.com/Netflix/dispatch/blob/master/src/dispatch/main.py#L112C12-L112C58

@router.post("/")
async def signup(req: SignUpRequestBody):
    return req

