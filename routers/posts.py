from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Post(BaseModel):
    id: int
    title: str
    content: str

fake_db = {
    1: {"id": 1, "title": "First Post", "content": "This is the first post."},
    2: {"id": 2, "title": "Second Post", "content": "This is the second post."}
}

@router.get("/", response_model=list[Post])
async def get_posts():
    return list(fake_db.values())

@router.post("/", response_model=Post)
async def create_post(post: Post):
    if post.id in fake_db:
        raise HTTPException(status_code=400, detail="Post already exists.")
    fake_db[post.id] = post.dict()
    return post

@router.put("/{post_id}", response_model=Post)
async def update_post(post_id: int, post: Post):
    if post_id not in fake_db:
        raise HTTPException(status_code=404, detail="Post not found.")
    fake_db[post_id] = post.dict()
    return post

@router.delete("/{post_id}", response_model=Post)
async def delete_post(post_id: int):
    if post_id not in fake_db:
        raise HTTPException(status_code=404, detail="Post not found.")
    return fake_db.pop(post_id)
