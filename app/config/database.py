from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/test"

engine = create_engine(
    DATABASE_URL,
    echo=True
)
