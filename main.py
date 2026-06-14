from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend Kas RW Berjalan"}