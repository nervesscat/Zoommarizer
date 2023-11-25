# Python code to convert video to audio
import moviepy.editor as mp

class VIDEO_CONVERTER:
    def convertToMP3(self, videoName):
        try:
            clip = mp.VideoFileClip(videoName)
            clip.audio.write_audiofile(videoName.replace('.mp4', '.mp3'))
        except Exception as e:
            print(f'Error: {e}')
        