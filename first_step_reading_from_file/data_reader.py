import speech_recognition as sr
import logger as l

def read_wav_file(path):
    l.logger.info(f'reading wav file, path: {path}')
    recognizer = sr.Recognizer()

    with sr.AudioFile(path) as wav:
        audio = recognizer.record(wav)
        text = recognizer.recognize_google(audio_data=audio)
    l.logger.info('reading succesffully')
    return text