from dataclasses import dataclass


@dataclass
class Mek:
    age: int
    name: str
    breed: str


Lesya = Mek(
    age=5,
    name='Lesya',
    breed='Domestic'
)

print(Lesya.name)
