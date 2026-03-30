from fastapi import FastAPI

app = FastAPI()

# Route principale
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Route analyze (IMPORTANT)
@app.post("/analyze")
def analyze_video(data: dict):
    video_url = data.get("video_url")

    return {
        "status": "success",
        "video_url": video_url,
        "analysis": "Analyse test réussie"
    }
