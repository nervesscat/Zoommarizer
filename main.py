import argparse
from VideoConverter import VIDEO_CONVERTER
from OpenAiConn import OPENAICONN

def convertMp4ToMp3(videoName):
    video = VIDEO_CONVERTER()
    video.convertToMP3(videoName)
    videoName = videoName.split('.')[0]
    mp3ToText(videoName + '.mp3')

def mp3ToText(audioName):
    openai = OPENAICONN()
    transcript = openai.getTranscript(audioName)
    with open('transcript.txt', 'w') as f:
        f.write(transcript.text)
    summary = openai.createSummary(transcript.text)
    with open('summarize.md', 'w') as f:
        f.write(summary)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', help='Video file name')
    args = parser.parse_args()
    if args.video:
        convertMp4ToMp3(args.video)
    else:
        print('Please provide a video file name')
