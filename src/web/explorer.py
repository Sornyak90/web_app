from fastapi import APIRouter
from model.explorer import Explorer
import fake.explorer as service

router = APIRouter(prefix="/explorer")

@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Explorer | None:
    return service.get_one(name)

@router.post("/")
def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)

@router.patch("/{name}")
def modify(name) -> Explorer | None:
    return service.modify(name)

@router.put("/{name}")
def replace(name) -> Explorer | None:
    return service.replace(name)

@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)