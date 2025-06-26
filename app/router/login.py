
from fastapi import APIRouter

from app.login.db import User
from app.login.schemas import UserCreate, UserRead, UserUpdate
from app.login.users import auth_backend, current_active_user, fastapi_users

#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Not needed if you setup a migration system like Alembic
#     await create_db_and_tables()
#     yield


# app = FastAPI(lifespan=lifespan)
app = APIRouter()

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
