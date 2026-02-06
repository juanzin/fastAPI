from typing import Annotated, Generator
from fastapi import Depends
from sqlmodel import Session
from app.config.database import engine


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

session_dep = Annotated[Session, Depends(get_db)]
