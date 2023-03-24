# Audio transcription and subtitle creation script

This Python script transcribes an audio file and creates subtitles in SRT format. It uses the [Whisper Speech Recognition API](https://whisper.ai/) for the transcription.

## Requirements

Before using the script, make sure that you have Python 3.x installed on your computer. You also need to install the required Python modules by running the following command:

pip install -r requirements.txt


## Usage

To use the script, simply run the following command:

python transcript.py <path_to_audio_file>


Replace `<path_to_audio_file>` with the path to the audio file that you want to transcribe.

After running the script, it will create two files in the same directory as the audio file:

- A transcript file with the extension `.txt` containing the transcribed text
- A subtitle file with the extension `.srt` containing the subtitles

## License

This script is released under the MIT License. See LICENSE file for more information.
