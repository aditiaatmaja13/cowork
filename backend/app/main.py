from fastapi import FastAPI

app = FastAPI(title="CoWork API")


@app.get("/")
def root():
    return {"message": "CoWork API running"}