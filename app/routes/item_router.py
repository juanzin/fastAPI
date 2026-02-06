from fastapi import APIRouter
from app.models.item import Item, ItemCreateIn, ItemCreateOut
from app.routes.deps.db_session import session_dep
from sqlmodel import select

items_router = APIRouter(prefix="/items", tags=["item"])



@items_router.get("/")
def get_items(db: session_dep) -> list[Item]:
    statement = select(Item)
    result = db.exec(statement).all()
    return result


@items_router.post("/")
def add_item(db: session_dep, item: ItemCreateIn) -> ItemCreateOut:
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return ItemCreateOut(id = db_item.id)