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
