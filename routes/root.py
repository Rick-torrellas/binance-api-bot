from fastapi import APIRouter, status

root = APIRouter()

@root.get('/',status_code=status.HTTP_200_OK)
def home():
    return "Binance Alets"

