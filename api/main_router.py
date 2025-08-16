# api/main_router.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from services import transcription_service, llm_service, tts_service
import io

router = APIRouter()

@router.post("/process-audio")
async def process_audio_endpoint(audio: UploadFile = File(...)):
    """
    This is the main endpoint that processes user audio.
    """
    # --- THE FIX IS HERE ---
    # We must pass the entire 'audio' object, not just 'audio.file'.
    transcript = transcription_service.transcribe_audio(audio)
    
    if not transcript:
        raise HTTPException(status_code=500, detail="Could not transcribe audio.")

    # Step 2: Generate AI reply
    ai_reply_text = llm_service.generate_ai_reply(transcript)
    
    # Step 3: Convert reply to speech
    ai_reply_audio_bytes = tts_service.convert_text_to_speech(ai_reply_text)
    if not ai_reply_audio_bytes:
        raise HTTPException(status_code=500, detail="Could not generate audio reply.")

    # Step 4: Stream the audio back to the frontend
    return StreamingResponse(io.BytesIO(ai_reply_audio_bytes), media_type="audio/mpeg")