# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.main_router import router as main_api_router

# Create the FastAPI app instance
app = FastAPI(
    title="Kashmiri AI Voice Assistant API",
    description="Backend for the voice-first AI assistant.",
    version="1.0.0"
)

# --- CORS (Cross-Origin Resource Sharing) ---
# This is crucial to allow your React frontend (running on a different port)
# to communicate with this backend.
origins = [
    "http://localhost:3000",  # Your React app's local development URL
    "http://localhost:5173",  # Another common React dev port (Vite)
    # Add your deployed frontend URL here later
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API router
app.include_router(main_api_router, prefix="/api", tags=["Main"])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Kashmiri AI Voice Assistant API!"}