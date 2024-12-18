
from sqlalchemy.exc import IntegrityError
from app.database.models.models import User
from app.database.repo.user_repository import UserRepository
from sqlalchemy.orm import Session
from app.schema.request.get_access import authorize, register
from app.schema.request.account.updateprofile import UpdateProfile
from app.utils.result import Result, err, success
from app.routing.security.hasher import hash_password, verify_password
from app.routing.security.jwtmanager import JWTManager
from app.utils.logger.logger import logger, log_info_with_separator

class UserService:

    def __init__(self, session: Session):
        self._session = session
        self._repo: UserRepository = UserRepository(session)


    async def update_profile(self, token: str, update_request: UpdateProfile):
        user: User = await JWTManager().get_current_user(token, self._session)
        await self._repo.update_profile()

    async def register(self, register_request: register.RegisterRequest) -> Result[None]:
        try:
            user = await self._repo.create(email=register_request.email, password=hash_password(register_request.password))
            return success(user)
        except IntegrityError:
            return err("User already exists")
        except Exception as e: 
            log_info_with_separator(str(e))
            return success("Some error while attemping resource.")
        
    async def authorize(self, email: str, password: str) -> Result[None]:
        authenticated: Result = await self._repo.authenticate_user(email, password)
        if authenticated.error:
            return err(authenticated.error)
        
        payload: dict = {
            "userId": str(authenticated.value.userId),
            "email": authenticated.value.email
        }

        return success(JWTManager().encode_token(payload))

    async def delete_profile(self, token: str):
        user: User = await JWTManager().get_current_user(token, self._session)
        return await self._repo.delete_by_id(user.userId)