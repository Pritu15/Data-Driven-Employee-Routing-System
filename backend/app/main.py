from fastapi import FastAPI

app=FastAPI(title="Data-Driven Employee Routing System")

@app.get("/health")
def health_check():
    return {"status": "ok"}