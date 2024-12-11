from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from app.database.database import get_session
from app.schema.request.team.update_team import UpdateTeam
from app.services.team_service import TeamService
from app.routing.security.jwtmanager import JWTManager, oauth2_scheme


from app.schema.request.team.create_team import CreateTeam
team_router = APIRouter(prefix="/team", tags=["Team"])


@team_router.post("/create")
async def create_team(createRequest: CreateTeam, token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    created = await TeamService(session).create_team(createRequest, token)

    if not created.success:
        raise HTTPException(
            status_code=400, 
            detail=created.error
        )
    
    return created.value

@team_router.post("/update")
async def update_team(updateRequest: UpdateTeam, token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    updated = await TeamService(session).update_team(updateRequest, token)

    if not updated.success:
        raise HTTPException(
            status_code=400, 
            detail=updated.error
        )
    
    return updated.value