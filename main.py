from fastapi import FastAPI

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