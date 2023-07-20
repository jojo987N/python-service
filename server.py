from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg


class Item(BaseModel):
    name: str
    # description: str | None = None
    # price: float
    # tax: float | None = None

conn = psycopg.connect("dbname=mydb host='localhost' user=postgres password='nass'")
cur = conn.cursor()

# with psycopg.connect("dbname=mydb host='localhost' user=postgres password='nass'") as conn:

    # with conn.cursor() as cur:

        # Execute a command: this creates a new table
        # cur.execute("""
        #     CREATE TABLE test (
        #         id serial PRIMARY KEY,
        #         num integer,
        #         data text)
        #     """)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def root(item: Item):
    # cur.execute("SELECT * FROM news")
    a = "Exist"
    cur.execute("SELECT * FROM news WHERE journal = '%s' "%(item.name))
    # for record in cur:
    #     print(record, cur.fetchone())
    if cur.fetchone() == None:
        cur.execute(
            "INSERT INTO news (journal) VALUES ('%s') "%(item.name))
        a = "updated"

    # print(cur.rowcount)
    # cur.fetchall()
    conn.commit()
    return a

@app.get("/fetch")
async def fetch():
    return {"message": "Hello World"}
