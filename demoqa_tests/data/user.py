import dataclasses
from datetime import date


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: date
    month: str
    subjects: str
    hobbies1: str
    hobbies2: str
    hobbies3: str
    picture: str
    addrees: str
    state: str
    city: str
