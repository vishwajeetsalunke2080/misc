import speech_recognition as sr

r=sr.Recognizer()
file=sr.AudioFile('welcome.wav')
with file as source:
    r.adjust_for_ambient_noise(source)
    audio=r.record(source, duration=5)
    result=r.recognize_google(audio,show_all=True,language='en')
    print(result)
