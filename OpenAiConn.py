from openai import OpenAI
import os

class OPENAICONN:
    def __init__(self):
        self.client = OpenAI()

    def getTranscript(self, audioFile):
        try:
            audio_file= open(audioFile, "rb")
            transcript = self.client.audio.transcriptions.create(model="whisper-1", file=audio_file)
            return transcript
        except Exception as e:
            print(f'Error: {e}')
    
 