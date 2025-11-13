from fastapi import FastAPI, HTTPException
from core.function import caesar

app = FastAPI()
texts = []
ciphertexts=[]
@app.get("/")
def root():
    return {"msg":"hi from test"}

@app.post("/items/")
def create_text(text: str,offset:int,id:int,mode:bool):
    new_text = {"text":text,"offset":offset,"mode":mode,"id":id}
    
    texts.append(new_text)
    return new_text

@app.get("/items/")
def read_texts():
    return texts

@app.get("/items/{text_id}")
def read_text(text_id: int):
    for t in texts:
        if t["id"] == text_id:
            return t
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/search/")
def search_texts(q: str = None):
    if q is None:
        return {"results": texts}
    filtered = [itm for itm in texts if q in itm["name"]]
    return {"query": q, "results": filtered}

@app.put("/items/{item_id}")
def update_text(item_id: int, text: str):
    for t in texts:
        if t["id"] == item_id:
            t["text"] = text
            return text
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{text_id}")
def delete_text(text_id: int):
    for i, t in enumerate(texts):
        if t["id"] == text_id:
            return texts.pop(i)
    raise HTTPException(status_code=404, detail="Item not found")