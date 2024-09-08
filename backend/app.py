from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from backend.auth import get_current_user
from backend.tenor_api import upload_to_tenor
from backend.models import Video, User, Subscription
from backend.db import SessionLocal, engine

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB and models initialization
@app.on_event("startup")
def startup_event():
    # Connect DB, create models, etc.
    pass

@app.post("/generate_gif/")
def generate_gif(video: Video, user: User = Depends(get_current_user)):
    # Code for video processing and GIF generation
    return {"message": "GIF generated"}

@app.post("/upload_tenor/")
def upload_gif_tenor(video_url: str, user: User = Depends(get_current_user)):
    upload_to_tenor(video_url)
    return {"message": "GIF uploaded to Tenor"}

@app.get("/subscription/")
def get_subscription(user: User = Depends(get_current_user)):
    subscription = Subscription.get_by_user(user.id)
    return {"subscription": subscription}
