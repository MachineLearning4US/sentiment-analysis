import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# launch the server in this file

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")
