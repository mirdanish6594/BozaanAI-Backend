# services/transcription_service.py
import whisper
import os
import tempfile
import io
from pydub import AudioSegment

# --- Ensure this path is 100% correct ---
ffmpeg_path = r"C:\Users\bilqu\Downloads\ffmpeg-7.0.2-essentials_build\ffmpeg-7.0.2-essentials_build\bin\ffmpeg.exe"
AudioSegment.converter = ffmpeg_path

# Load the Whisper model
print("Loading Whisper model...")
model = whisper.load_model("tiny")
print("Whisper model loaded successfully.")

def transcribe_audio(audio_file): # This function now expects the full UploadFile object
    """
    Transcribes an audio file using the Whisper model.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            # This line now works because audio_file has the .filename attribute
            original_filename = audio_file.filename
            input_path = os.path.join(temp_dir, original_filename)
            
            with open(input_path, "wb") as buffer:
                buffer.write(audio_file.file.read())
            print(f"1. Saved uploaded file to: {input_path}")

            output_wav_path = os.path.join(temp_dir, "output.wav")
            print(f"2. Will convert to: {output_wav_path}")

            print("3. Loading audio with pydub...")
            audio_segment = AudioSegment.from_file(input_path)

            print("4. Standardizing audio to 16kHz mono WAV...")
            audio_segment = audio_segment.set_frame_rate(16000).set_channels(1)

            print(f"5. Exporting standardized audio...")
            audio_segment.export(output_wav_path, format="wav")

            print("6. Running Whisper transcription...")
            result = model.transcribe(output_wav_path, fp16=False)
            transcript = result["text"]
            print(f"7. Transcription successful: {transcript[:50]}...")

            return transcript

        except Exception as e:
            print(f"---!!! AN ERROR OCCURRED !!!---")
            print(f"ERROR DETAILS: {e}")
            import traceback
            traceback.print_exc()
            print(f"---!!! END OF ERROR !!!---")
            return None