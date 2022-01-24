from fastapi import FastAPI, status, HTTPException
from typing import Optional

from fastapi.params import Depends
from . import schemas
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/about')
def about():
    return {
        "data": {
            "name": "Carlos Cativo",
            "age": 25
        }
    }


@app.get('/blog')
def all_blog(
        limit: int = 10,
        published: bool = True,
        sort: Optional[str] = None,
        db: Session = Depends(get_db)
):
    blogs = db.query(models.Blog).all()

    if published:
        # Only get 10 published blogs
        return {
            "data": blogs
        }
    # Only get 10 published blogs
    return {
        "data": blogs
    }


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def show(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if blog:
        return {"data": blog}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {
        "data": {
            "id": new_blog.id,
            "title": new_blog.title,
            "content": new_blog.body
        }
    }
