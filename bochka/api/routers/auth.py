from datetime import timedelta
from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

from bochka.api.dependencies.session import get_sync_session
from bochka.api.schemas.user import UserRegister, UserLogin
from bochka.service.auth.create_user_command import CreateUserCommand
from bochka.service.auth.read_user_query import ReadUserQuery
from bochka.settings.auth import auth_settings
from bochka.utils.jwt import create_access_token

router = APIRouter(
    prefix="auth",
    tags=["auth"],
    include_in_schema=False,
)


@router.post(
    "/register",
    status_code=HTTPStatus.CREATED
)
def register(user: UserRegister, session: Session = Depends(get_sync_session)) -> None:
    command = CreateUserCommand(UserRegister.to_service_model(user), session)

    command.execute()


@router.post(
    "/login"
)
def login(user: UserLogin, session: Session = Depends(get_sync_session)) -> Response:
    query = ReadUserQuery(user, session)
    if query.login():
        access_token_expires = timedelta(minutes=auth_settings.access_token_expire_minutes)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )

        response = Response(status_code=200)
        response.set_cookie(
            key="access_token",
            value=f"Bearer {access_token}",
            max_age=1800,
            expires=1800,
        )
        return response
    else:
        return Response(status_code=401)
