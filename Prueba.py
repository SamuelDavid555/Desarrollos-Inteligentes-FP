import speech_recognition as sr

r = sr.Recognizer()

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

with sr.Microphone() as source:
    print("Say Something...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='es-ES')
        palabra = "{}".format(text)
        print("What did you say: {}".format(text))
        palabra = normalize(palabra)
        resSplit = palabra.split()
        print(resSplit)
    except:
        print("I am sorry! I can not understand!")