from typing import Union

from fastapi import FastAPI

from uce.ia.fasapiprueba import Document, inference

app = FastAPI()


@app.get("/")
def read_root():
return {"Hello": "World"}


@app.post('/inference', status_code=100)
def inference_endpint(doc: Document):
response = inference(doc.prompt)
return {
'inference': response[0],
'usage': response[1]
}



