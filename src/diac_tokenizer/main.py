from pydantic import BaseModel 
from fastapi import FastAPI
from diac_tokenizer.sentpiece import get_tokens

app = FastAPI()

class Request(BaseModel):
    text: str
class Response(BaseModel):
    tokens: list

@app.get('/')
def root():
    return {'message' : 'API is running'}

@app.post('/get_tokens' , response_model = Response)
def predict_endpoint(request: Request):
    pred = get_tokens(request.text)
    return {'tokens' : pred}