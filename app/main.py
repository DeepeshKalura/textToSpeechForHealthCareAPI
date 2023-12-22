from fastapi import Body, FastAPI
from fastapi.responses import FileResponse
from app.logic.audioFileLogic import audioFileProceesing
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]






app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Backend Client for the project"}


# @app.post("/audio")
# async def process_audio_endpoint(audio_file: UploadFile = File(...)):
#     return audioFileProceesing(audio_file)

class AudioRequestModel(BaseModel):
    audio_url: str





@app.post("/audio")
async def process_audio_endpoint(audio: AudioRequestModel = Body(...)):

    audioFileProceesing(audio.audio_url)
    return FileResponse("response.mp3", media_type="audio/mpeg")