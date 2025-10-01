from fastapi import APIRouter
from model.creature import Creature
import fake.creature as service

router = APIRouter(prefix="/creature")

@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Creature | None:
    return service.get_one(name)

@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)

@router.patch("/{name}")
def modify(name) -> Creature | None:
    return service.modify(name)

@router.put("/{name}")
def replace(name) -> Creature | None:
    return service.replace(name)

@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)