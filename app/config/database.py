from sqlmodel import SQLModel, create_engine, Session

SERVER = "mysql"
HOST = "localhost"
PORT = "3306"
TOOL = "pymysql"
DB_NAME = "test"
USER_NAME = "root"
PASSWORD = "root"

# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/test"
DATABASE_URL = SERVER + "+" + TOOL + "://" + USER_NAME + ":" + PASSWORD + "@" + HOST + ":" + PORT + "/" + DB_NAME

engine = create_engine(
    DATABASE_URL,
    echo=True
)
