from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Modèle de requête
class VideoRequest(BaseModel):
    video_url: str


# Route de test (GET)
@app.get("/")
def root():
    return {
        "message": "CreatorBoost API running successfully"
    }


# Route principale d'analyse
@app.post("/analyze")
def analyze_video(request: VideoRequest):
    # Simulation d'analyse vidéo
    # (Plus tard on pourra connecter une vraie IA)

    return {
        "video_url": request.video_url,

        # Statistiques principales
        "estimated_views": 5000,
        "engagement_score": 82,
        "viral_probability": 74,

        # Meilleur moment pour poster
        "best_post_time": "18:00",
        "best_day": "Tuesday",
        "time_range": "17:00 - 19:00",

        # Suggestions IA
        "suggestions": "Use trending music and post consistently",

        # Hashtags recommandés
        "hashtags": "#viral #fyp #trending #creatorboost"
    }
