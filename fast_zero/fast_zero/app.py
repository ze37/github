from fastapi import FastAPI
from http import HTTPStatus
app = FastAPI()
from fast_zero.schemas import Message

@app.get('/',status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
