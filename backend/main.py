from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "AI-Powered Predictive Maintenance System API is running!"}