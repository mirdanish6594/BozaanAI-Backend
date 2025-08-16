# services/tts_service.py
from gtts import gTTS
import io

def convert_text_to_speech(text):
    """
    Converts text to speech using gTTS and returns the audio as bytes.
    """
    try:
        # Use 'ur' (Urdu) as a fallback for Kashmiri pronunciation
        tts = gTTS(text, lang='ur', slow=False)
        
        # Save the audio to a bytes buffer in memory instead of a file
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0) # Go to the beginning of the buffer
        
        return audio_fp.read()
    except Exception as e:
        print(f"Error during TTS conversion: {e}")
        return None