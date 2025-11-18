from fastapi import Fastapi
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World!"}
