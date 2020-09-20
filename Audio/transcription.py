import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def transcribe():
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    file_name = os.path.join(
        os.path.dirname(__file__),
        'audio',
        'file1.flac')

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        language_code='en-US',
        audio_channel_count = 2,
        enable_automatic_punctuation=True)
    # print(config,audio)
    # Detects speech in the audio file
    response = client.recognize(config, audio)
    f = open('transcript.txt','w')
    for result in response.results:
        f.write(result.alternatives[0].transcript)
    f.close()