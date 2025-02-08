from fastapi import FastAPI
from app.api.v1.routes import router as api_router

app = FastAPI(title="Flashcard Generator API")

# Register the API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the Flashcard Generator API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)