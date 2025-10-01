from model.explorer import Explorer


_explorers = [
    Explorer(name="Claude Hande",
            country="FR",
            description="Scare during full moons"), 
    Explorer(name="Noah Weiser",
            country="DE",
            description="Myopic machete man"),
    ]

def get_all() -> list[Explorer]:
    return _explorers

def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def create(explorer: Explorer) -> Explorer:
    return explorer

def modify(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def replace(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def delete(name: str) -> bool:
    for _explorer in _explorers:
        if _explorer.name == name:
            return True
    return False



