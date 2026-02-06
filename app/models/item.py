from sqlmodel import SQLModel, Field

class ItemBase(SQLModel):
    name: str = Field()
    price: float = Field()
    stock: int = Field()

class ItemCreateIn(ItemBase): ...

class ItemCreateOut(SQLModel):
    id: int = Field()

class Item(ItemBase, table=True):
    id:int = Field(primary_key=True)
