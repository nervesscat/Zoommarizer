from openai import OpenAI
import os

class OPENAICONN:
    def __init__(self):
        self.client = OpenAI()
        self.my_assistant = self.client.beta.assistants.retrieve("asst_Z3U7WzySbpYxv2cWPgv3kc4U")

    def getTranscript(self, audioFile):
        try:
            audio_file= open(audioFile, "rb")
            transcript = self.client.audio.transcriptions.create(model="whisper-1", file=audio_file)
            return transcript
        except Exception as e:
            print(f'Error: {e}')

    def createSummary(self, transcript):
        completion = self.client.chat.completions.create(
            model=self.my_assistant.model,
            messages=[
                {"role": "system", "content": self.my_assistant.instructions},
                {"role": "user", "content": transcript}])
        return completion.choices[0].message.content
 