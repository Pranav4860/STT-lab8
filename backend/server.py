from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from elasticsearch import Elasticsearch
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "http://elasticsearch:9200")
es = Elasticsearch([ELASTICSEARCH_HOST])
index_name = "india"

def create_index():
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body={
            "mappings": {
                "properties": {
                    "id": {"type": "keyword"},
                    "text": {"type": "text"}
                }
            }
        })

create_index()
@app.get("/insert/{query}")
def insert_document(query: str):
    doc_id = str(hash(query))
    doc = {"id": doc_id, "text": query}
    res = es.index(index=index_name, id=doc_id, document=doc)
    return {"result": res["result"], "id": doc_id}

@app.get("/get/{query}")
def get_document(query: str):
    res = es.search(index=index_name, body={"query": {"match": {"text": query}}})
    return {"hits": res["hits"]["hits"]}

