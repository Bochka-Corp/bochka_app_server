from typing import Self

from pydantic import BaseModel

from bochka.service.schemas import user as svc_user


class UserRegister(BaseModel):
    first_name: str
    email: str
    password: str

    @staticmethod
    def to_service_model(user: "UserRegister") -> svc_user.UserRegister:
        return svc_user.UserRegister(
            first_name=user.first_name,
            email=user.email,
            password=user.password
        )


class UserLogin(BaseModel):
    email: str
    password: str

    @staticmethod
    def to_service_model(user: "UserLogin") -> svc_user.UserLogin:
        return svc_user.UserLogin(
            email=user.email,
            password=user.password
        )
