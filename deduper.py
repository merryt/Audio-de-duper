import speech_recognition as sr

r = sr.Recognizer()


def input_audio_file(filename):
    audio_file = sr.AudioFile(filename)
    with audio_file as source:
        audio = r.record(source)
    return audio

def transcribe_audio(audio):
    transcription = r.recognize_google(audio, key="AIzaSyDRdSN1VaRW27HxA68rZW5FesS2qoPD8")
    print(transcription)
    return transcription

firstfile = input_audio_file("source_files/Daily 2018-11-10.wav")
transcribe_audio(firstfile)
