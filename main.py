from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ ACTIVER CORS (TRÈS IMPORTANT POUR FLUTTERFLOW)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route test
@app.get("/")
def read_root():
    return {"message": "CreatorBoost API running"}

# Route principale analyse vidéo
@app.post("/analyze")
def analyze_video(data: dict):

    video_url = data.get("video_url")

    # ⚡ Simulation résultats (pour test FlutterFlow)
    return {
        "video_url": video_url,
        "estimated_views": 5000,
        "engagement_score": 82,
        "viral_probability": 74
    }
