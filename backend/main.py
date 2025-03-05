from fastapi import FastAPI
app = FastAPI()

items = ['hi', 'my']


@app.get("/")
def health():
    return {"items": items}