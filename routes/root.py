from fastapi import APIRouter, status
from models.Kline import Kline
from schemas.kline import klineEntity,klinesEntity
from config.mongodb import conection

database = conection.local.kline

root = APIRouter()

@root.get('/',status_code=status.HTTP_200_OK)
def home():
    return "Binance Alets"

@root.get('/klines')
async def getAllKlines():
    return klinesEntity(database.find())

@root.post('/generate')
async def generate(kline: Kline):
    new_user = dict(kline)
    del new_user["id"]
    id = database.insert_one(new_user).inserted_id
    kline = database.find_one({"_id": id}) # type: ignore
    return klineEntity(kline)