import speech_recognition as sr


def read_wav_file(path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(path) as wav:
        audio = recognizer.record(wav)
        text = recognizer.recognize_google(audio_data=audio)
    return text