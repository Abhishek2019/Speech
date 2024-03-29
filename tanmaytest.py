import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import speech_recognition as sr

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'resources',
#     'audio.raw')

# Loads the audio into memory
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# with io.open(file_name, 'rb') as audio_file:
#     content = audio_file.read()
#     audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(

    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)
alternatives = response.results[0].alternatives

for alternative in alternatives:
    print('Transcript: {}'.format(alternative.transcript))
