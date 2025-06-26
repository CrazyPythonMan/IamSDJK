import uvicorn
from fastapi import Depends, FastAPI

from app.login.db import User
from app.login.schemas import UserCreate, UserRead, UserUpdate
from app.login.users import auth_backend, current_active_user, fastapi_users
from app.router.login import app as login_router_demo
#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Not needed if you setup a migration system like Alembic
#     await create_db_and_tables()
#     yield


# app = FastAPI(lifespan=lifespan)
app = FastAPI()
app.include_router(login_router_demo, tags=["auth"])


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)