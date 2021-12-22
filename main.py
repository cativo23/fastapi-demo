from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {
        'data': {
            'message': "Hello World!"
        }
    }

@app.get('/about')
def about():
    return {
        "data": {
            "name": "Carlos Cativo",
            "age": 25
        }
    }

@app.get('/blog')
def blog(limit: int = 10, published: bool = True, sort: Optional[str] = None):

    if published:
      #Only get 10 published blogs
        return {
            "data": f'List of {limit} published blog(s)'
        }  
    else:
        #Only get 10 published blogs
        return {
            "data": f'List of {limit} unpublished blog(s)'
        }
    

@app.get('/blog/unpublished')
def unpublished():
    #TODO: Fetch blog with id = id
    return {
        "data": "unplublished list"
    }

@app.get('/blog/{id}')
def show(id: int):
    #TODO: Fetch blog with id = id
    return {
        "data": id
    }

@app.get('/blog/{id}/comment')
def comments(id: int):
    #TODO: Fetch messages for blog with id = id
    return {
        "data": {
            "comments": [
                {
                    "id": 12,
                    "text": "Text"
                }
            ],
        }
    }

class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool]



@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'blog created with title: {blog.title}'}