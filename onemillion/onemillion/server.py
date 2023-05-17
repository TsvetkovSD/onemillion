import uvicorn
from fastapi import FastAPI
from onemillion.routers import answers

app = FastAPI(title="One million users API", version="0.1.0")

app.include_router(answers.router)

if __name__ == "__main__":
    uvicorn.run(app, reload=True)