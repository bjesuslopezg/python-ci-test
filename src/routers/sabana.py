from fastapi import APIRouter

# Evitar importa los repositorios 
#from repository.database import db_manager

router = APIRouter()

@router.get("/", response_model=str)
def saludo():
    return "Welcome"
