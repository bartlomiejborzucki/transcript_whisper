from datetime import timedelta
import os
import whisper
import argparse

parser = argparse.ArgumentParser(description='Transcribe audio and create subtitles')
parser.add_argument('path', type=str, help='path to the audio file')
args = parser.parse_args()

def create_model():
    return whisper.load_model("medium", "cpu")

def transcribe_audio(path):
    model = create_model()
    return model.transcribe(path)

def create_transcript_file(transcription, path):
    base_path = os.path.splitext(path)[0]
    transcript_suffix = '_transcript.txt'
    transcript_path = base_path + transcript_suffix
    with open(transcript_path, "w", encoding='utf-8') as file:
        file.write(transcription['text'])

def create_subtitles(transcription, path):
    segments = transcription['segments']
    base_path = os.path.splitext(path)[0]
    subtitle_suffix = '_subtitles.srt'
    subtitle_path = base_path + subtitle_suffix
    with open(subtitle_path, 'w', encoding='utf-8') as srtFile:
        for segment in segments:
            start_time = timedelta(seconds=int(segment['start']))
            end_time = timedelta(seconds=int(segment['end']))
            text = segment['text'].lstrip()
            segment_id = segment['id'] + 1
            segment_text = f"{segment_id}\n{start_time} --> {end_time}\n{text}\n\n"
            srtFile.write(segment_text)

transcription = transcribe_audio(args.path)
create_transcript_file(transcription, args.path)
create_subtitles(transcription, args.path)