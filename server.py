from fastapi import FastAPI
from routes.root import root

app = FastAPI(
    title="API Binnace Alerts",
    version="v0.2.0"
)

app.include_router(root)