from fastapi import FastAPI
import config
#from models.base import *
from routers import sabana, diplomado


app = FastAPI(
    title="Template Micro Service", 
    version="0.1.0"
)

app.include_router(sabana.router, prefix="/sabana", tags=["Sabana"]) 
app.include_router(diplomado.router, prefix="/diplomado", tags=["Diplomado"]) 
