from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3

def model():

    model = Model('./vosk-model-en-us-0.22-lgraph')
    recognizer = KaldiRecognizer(model, 16000)

    capture = pyaudio.PyAudio()
    stream = capture.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:

        data = stream.read(4096, exception_on_overflow=False)

        if len(data) == 0:
            break

        if recognizer.AcceptWaveform(data):
            return recognizer.Result()


def sayText(text):

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume',1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    return text
