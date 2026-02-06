from sqlmodel import SQLModel, Field

class ItemBase(SQLModel): # item model, 3 columns
    name: str = Field()
    price: float = Field()
    stock: int = Field()

class ItemCreateIn(ItemBase): ... # add item to the database

class ItemCreateOut(SQLModel): # get items from DB
    id: int = Field()

class Item(ItemBase, table=True): # item model, it extends from ItemBase
    id:int = Field(primary_key=True)
