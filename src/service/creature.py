from src.models import Creature
import src.fake.creature as data

def get_all() -> list[Creature]:
    return data.get_all()

def get_one(name: str) -> Creature | None:
    return data.get_one(id)

def create(creature: Creature) -> Creature:
    return data.create(creature)

def modify(id, creature: Creature) -> Creature | None:
    return data.modify(id, creature)

def replace(id, creature: Creature) -> Creature | None:
    return data.replace(id, creature)

def delete(id, creature: Creature) -> bool:
    return data.delete(id)