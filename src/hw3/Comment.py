from pydantic import BaseModel
form hw3.Post import Post

class Comment(BaseModel):
    postId: Post
    id: str
    name: str
    email: str
    body: str

