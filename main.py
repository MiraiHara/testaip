from fastapi import FastAPI
from connect import *

app = FastAPI()
# mydb, db = dbcon()

# @app.get("/getFromNAME/{name}")
# async def get_name(name: str):
#     data = []
#     sql = "SELECT * FROM color WHERE color.NAME = \'" + name + "\'"
#     db.execute(sql)
#     rows = db.fetchall()
#     for row in rows:
#         data.append(row['HEX'])
#     return data

# @app.get("/getFromHEX/{hex}")
# async def get_hex(hex: str):
#     data = []
#     sql = "SELECT * FROM color WHERE color.ID = \'" + str(int(hex, base=16)) + "\'"
#     db.execute(sql)
#     for row in db.fetchall():
#         data.append(row['NAME'])
#     return data

@app.get("/")
async def root():
    return {"message": "Hello World"}