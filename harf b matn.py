import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Dar hal goosh dadan...")
    try:
        audio_data = r.record(source, duration=5)
        print("Dar hal tashkhis goftar...")
        text = r.recognize_google(audio_data, language="fa")
        print("Shoma goftid:", text)
    except sr.UnknownValueError:
        print("Motavajeh nashodam, lotfan dobare emtehan konid.")
    except sr.RequestError:
        print("Etesal be internet ra barresi konid.")
