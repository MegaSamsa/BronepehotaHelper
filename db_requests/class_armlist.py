from dataclasses import dataclass

# Класс армлистов
@dataclass
class Armlist:
    id: int
    name: str
    cost: int
    rank: int
    fraction_id: int
    image: bytes

# Класс техлистов
@dataclass
class Techlist:
    id: int
    name: str
    cost: int
    rank: int
    fraction_id: int
    image: bytes