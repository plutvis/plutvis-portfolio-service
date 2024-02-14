from pydantic import BaseModel


class SignUpRequestBody(BaseModel):
    email: str
    password: str
    referralId: str