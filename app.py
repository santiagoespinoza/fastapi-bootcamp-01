from fastapi import FastApi

app = FastAPI()

@app.get('/')
def root():
    return{
        "Hello":"World"
    }