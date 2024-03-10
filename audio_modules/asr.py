from vosk import Model, KaldiRecognizer
import pyaudio

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
            print(recognizer.Result())
            return recognizer.Result()