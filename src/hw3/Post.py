from pydantic import BaseModel

# Пользователи: id от 1 до 10
class Post(BaseModel):
    id: int
    title: str
    body: str
    userId: int

